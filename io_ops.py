"""
User interaction & file I/O. Implement guards (validation) + try/except here.

Guidance:
- Prompt for input filename (reject empty; re-prompt).
- Read text with UTF-8; handle FileNotFoundError, PermissionError, UnicodeDecodeError.
- Prompt for output filename (default to 'output.txt').
- If output exists, confirm overwrite (y/n; re-prompt on invalid).
- Write lines; handle PermissionError/OSError.
- Never crash on user mistakes; re-prompt or exit gracefully with a helpful message.

Note:
- Keep function responsibilities small and names descriptive.
- No heavy text-processing logic belongs here.
"""

# TODO: define small helpers such as:
# def prompt_nonempty(prompt_text: str) -> str: ...
# def read_text_file(path: str) -> str: ...
# def confirm_overwrite(path: str) -> bool: ...
# def write_lines(path: str, lines: list[str]) -> bool: ...
