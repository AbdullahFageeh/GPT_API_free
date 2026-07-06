/*
Dependency (Maven):
<dependency>
  <groupId>com.openai</groupId>
  <artifactId>openai-java</artifactId>
  <version>LATEST_VERSION</version>
</dependency>

Dependency (Gradle):
implementation("com.openai:openai-java:LATEST_VERSION")
*/

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.StreamResponse;
import com.openai.models.ChatModel;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionChunk;
import com.openai.models.chat.completions.ChatCompletionCreateParams;
import java.io.PrintStream;

public class DemoJava {
    private static final OpenAIClient client = OpenAIOkHttpClient.builder()
            .apiKey(System.getenv().getOrDefault("OPENAI_API_KEY", "YOUR API KEY"))
            .baseUrl("https://api.chatanywhere.tech/v1")
            .build();

    // Non-stream response
    public static void gpt35Api(String userText) {
        ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
                .model(ChatModel.GPT_3_5_TURBO)
                .addUserMessage(userText)
                .build();

        ChatCompletion completion = client.chat().completions().create(params);
        String content = completion.choices().get(0).message().content().orElse("");
        System.out.println(content);
    }

    // Stream response
    public static void gpt35ApiStream(String userText) {
        ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
                .model(ChatModel.GPT_3_5_TURBO)
                .addUserMessage(userText)
                .build();

        // Caching System.out to a local variable for slightly better performance in the loop
        PrintStream out = System.out;
        try (StreamResponse<ChatCompletionChunk> stream = client.chat().completions().createStreaming(params)) {
            stream.stream().forEach(chunk -> {
                if (!chunk.choices().isEmpty()) {
                    String delta = chunk.choices().get(0).delta().content().orElse("");
                    if (!delta.isEmpty()) {
                        out.print(delta);
                    }
                }
            });
            out.println();
        }
    }

    public static void main(String[] args) {
        String prompt = "What is the relationship between Lu Xun and Zhou Shuren?";

        // Non-stream call
        // gpt35Api(prompt);

        // Stream call
        gpt35ApiStream(prompt);
    }
}
