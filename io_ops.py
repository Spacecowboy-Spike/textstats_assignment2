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

#--- Read the raw file text (assumes input.txt exists in the same folder) ---
def read_text(filepath='input.txt'):
    with open(filepath, "r", encoding="utf-8") as file_in:
        text_content = file_in.read()
    return text_content

# --- Write to output.txt ---
def output_report(output_lines, filepath='output.txt'):
    with open(filepath, "w", encoding="utf-8") as file_out:
        line_index = 0
        while line_index < len(output_lines):
            file_out.write(output_lines[line_index] + ("\n" if line_index < len(output_lines) - 1 else ""))
            line_index += 1