from collections import Counter

"""
Statistical analysis of text data.
Calculates word counts, character counts, and frequency statistics.
"""

class TextAnalyzer:
    """Analyzes text and generates statistics."""

    def __init__(self, raw_text, words):
        self.raw_text = raw_text or ""
        self.words = words or []

        # caches (filled by analyze)
        self.word_count = 0
        self.unique_word_count = 0
        self.char_count_with_spaces = 0
        self.char_count_no_spaces = 0
        self.avg_word_length_str = "0.0"     # keep 1-decimal string
        self._most_common = ("", 0)          # (word, count)
        self._letter_freqs = {}
        self._analyzed = False


    def analyze(self):
        """Run all computations by delegating to focused helpers."""
        self._count_chars()
        self._compute_word_stats()
        self._compute_avg_word_length()
        self._compute_most_common()
        self._compute_letter_freqs()
        self._analyzed = True

    # =========================
    # Private helpers (focused)
    # =========================
    def _count_chars(self):
        """Fill char_count_with_spaces / char_count_no_spaces."""
        self.char_count_with_spaces = len(self.raw_text)
        # faster than a manual while-loop
        self.char_count_no_spaces = sum(1 for ch in self.raw_text if not ch.isspace())

    def _compute_word_stats(self):
        """Fill word_count / unique_word_count."""
        self.word_count = len(self.words)
        self.unique_word_count = len(set(self.words))

    def _compute_avg_word_length(self):
        """Fill avg_word_length_str to 1 decimal."""
        if self.word_count == 0:
            self.avg_word_length_str = "0.0"
            return
        total_letters = sum(len(w) for w in self.words)
        self.avg_word_length_str = f"{total_letters / self.word_count:.1f}"

    def _compute_most_common(self):
        """Compute all tie-maximum words; join by ', ' and keep the shared max count."""
        if self.word_count == 0:
            self._most_common = ("", 0)
            return
        c = Counter(self.words)
        max_cnt = max(c.values())

        # Get all words have highest frequency
        tied_words = [w for w, n in c.items() if n == max_cnt]
        # Sort words alphabetically
        tied_words_sorted = sorted(set(tied_words), key=str.lower)

        # Join with comma and space
        combined = ", ".join(f"'{w}'" for w in tied_words_sorted)
        self._most_common = (combined, max_cnt)

    def _compute_letter_freqs(self):
        """Fill _letter_freqs counting only a-z (case-insensitive)."""
        self._word_freqs = Counter(self.words)


    # =========================
    # Design Probes API
    # (names must match main.py)
    # =========================
    def get_word_count(self):
        self._ensure_analyzed()
        return self.word_count

    def get_unique_word_count(self):
        self._ensure_analyzed()
        return self.unique_word_count

    def get_most_common_word(self):
        """Return (word, count); if no words -> ("", 0)."""
        self._ensure_analyzed()
        w, c = self._most_common
        # If w contains multiple comma-separated words (e.g., "'a', 'b', 'c'")
        # we manually format it into a cleaner printable string.
        if ", " in w:
        # Return a formatted string that looks like a tuple, 
        # but without Python automatically adding extra outer quotes.
            return f"({w}, {c})"
        else:
        # For a single word, keep a consistent tuple-like format.
            return f"('{w}', {c})"

    def get_letter_frequencies(self, include_zeros=True):
        """Return dict of letter->count word."""
        self._ensure_analyzed()
        return dict(self._word_freqs)

    # =========================
    # Official output
    # =========================
    def get_formatted_output(self):
        self._ensure_analyzed()
        lines = [
            "=== Text Statistics Report ===",
            f"Word count: {self.word_count}",
            f"Unique words: {self.unique_word_count}",
            f"Characters (with spaces): {self.char_count_with_spaces}",
            f"Characters (no spaces): {self.char_count_no_spaces}",
            f"Average word length: {self.avg_word_length_str}",
        ]
        w, c = self._most_common
        lines.append(
            f"Most common word: {w} ({c})" if c > 0 else "Most common word: N/A"
            )
        return "\n".join(lines)


    # =========================
    # Guard
    # =========================
    def _ensure_analyzed(self):
        if not self._analyzed:
            self.analyze()
