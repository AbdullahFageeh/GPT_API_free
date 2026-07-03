import pytest
from unittest.mock import patch, MagicMock
from demo_python import gpt_35_api

def test_gpt_35_api_success(capsys):
    mock_messages = [{"role": "user", "content": "Hello"}]
    mock_response = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = "Hi there!"
    mock_response.choices = [mock_choice]

    with patch('demo_python.client.chat.completions.create', return_value=mock_response) as mock_create:
        gpt_35_api(mock_messages)
        mock_create.assert_called_once_with(model="gpt-3.5-turbo", messages=mock_messages)

        captured = capsys.readouterr()
        assert "Hi there!\n" == captured.out

def test_gpt_35_api_error(capsys):
    mock_messages = [{"role": "user", "content": "Hello"}]

    with patch('demo_python.client.chat.completions.create', side_effect=Exception("API limit reached")) as mock_create:
        gpt_35_api(mock_messages)
        mock_create.assert_called_once_with(model="gpt-3.5-turbo", messages=mock_messages)

        captured = capsys.readouterr()
        assert "An error occurred: API limit reached\n" == captured.out
