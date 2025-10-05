import text_stats
import io_ops


"""
Entry point (orchestration only).

TODO (team):
- Prompt for input file path (interactive) — keep logic minimal.
- Call functions from text_stats.py to compute results.
- Print six output lines in exact format.
- Prompt for output file, confirm overwrite, write lines via io_ops.py.
- Ensure this file stays "thin" — no heavy logic here.
"""

# from io_ops import ...   # TODO: import the small set of I/O helpers you create
# from text_stats import ...  # TODO: import your pure functions

def main() -> None:
    # TODO: glue together a simple flow:
    # 1) get input path (prompt)
    filename_input = io_ops.prompt_nonempty()
    # 2) read text (io_ops)
    text_content = io_ops.read_text(filename_input)
    # 3) compute metrics (text_stats)
    stats_summary = text_stats.stats_summary(text_content)
    # 4) print to console
    output_lines = text_stats.format_report(stats_summary)
    line_index = 0
    while line_index < len(output_lines):
        print(output_lines[line_index])
        line_index += 1
    # 5) write to output file (io_ops)
    filename_output = io_ops.write_filename()
    io_ops.write_lines(output_lines, filename_output)

if __name__ == "__main__":
    main()
