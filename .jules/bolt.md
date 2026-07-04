## 2026-07-06 - Optimize Python Streaming Performance
**Learning:** Python streaming implementations for LLM responses can be bottlenecked by `print()` overhead and repeated nested attribute lookups (e.g., `chunk.choices[0].delta.content`) within the loop. Caching `sys.stdout.write` and localizing attribute access significantly reduces the per-chunk overhead.
**Action:** Always cache `sys.stdout.write` and use local variables for deeply nested attributes in performance-critical loops.
