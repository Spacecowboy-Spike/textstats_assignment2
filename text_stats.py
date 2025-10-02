import re
"""
Pure text-processing functions (no I/O or exceptions).

Responsibilities:
- Tokenize words (A–Z only, case-insensitive).
- Count characters (with and without spaces).
- Compute: word count, unique words, average word length (one decimal).
- Determine most common word(s) and frequency; alphabetical order for ties.
- Format the six output lines in the exact required text format.

Rules:
- No input(), no print(), no file I/O, no try/except here.
- Keep functions small, composable, and testable.
"""

# Hints (do not implement here yet):
# - Consider a constant regex pattern for words.
# - Separate calculation from formatting.
# - Return data structures that are easy to test.

# --- Word extraction: letters only (A–Z/a–z), case-insensitive for counting/uniqueness ---
def tokenize_words(text_content):
    
    lowered_text = text_content.lower()
    word_list = re.findall(r"[a-zA-Z]+", lowered_text)
    return word_list


# --- Word statistics ---
def word_count(word_list):
    word_count = len(word_list)
    unique_word_count = len(set(word_list))
    return word_count, unique_word_count

# --- Text stats summary ---
def stats_summary(word_count, unique_word_count, characters_with_spaces,
                characters_no_spaces, average_word_length_str,
                most_common_line):
    return {
        "word_count": word_count,
        "unique_word_count": unique_word_count,
        "characters_with_spaces": characters_with_spaces,
        "characters_no_spaces": characters_no_spaces,
        "average_word_length_str": average_word_length_str,
        "most_common_line": most_common_line}