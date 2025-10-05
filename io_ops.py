from pathlib import Path
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
def prompt_nonempty():
    while True:
        filename = input('Please type the filename you want to read: ').strip()
        if len(filename) == 0:
            print('Filename must not be empty')
            continue
        filename += '.txt'
        file_path = Path(filename)
        if not file_path.exists():
            print(f"File '{filename}' not found in current directory.")
            continue
        return filename


#--- Read the raw file text (assumes input.txt exists in the same folder) ---
def read_text(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        text_content = file_in.read()
    return text_content


# def confirm_overwrite(path: str) -> bool: ...
def write_filename():
    while True:
        filename = input('Please name the filename you want to write: ').strip()
        if len(filename) == 0:
            print('Filename must not be empty')
            continue
        filename += '.txt'
        file_path = Path(filename)
        if file_path.exists():
            rewrite = input(f"File '{filename}' is already exists in current directory, do you want to overwrite it(yes/no)? ")
            if rewrite.strip().lower() == 'yes':
                return filename
            else:
                continue
        return filename

# --- Write to output.txt ---
def write_lines(output_lines, filename):
    with open(filename, "w", encoding="utf-8") as file_out:
        line_index = 0
        while line_index < len(output_lines):
            file_out.write(output_lines[line_index] + ("\n" if line_index < len(output_lines) - 1 else ""))
            line_index += 1