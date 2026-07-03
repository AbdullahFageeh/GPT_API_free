import { vi, describe, it, expect, beforeEach, afterEach } from 'vitest';

const mockCreate = vi.fn();
vi.mock('openai', () => {
  return {
    default: class {
      constructor() {
        this.chat = {
          completions: {
            create: mockCreate
          }
        };
      }
    }
  };
});

// Import dynamically after setting up the mock
const { gpt35Api, gpt35ApiStream } = await import('./demo_nodejs.js');

describe('demo_nodejs', () => {
  let originalConsoleLog;
  let originalStdoutWrite;

  beforeEach(() => {
    originalConsoleLog = console.log;
    originalStdoutWrite = process.stdout.write;
    console.log = vi.fn();
    process.stdout.write = vi.fn();
  });

  afterEach(() => {
    console.log = originalConsoleLog;
    process.stdout.write = originalStdoutWrite;
    vi.clearAllMocks();
  });

  describe('gpt35Api', () => {
    it('should call completions.create and log the response', async () => {
      const messages = [{ role: 'user', content: 'test message' }];
      const mockResponse = {
        choices: [
          { message: { content: 'test response' } }
        ]
      };

      mockCreate.mockResolvedValueOnce(mockResponse);

      await gpt35Api(messages);

      expect(mockCreate).toHaveBeenCalledWith({
        model: 'gpt-3.5-turbo',
        messages
      });
      expect(console.log).toHaveBeenCalledWith('test response');
    });

    it('should log an empty string if content is undefined', async () => {
      const messages = [{ role: 'user', content: 'test message' }];
      const mockResponse = {
        choices: [{}]
      };

      mockCreate.mockResolvedValueOnce(mockResponse);

      await gpt35Api(messages);
      expect(console.log).toHaveBeenCalledWith('');
    });
  });

  describe('gpt35ApiStream', () => {
    it('should call completions.create with stream: true and write chunks to stdout', async () => {
      const messages = [{ role: 'user', content: 'test message' }];
      const mockStream = {
        async *[Symbol.asyncIterator]() {
          yield { choices: [{ delta: { content: 'chunk1' } }] };
          yield { choices: [{ delta: { content: 'chunk2' } }] };
          yield { choices: [{ delta: { content: undefined } }] };
          yield { choices: [{}] }; // no delta
        }
      };

      mockCreate.mockResolvedValueOnce(mockStream);

      await gpt35ApiStream(messages);

      expect(mockCreate).toHaveBeenCalledWith({
        model: 'gpt-3.5-turbo',
        messages,
        stream: true
      });
      expect(process.stdout.write).toHaveBeenCalledWith('chunk1');
      expect(process.stdout.write).toHaveBeenCalledWith('chunk2');
      expect(process.stdout.write).toHaveBeenCalledWith('\n');
      expect(process.stdout.write).toHaveBeenCalledTimes(3); // chunk1, chunk2, and newline
    });
  });
});
