from collections import Counter
import string

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
        self._letter_freqs = {ch: 0 for ch in string.ascii_lowercase}
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
        """Fill _most_common as (word, count) with deterministic tie-break."""
        if self.word_count == 0:
            self._most_common = ("", 0)
            return
        c = Counter(self.words)
        max_cnt = max(c.values())
        # tie-break by lexicographic order for determinism
        best = min([w for w, n in c.items() if n == max_cnt])
        self._most_common = (best, max_cnt)

    def _compute_letter_freqs(self):
        """Fill _letter_freqs counting only a-z (case-insensitive)."""
        self._letter_freqs = {ch: 0 for ch in string.ascii_lowercase}
        for ch in self.raw_text.lower():
            if ch in self._letter_freqs:
                self._letter_freqs[ch] += 1


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
        return self._most_common

    def get_letter_frequencies(self, include_zeros=True):
        """Return dict of letter->count (a-z, case-insensitive)."""
        self._ensure_analyzed()
        if include_zeros:
            return dict(self._letter_freqs)
        return {k: v for k, v in self._letter_freqs.items() if v > 0}

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
        lines.append(f"Most common word: '{w}' ({c})" if c > 0 else "Most common word: N/A")
        return "\n".join(lines)


    # =========================
    # Guard
    # =========================
    def _ensure_analyzed(self):
        if not self._analyzed:
            self.analyze()
