async function * mockStream() {
  for (let i = 0; i < 500000; i++) {
    yield { choices: [{ delta: { content: "hello " } }] };
  }
}

async function runOriginal() {
  const stream = mockStream();
  const start = Date.now();
  for await (const chunk of stream) {
    const delta = chunk.choices?.[0]?.delta?.content;
    if (delta) {
      process.stdout.write(delta);
    }
  }
  process.stdout.write("\n");
  const end = Date.now();
  console.error("Original time:", end - start);
}

async function runBuffered() {
  const stream = mockStream();
  const start = Date.now();
  let buffer = "";
  for await (const chunk of stream) {
    const delta = chunk.choices?.[0]?.delta?.content;
    if (delta) {
      buffer += delta;
      if (buffer.length >= 8192) {
        process.stdout.write(buffer);
        buffer = "";
      }
    }
  }
  if (buffer.length > 0) process.stdout.write(buffer);
  process.stdout.write("\n");
  const end = Date.now();
  console.error("Buffered time:", end - start);
}

async function runBackpressure() {
  const stream = mockStream();
  const start = Date.now();
  for await (const chunk of stream) {
    const delta = chunk.choices?.[0]?.delta?.content;
    if (delta) {
      if (!process.stdout.write(delta)) {
        await new Promise(resolve => process.stdout.once('drain', resolve));
      }
    }
  }
  process.stdout.write("\n");
  const end = Date.now();
  console.error("Backpressure time:", end - start);
}

const type = process.argv[2];
if (type === 'original') runOriginal();
else if (type === 'buffered') runBuffered();
else if (type === 'backpressure') runBackpressure();
