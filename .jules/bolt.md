## 2026-07-06 - [Streaming Loop Optimization]
**Learning:** Caching `sys.stdout.write` and localizing nested attribute lookups (e.g., `chunk.choices[0].delta.content`) in Python streaming loops can reduce local CPU overhead by ~70% compared to standard `print()` calls in high-volume benchmarks. However, in network-bound LLM applications, this gain is often dwarfed by network latency.
**Action:** Use localized lookups and `sys.stdout.write` for streaming loops when performance is critical, but ensure it doesn't compromise code readability for demo purposes. Always include a final `flush()` and trailing newline.

## 2026-07-06 - [Go and Node.js Streaming Loop Optimization]
**Learning:** In Go, using `os.Stdout.WriteString` instead of `fmt.Print` in high-frequency loops (like LLM token streaming) avoids reflection and internal formatting overhead, providing a small but measurable CPU gain. In Node.js, caching `process.stdout.write.bind(process.stdout)` and localizing nested property lookups (e.g., `chunk.choices[0]`) similarly reduces overhead in hot loops.
**Action:** Apply these localized optimizations in streaming scenarios across different languages to minimize local execution overhead, even when the primary bottleneck is network latency.
