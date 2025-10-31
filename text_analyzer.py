from collections import Counter
"""
Statistical analysis of text data.
Calculates word counts, character counts, and frequency statistics.
"""

class TextAnalyzer:
    """Analyzes text and generates statistics."""
    
    def __init__(self, raw_text, words):
        """Initialize with raw text and processed word list."""
        self.raw_text = raw_text
        self.words = words
        self.word_count = len(words)
        self.unique_word_count = 0
        self.char_count_with_spaces = 0
        self.char_count_no_spaces = 0
        self.avg_word_length = 0.0
        self.most_common_words = []
        self.summary = {}
    
    def analyze(self):
        """Calculate all text statistics."""
        
            
        # --- Character counts ---
        self.char_count_no_spaces, self.char_count_with_spaces = self.count_chars()
        self.summary["char_count_with_spaces"] = self.char_count_with_spaces
        self.summary["char_count_no_spaces"] = self.char_count_no_spaces
        
        # --- Word statistics ---
        self.word_count, self.unique_word_count = self.word_count()
        self.summary["word_count"] = self.word_count
        self.summary["unique_word_count"] = self.unique_word_count

        # average word length with one decimal; 0.0 if there are no words
        self.avg_word_length = self.avg_word_length_str()
        self.summary["avg_word_length_str"] = self.avg_word_length

        # --- Most common word(s) and frequency ---
        self.most_common_words = self.most_common_word()
        self.summary["most_common_line"] = self.most_common_words


        return self.summary
        
        
# --- Character counts ---   
    def count_chars(self):
        self.self.char_count_with_spaces = len(self.raw_text)
        self.char_count_no_spaces = 0
        char_index = 0
        while char_index < len(self.raw_text):
            current_char = self.raw_text[char_index]
            if not current_char.isspace():
                self.char_count_no_spaces += 1
            char_index += 1
        return self.char_count_no_spaces, self.char_count_with_spaces


# average word length with one decimal; 0.0 if there are no words
    def average_word_length_str(self):
        # total letters across all words
        total_letter_count = 0
        word_index = 0
        while word_index < len(self.words):
            total_letter_count += len(self.words[word_index])
            word_index += 1
        self.avg_word_length = (total_letter_count / self.word_count) if self.word_count != 0 else 0.0
        self.avg_word_length = f"{self.avg_word_length:.1f}"
        return self.avg_word_length

# --- Word statistics ---
    def word_count(self):
        self.word_count = len(self.words)
        self.unique_word_count = len(set(self.words))
        return self.word_count, self.unique_word_count


# --- Most common word(s) and frequency ---
    def most_common_word(self):
        if self.word_count == 0:
            self.most_common_words = "Most common word(s): (0)"
        else:
            word_counts = Counter(self.words)
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
                self.most_common_words = f"Most common word(s): {most_frequent_words[0]} ({highest_frequency})"
            else:
                self.most_common_words = f"Most common word(s): {', '.join(most_frequent_words)} ({highest_frequency})"
            return self.most_common_words


    
    def get_formatted_output(self):
        """Return formatted statistics as a string."""
        output_lines = [
        f"Word count: {self.summary['word_count']}",
        f"Unique words: {self.summary['unique_word_count']}",
        f"Characters (with spaces): {self.summary['characters_with_spaces']}",
        f"Characters (no spaces): {self.summary['characters_no_spaces']}",
        f"Average word length: {self.summary['average_word_length_str']}",
        self.summary['most_common_line'],
        ]
        return output_lines