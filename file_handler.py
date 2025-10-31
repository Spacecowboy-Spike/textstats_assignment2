from pathlib import Path
"""
File handling operations for text statistics program.
Handles user prompts, file reading, and file writing with error handling.
"""

class FileHandler:
    """Manages all file input/output operations."""
    
    def prompt_for_input_file(self):
        """Prompt user for input filename with validation."""
        try:
            while True:
                filename = input('Please type the filename you want to read: ').strip()
                if len(filename) == 0:
                    print('Filename must not be empty')
                    continue
                if not filename.lower().endswith(".txt"):
                    filename += '.txt'
                file_path = Path(filename)
                if not file_path.exists():
                    print(f"File '{filename}' not found in current directory.")
                    continue
                return filename
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None
    
    def prompt_for_output_file(self):
        """Prompt user for output filename with validation."""
        while True:
            filename = input('Please name the filename you want to write: ').strip()
            if len(filename) == 0:
                print('Filename must not be empty')
                continue
            if not filename.lower().endswith(".txt"):
                filename += '.txt'
            file_path = Path(filename)
            if file_path.exists():
                rewrite = input(f"File '{filename}' is already exists in current directory, do you want to overwrite it(yes/no)? ")
                if rewrite.strip().lower() == 'yes':
                    return filename
                else:
                    continue
            return filename
    
    def read_file(self, filename):
        """Read and return contents of a file."""
        try:
            with open(filename, "r", encoding="utf-8") as file_in:
                text_content = file_in.read()
            return text_content
        
        except FileNotFoundError:
            print(f"\nError: The file '{filename}' was not found.")
            raise

        except PermissionError:
            print(f"\nError: Permission denied while trying to read '{filename}'.")
            raise
    
    def write_file(self, filename, content):
        """Write content to a file."""
        try:
            with open(filename, "w", encoding="utf-8") as file_out:
                line_index = 0
            while line_index < len(content):
                file_out.write(content[line_index] + ("\n" if line_index < len(content) - 1 else ""))
                line_index += 1
                
            print(f"File '{filename}' written successfully.")
        except PermissionError:
            print(f"\nError: Permission denied while trying to write '{filename}'.")
            raise

        except IOError:
            print(f"\nError: An I/O error occurred while writing to '{filename}'.")
            raise