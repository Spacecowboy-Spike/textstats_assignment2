import re
from collections import Counter
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


# --- Character counts ---
def count_chars(text_content):
    characters_with_spaces = len(text_content)
    characters_no_spaces = 0
    char_index = 0
    while char_index < len(text_content):
        current_char = text_content[char_index]
        if not current_char.isspace():
            characters_no_spaces += 1
        char_index += 1
    return characters_no_spaces, characters_with_spaces


# average word length with one decimal; 0.0 if there are no words
def average_word_length_str(word_list, word_count):
    # total letters across all words
    total_letter_count = 0
    word_index = 0
    while word_index < len(word_list):
        total_letter_count += len(word_list[word_index])
        word_index += 1
    average_word_length = (total_letter_count / word_count) if word_count != 0 else 0.0
    average_word_length_str = f"{average_word_length:.1f}"
    return average_word_length_str


# --- Word statistics ---
def word_count(word_list):
    word_count = len(word_list)
    unique_word_count = len(set(word_list))
    return word_count, unique_word_count


# --- Most common word(s) and frequency ---
def most_common_word(word_count, word_list):
    if word_count == 0:
        most_common_line = "Most common word(s): (0)"
    else:
        word_counts = Counter(word_list)
        highest_frequency = 0
        for word in word_counts:
            if word_counts[word] > highest_frequency:
                highest_frequency = word_counts[word]
        most_frequent_words = []
        for word in word_counts:
            if word_counts[word] == highest_frequency:
                most_frequent_words.append(word)
        most_frequent_words.sort()
        if len(most_frequent_words) == 1:
            most_common_line = f"Most common word(s): {most_frequent_words[0]} ({highest_frequency})"
        else:
            most_common_line = f"Most common word(s): {', '.join(most_frequent_words)} ({highest_frequency})"
        return most_common_line


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
    
    
# --- Build the six required lines in the exact order/format ---
def format_report(stats_summary):
    output_lines = [
        f"Word count: {stats_summary['word_count']}",
        f"Unique words: {stats_summary['unique_word_count']}",
        f"Characters (with spaces): {stats_summary['characters_with_spaces']}",
        f"Characters (no spaces): {stats_summary['characters_no_spaces']}",
        f"Average word length: {stats_summary['average_word_length_str']}",
        stats_summary['most_common_line'],
    ]
    return output_lines