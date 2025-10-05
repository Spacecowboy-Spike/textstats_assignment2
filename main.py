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
    # 4) print to console
    # 5) write to output file (io_ops)
    filename_output = io_ops.write_filename()
    io_ops.write_lines(output_lines, filename_output)
    pass




    # --- Character counts ---
    characters_no_spaces, characters_with_spaces = text_stats.count_chars(text_content)

    # --- Word extraction: letters only (A–Z/a–z), case-insensitive for counting/uniqueness ---
    word_list = text_stats.tokenize_words(text_content)

    # --- Word statistics ---
    word_count, unique_word_count = text_stats.word_count(word_list)

    # average word length with one decimal; 0.0 if there are no words
    average_word_length_str = text_stats.average_word_length_str(word_list, word_count)

    # --- Most common word(s) and frequency ---
    most_common_line = text_stats.most_common_word(word_count, word_list)

    # --- Text stats summary ---
    stats_summary = text_stats.stats_summary(word_count, unique_word_count, characters_with_spaces,
                characters_no_spaces, average_word_length_str,
                most_common_line)
    
    # --- Build the six required lines in the exact order/format ---
    output_lines = text_stats.format_report(stats_summary)

    # --- Print to console ---
    line_index = 0
    while line_index < len(output_lines):
        print(output_lines[line_index])
        line_index += 1
        


if __name__ == "__main__":
    main()
