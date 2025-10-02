import re
from collections import Counter

WORD_PATTERN = re.compile(r"[a-zA-Z]+")

def tokenize(text):
    """
    Extract words (A-Z only) from text, lowercase.
    """
    return WORD_PATTERN.findall(text.lower())

def count_characters(text):
    """
    Count characters with and without spaces.
    Returns a tuple: (with_spaces, no_spaces)
    """
    with_spaces = len(text)
    no_spaces = sum(1 for c in text if not c.isspace())
    return with_spaces, no_spaces

def compute_stats(text):
    """
    Main function to compute all stats needed.
    Returns a dict with:
    - word_count, unique_words,
    - characters_with_spaces, characters_no_spaces,
    - average_word_length (float, one decimal place),
    - most_common (list of (word, count) tuples)
    """
    words = tokenize(text)
    characters_with_spaces, characters_no_spaces = count_characters(text)

    word_count = len(words)
    unique_words = len(set(words))

    total_letters = sum(len(w) for w in words)
    average_word_length = round(total_letters / word_count, 1) if word_count else 0.0

    word_counts = Counter(words)
    if word_counts:
        highest_freq = max(word_counts.values())
        most_common_words = sorted([w for w, c in word_counts.items() if c == highest_freq])
        most_common = [(w, highest_freq) for w in most_common_words]
    else:
        most_common = []

    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "characters_with_spaces": characters_with_spaces,
        "characters_no_spaces": characters_no_spaces,
        "average_word_length": average_word_length,
        "most_common": most_common
    }

def format_stats(stats):
    """
    Format the stats dict into output lines (list of strings).
    """
    lines = [
        f"Word count: {stats['word_count']}",
        f"Unique words: {stats['unique_words']}",
        f"Characters (with spaces): {stats['characters_with_spaces']}",
        f"Characters (no spaces): {stats['characters_no_spaces']}",
        f"Average word length: {stats['average_word_length']:.1f}"
    ]

    if not stats["most_common"]:
        lines.append("Most common word(s): (0)")
    else:
        words = ", ".join(word for word, count in stats["most_common"])
        count = stats["most_common"][0][1]
        lines.append(f"Most common word(s): {words} ({count})")

    return lines
