package main

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/sashabaranov/go-openai"
)

func TestGpt35API_Success(t *testing.T) {
	// Create a mock HTTP server
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Verify the request
		if r.URL.Path != "/chat/completions" {
			t.Errorf("Expected to request '/chat/completions', got: %s", r.URL.Path)
		}

		// Mock response body
		response := openai.ChatCompletionResponse{
			ID:      "chatcmpl-123",
			Object:  "chat.completion",
			Created: 1677652288,
			Model:   openai.GPT3Dot5Turbo,
			Choices: []openai.ChatCompletionChoice{
				{
					Index: 0,
					Message: openai.ChatCompletionMessage{
						Role:    openai.ChatMessageRoleAssistant,
						Content: "Hello, world!",
					},
					FinishReason: "stop",
				},
			},
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(response)
	}))
	defer server.Close()

	// Configure the client to use the mock server
	config := openai.DefaultConfig("dummy-api-key")
	config.BaseURL = server.URL
	client := openai.NewClientWithConfig(config)

	// Define test input
	messages := []openai.ChatCompletionMessage{
		{
			Role:    openai.ChatMessageRoleUser,
			Content: "Say hello",
		},
	}

	// Call the function
	err := gpt35API(context.Background(), client, messages)

	// Verify no error
	if err != nil {
		t.Fatalf("Expected no error, got: %v", err)
	}
}

func TestGpt35API_Error(t *testing.T) {
	// Create a mock HTTP server returning an error
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte(`{"error": {"message": "Internal server error", "type": "server_error"}}`))
	}))
	defer server.Close()

	// Configure the client to use the mock server
	config := openai.DefaultConfig("dummy-api-key")
	config.BaseURL = server.URL
	client := openai.NewClientWithConfig(config)

	// Define test input
	messages := []openai.ChatCompletionMessage{
		{
			Role:    openai.ChatMessageRoleUser,
			Content: "Say hello",
		},
	}

	// Call the function
	err := gpt35API(context.Background(), client, messages)

	// Verify error occurred
	if err == nil {
		t.Fatalf("Expected an error but got nil")
	}
}
