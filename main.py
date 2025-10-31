"""
Text Statistics Analyzer - OOP Version

Main entry point for the text analysis program.

This script orchestrates the workflow using three classes students implement:
- FileHandler      : user prompts, file reads/writes
- TextProcessor    : text cleaning and tokenization
- TextAnalyzer     : statistics and formatted report

IMPORTANT:
- The console prints below are **design probes** that call small, focused
  methods on TextAnalyzer. They are for visibility only and must NOT change
  the program’s final output. The official output is still whatever
  get_formatted_output() returns and what we write to the output file.
"""

from text_processor import TextProcessor
from text_analyzer import TextAnalyzer
from file_handler import FileHandler


def main():
    print("=== Text Statistics Analyzer (OOP) ===\n")

    # 1) Read input
    print("[main] Initializing FileHandler and reading input file...")
    file_handler = FileHandler()
    raw_text = file_handler.read_input_file()
    print(f"[main] Loaded {len(raw_text)} characters.\n")

    # 2) Process text
    print("[main] Initializing TextProcessor and extracting words...")
    processor = TextProcessor(raw_text)
    words = processor.get_words()
    print(f"[main] Extracted {len(words)} words.\n")

    # 3) Analyze
    print("[main] Initializing TextAnalyzer and running analyze()...")
    analyzer = TextAnalyzer(raw_text, words)
    analyzer.analyze()
    print("[main] analyze() complete.\n")

    # 4) Design probes (expected to exist; do not modify final output)
    print("--- Design Probes (for learning visibility only) ---")
    word_count = analyzer.get_word_count()
    print(f"[probe] get_word_count() -> {word_count}")

    unique_word_count = analyzer.get_unique_word_count()
    print(f"[probe] get_unique_word_count() -> {unique_word_count}")

    most_common_word = analyzer.get_most_common_word()
    print(f"[probe] get_most_common_word() -> {most_common_word}")

    letter_freqs_preview = analyzer.get_letter_frequencies(include_zeros=True)
    # Show a deterministic, tiny preview to avoid cluttering the console
    preview_keys = sorted(letter_freqs_preview.keys())[:5]
    preview = {k: letter_freqs_preview[k] for k in preview_keys}
    print(f"[probe] get_letter_frequencies(include_zeros=True) -> preview {preview}")
    print("--- End Design Probes ---\n")

    # 5) Official output (the program's actual result)
    print("--- Analysis Results ---")
    final_output = analyzer.get_formatted_output()
    print(final_output)

    # 6) Write results
    print("\n[main] Writing results to output file...")
    file_handler.write_output_file(final_output)

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
