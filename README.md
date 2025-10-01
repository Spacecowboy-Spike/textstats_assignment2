# Text Stats — Refactor Starter (No Solution Code)

This starter repo contains empty module files with TODO comments. Your job:
- Extract pure text-processing logic into `text_stats.py` (no input/print/file I/O, no try/except).
- Implement user interaction + guards + exception handling in `io_ops.py`.
- Keep `main.py` minimal: prompt → call functions → print/write.

## How to Run
```bash
python main.py
```
(Your team decides on interactive prompts and defaults; document them here once implemented.)

## Output Requirements (exact format)
1. Word count
2. Unique words
3. Characters (with spaces)
4. Characters (no spaces)
5. Average word length (one decimal)
6. Most common word(s): alphabetical order for ties; `(0)` if no words

## Team Workflow
- Use a **feature branch** for each task (e.g., `refactor/modules`, `io/guards`).
- Open **Pull Requests** for review before merging to `main`.
- Track tasks with **Issues** and/or a **Project Board**.

## Definition of Done
- `main.py` orchestrates only.
- `text_stats.py` has no I/O or exceptions.
- `io_ops.py` validates user input and handles file exceptions.
- Program never crashes on bad input; re-prompts or exits gracefully.
- Output matches the spec exactly.
- README updated with run instructions and any assumptions.
