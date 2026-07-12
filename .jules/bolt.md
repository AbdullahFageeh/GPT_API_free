## 2026-07-06 - [Streaming Loop Optimization]
**Learning:** Caching `sys.stdout.write` and localizing nested attribute lookups (e.g., `chunk.choices[0].delta.content`) in Python streaming loops can reduce local CPU overhead by ~70% compared to standard `print()` calls in high-volume benchmarks. However, in network-bound LLM applications, this gain is often dwarfed by network latency.
**Action:** Use localized lookups and `sys.stdout.write` for streaming loops when performance is critical, but ensure it doesn't compromise code readability for demo purposes. Always include a final `flush()` and trailing newline.

## 2026-07-12 - [Go Streaming Loop Performance]
**Learning:** In Go, `fmt.Print` accepts variadic interface arguments, leading to interface boxing and reflection on every call. Using `os.Stdout.WriteString` and localizing the lookup to a local variable avoids this overhead.
**Action:** Prefer `os.Stdout.WriteString` for high-frequency string output in Go to minimize allocations and reflection.
