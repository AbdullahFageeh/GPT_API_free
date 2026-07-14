## 2026-07-06 - [Streaming Loop Optimization]
**Learning:** Caching `sys.stdout.write` and localizing nested attribute lookups (e.g., `chunk.choices[0].delta.content`) in Python streaming loops can reduce local CPU overhead by ~70% compared to standard `print()` calls in high-volume benchmarks. However, in network-bound LLM applications, this gain is often dwarfed by network latency.
**Action:** Use localized lookups and `sys.stdout.write` for streaming loops when performance is critical, but ensure it doesn't compromise code readability for demo purposes. Always include a final `flush()` and trailing newline.

## 2026-07-14 - [Style vs Tooling Conflict in Go]
**Learning:** The repository's Go files use 4-space indentation, which deviates from standard `go fmt` tab indentation. Running `go fmt` as a verification step causes massive whitespace diffs that can lead to PR rejection.
**Action:** After running `go fmt` for syntax validation, restore 4-space indentation using `sed -i 's/\t/    /g' [file]` to maintain codebase consistency.

## 2026-07-14 - [Safety in Node.js Property Localization]
**Learning:** In LLM streaming responses, the `choices` array in a chunk can occasionally be empty or undefined (e.g., in trailing metadata chunks). Replacing optional chaining `?.` with direct indexing `[0]` for "performance" introduces crash risks.
**Action:** Always maintain optional chaining or explicit length checks when localizing properties from stream chunks. Caching `choices?.[0]` still provides property access optimization without sacrificing safety.
