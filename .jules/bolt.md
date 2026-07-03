## 2026-07-16 - [Initial Research]
**Learning:** The repository consists primarily of documentation and demo scripts for an API proxy. Performance gains can be achieved by optimizing these scripts' execution paths and following best practices for the OpenAI-compatible APIs.
**Action:** Identify and implement micro-optimizations in the demo scripts (e.g., Python loop optimizations) to reduce execution overhead.

## 2026-07-16 - [Lessons from sys.stdout.flush()]
**Learning:** Adding `sys.stdout.flush()` in a tight loop significantly increases overhead due to frequent system calls. While it improves real-time visual feedback in some terminals, it is a performance regression for bulk processing or when standard buffering would suffice.
**Action:** Avoid `flush()` inside loops unless immediate visibility is strictly required and worth the performance trade-off. Prefer standard buffering for higher throughput.
