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



def word_frequencies(word_count, word_list):
    # --- Most common word(s) and frequency -
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
    return most_common_line, most_frequent_words, highest_frequency






def most_common(n: int, word_freqs: Dict[str, int]) -> List[Tuple[str, int]]:
    """
    Return the 'n' most frequent word(s), sorted alphabetically on tie.

    Parameters:
        n (int): Maximum number of most common words to return.
        word_freqs (Dict[str, int]): Dictionary of word -> frequency.

    Returns:
        List[Tuple[str, int]]: List of (word, frequency) tuples.
    """
    if not word_freqs or n <= 0:
        return []

    max_freq = max(word_freqs.values())
    most_frequent = [(word, freq) for word, freq in word_freqs.items() if freq == max_freq]
    most_frequent_sorted = sorted(most_frequent, key=lambda x: x[0])

    return most_frequent_sorted[:n]


def compute_stats(text: str) -> Dict[str, Any]:
    """
    Compute all required statistics from the text.

    Parameters:
        text (str): The raw input text.

    Returns:
        Dict[str, Any]: Dictionary containing computed text statistics.
    """
    tokens = tokenize(text)
    freqs = word_frequencies(tokens)

    word_count = len(tokens)
    unique_words = len(set(tokens))
    characters_with_spaces = len(text)
    characters_no_spaces = sum(1 for c in text if not c.isspace())
    total_letters = sum(len(word) for word in tokens)
    avg_word_length = round((total_letters / word_count), 1) if word_count > 0 else 0.0
    most_common_words_list = most_common(len(freqs), freqs)

    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "characters_with_spaces": characters_with_spaces,
        "characters_no_spaces": characters_no_spaces,
        "average_word_length": avg_word_length,
        "most_common": most_common_words_list,
    }

