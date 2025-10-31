## OOP Refactor (Completed)

This project is being refactored from a functional design to object-oriented design.

### Branch Structure
- `main`: Working functional version
- `oop-refactor`: OOP version in development, I left it in case The instructor will review my assignment 2
- `assignment3`: Based on `oop-refactor`, continue to finish assignment 3

### New Class Structure
- `FileHandler`: Manages all file I/O operations
- `TextProcessor`: Handles text cleaning and tokenization  
- `TextAnalyzer`: Performs statistical analysis

### Status
- [x] Repository forked and cloned
- [x] OOP branch created
- [x] New main.py added
- [x] Class skeletons created
- [x] Classes implemented (Assignment 3)
- [x] Update README and documentation  


## Class Design

### FileHandler
Handles all file input/output operations.  
- Prompts the user for input/output filenames.  
- Validates file existence and manages overwriting prompts.  
- Reads text data from input files and writes results to output files.  

### TextProcessor
Processes raw text and extracts words.  
- Removes punctuation and converts text to lowercase.  
- Splits text into individual words.  
- Returns a clean list of words for analysis.  

### TextAnalyzer
Performs all statistical computations on the processed text.  
- Calculates word count, unique word count, and character counts.  
- Determines average word length.  
- Finds the most common word(s), handling ties alphabetically.  
- Computes word frequency distribution (called “letter frequency” for compatibility).  
- Generates a formatted report for output.


## How to Run

1. Open a terminal in the project directory.  
2. Run the main program:
   ```bash
   python main.py
3. When prompted, type the name of the input file (without .txt extension).
4. After processing, provide an output filename when prompted.
5. The analysis results will be saved in the specified .txt file.


## Design Decisions

- **Separation of concerns:** Each class handles one clear responsibility (I/O, processing, analysis).  
- **Modular Analysis Methods:**  
  In the `TextAnalyzer` class, instead of writing all logic inside a single `analyze()` method, I intentionally separated each computation into focused private helper methods (e.g., `_count_chars()`, `_compute_word_stats()`, `_compute_avg_word_length()`, etc.).  
  This modular structure improves readability, debugging, and reusability. 
  Each helper method performs one well-defined task, while `analyze()` simply coordinates their execution in order.  
  As a result, it’s easier to modify or test individual calculations without breaking the rest of the class.
- **Error handling:** All user inputs (including Ctrl+C) are caught gracefully to prevent crashes.  
- **Compatibility:** Method names strictly follow the interface expected by main.py.  
- **Determinism:** The most common word computation breaks ties alphabetically to ensure consistent output.