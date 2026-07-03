package main

import (
	"context"
	"testing"

	openai "github.com/sashabaranov/go-openai"
)

func TestGpt35API_EmptyMessages(t *testing.T) {
	client := newClient()
	ctx := context.Background()

	var messages []openai.ChatCompletionMessage

	err := gpt35API(ctx, client, messages)
	if err == nil {
		t.Error("Expected an error when messages slice is empty, got nil")
	} else if err.Error() != "messages cannot be empty" {
		t.Errorf("Expected error message 'messages cannot be empty', got '%s'", err.Error())
	}
}
