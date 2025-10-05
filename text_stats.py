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
def average_word_length_str(word_list, total_words):
    # total letters across all words
    total_letter_count = 0
    word_index = 0
    while word_index < len(word_list):
        total_letter_count += len(word_list[word_index])
        word_index += 1
    average_word_length = (total_letter_count / total_words) if total_words != 0 else 0.0
    average_word_length = f"{average_word_length:.1f}"
    return average_word_length


# --- Word statistics ---
def word_count(word_list):
    total_words = len(word_list)
    unique_word_count = len(set(word_list))
    return total_words, unique_word_count


# --- Most common word(s) and frequency ---
def most_common_word(total_words, word_list):
    if total_words == 0:
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
def stats_summary(text_content):
    
    # --- Character counts ---
    characters_no_spaces, characters_with_spaces = count_chars(text_content)

    # --- Word extraction: letters only (A–Z/a–z), case-insensitive for counting/uniqueness ---
    word_list = tokenize_words(text_content)

    # --- Word statistics ---
    total_words, unique_word_count = word_count(word_list)

    # average word length with one decimal; 0.0 if there are no words
    average_word_length = average_word_length_str(word_list, total_words)

    # --- Most common word(s) and frequency ---
    most_common_line = most_common_word(total_words, word_list)

    return {
        "word_count": total_words,
        "unique_word_count": unique_word_count,
        "characters_with_spaces": characters_with_spaces,
        "characters_no_spaces": characters_no_spaces,
        "average_word_length_str": average_word_length,
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