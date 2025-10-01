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
    # 2) read text (io_ops)
    # 3) compute metrics (text_stats)
    # 4) print to console
    # 5) write to output file (io_ops)
    pass

if __name__ == "__main__":
    main()
