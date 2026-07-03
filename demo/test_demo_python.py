import pytest
from unittest.mock import MagicMock
from demo.demo_python import gpt_35_api, gpt_35_api_stream
from openai import OpenAIError

def test_gpt_35_api_success(mocker, capsys):
    # Mock the openai client used in demo_python
    mock_client = mocker.patch('demo.demo_python.client')

    # Create mock response structure
    mock_choice = MagicMock()
    mock_choice.message.content = "This is a test response."
    mock_completion = MagicMock()
    mock_completion.choices = [mock_choice]

    # Set the return value for client.chat.completions.create
    mock_client.chat.completions.create.return_value = mock_completion

    # Define test messages
    messages = [{'role': 'user', 'content': 'Test message'}]

    # Call the function
    gpt_35_api(messages)

    # Verify the mock was called with correct arguments
    mock_client.chat.completions.create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Verify the output
    captured = capsys.readouterr()
    assert captured.out.strip() == "This is a test response."

def test_gpt_35_api_error(mocker):
    # Mock the openai client used in demo_python to raise an error
    mock_client = mocker.patch('demo.demo_python.client')
    mock_client.chat.completions.create.side_effect = OpenAIError("API Error")

    messages = [{'role': 'user', 'content': 'Test message'}]

    # Verify the exception is propagated
    with pytest.raises(OpenAIError, match="API Error"):
        gpt_35_api(messages)


def test_gpt_35_api_stream_success(mocker, capsys):
    # Mock the openai client used in demo_python
    mock_client = mocker.patch('demo.demo_python.client')

    # Create a generator function to simulate stream chunks
    def mock_stream():
        # First chunk
        chunk1 = MagicMock()
        chunk1.choices = [MagicMock()]
        chunk1.choices[0].delta.content = "Stream "
        yield chunk1

        # Second chunk with None content (simulating role chunk or similar)
        chunk2 = MagicMock()
        chunk2.choices = [MagicMock()]
        chunk2.choices[0].delta.content = None
        yield chunk2

        # Third chunk
        chunk3 = MagicMock()
        chunk3.choices = [MagicMock()]
        chunk3.choices[0].delta.content = "response."
        yield chunk3

    # Set the return value for client.chat.completions.create
    mock_client.chat.completions.create.return_value = mock_stream()

    # Define test messages
    messages = [{'role': 'user', 'content': 'Test message stream'}]

    # Call the function
    gpt_35_api_stream(messages)

    # Verify the mock was called with correct arguments
    mock_client.chat.completions.create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    # Verify the output (it should ignore the None content)
    captured = capsys.readouterr()
    assert captured.out == "Stream response."

def test_gpt_35_api_stream_error(mocker):
    # Mock the openai client used in demo_python to raise an error
    mock_client = mocker.patch('demo.demo_python.client')
    mock_client.chat.completions.create.side_effect = OpenAIError("API Stream Error")

    messages = [{'role': 'user', 'content': 'Test message stream'}]

    # Verify the exception is propagated
    with pytest.raises(OpenAIError, match="API Stream Error"):
        gpt_35_api_stream(messages)
