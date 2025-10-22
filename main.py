"""
Text Statistics Analyzer - OOP Version
Main entry point for the text analysis program.

This module orchestrates the text analysis workflow using object-oriented design.
Students should implement the TextAnalyzer, TextProcessor, and FileHandler 
classes to match the interface demonstrated here.
"""

from text_processor import TextProcessor
from text_analyzer import TextAnalyzer
from file_handler import FileHandler


def main():
    """
    Main function that orchestrates the text analysis workflow.
    
    Workflow:
    1. Prompt user for input filename
    2. Read the text file
    3. Create a TextProcessor and clean/tokenize the text
    4. Create a TextAnalyzer with the processed tokens
    5. Generate statistics
    6. Display results to console
    7. Prompt user for output filename
    8. Write results to file
    """
    print("=== Text Statistics Analyzer (OOP Version) ===\n")
    
    # Step 1 & 2: Get input file and read content
    file_handler = FileHandler()
    raw_text = file_handler.read_input_file()
    
    # Step 3: Process and tokenize the text
    processor = TextProcessor(raw_text)
    words = processor.get_words()
    
    # Step 4 & 5: Create analyzer and generate statistics
    analyzer = TextAnalyzer(raw_text, words)
    analyzer.analyze()
    
    # Step 6: Display results to console
    print("\n--- Analysis Results ---")
    print(analyzer.get_formatted_output())
    
    # Step 7 & 8: Write results to output file
    file_handler.write_output_file(analyzer.get_formatted_output())
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()