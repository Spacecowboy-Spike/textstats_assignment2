## Testing Log

### Test 1: Standard input file
- Input: `input_standard.txt`
- Expected: 

Word count: 7
Unique words: 7
Characters (with spaces): 38
Characters (no spaces): 31
Average word length: 4.3
Most common word: 'here', 'or', 'paste', 'sample', 'some', 'text', 'write' (1)

- Actual: 

Word count: 7
Unique words: 7
Characters (with spaces): 38
Characters (no spaces): 31
Average word length: 4.3
Most common word: 'here', 'or', 'paste', 'sample', 'some', 'text', 'write' (1)

- Status: ✓ Pass

### Test 2: Edge case - empty file
- Input: `input_empty.txt`
- Expected: 

Word count: 0
Unique words: 0
Characters (with spaces): 0
Characters (no spaces): 0
Average word length: 0.0
Most common word: N/A

- Actual: 

Word count: 0
Unique words: 0
Characters (with spaces): 0
Characters (no spaces): 0
Average word length: 0.0
Most common word: N/A

- Status: ✓ Pass

### Test 3: File with only spaces and punctuation
- Input: `input_space_punctuation.txt`
- Expected: 

Word count: 0
Unique words: 0
Characters (with spaces): 61
Characters (no spaces): 36
Average word length: 0.0
Most common word: N/A

- Actual: 

Word count: 0
Unique words: 0
Characters (with spaces): 61
Characters (no spaces): 36
Average word length: 0.0
Most common word: N/A

- Status: ✓ Pass
...

### Test 4: Long file
- Input: `input_long_file.txt`
- Expected: 

Word count: 1431
Unique words: 339
Characters (with spaces): 7731
Characters (no spaces): 6235
Average word length: 4.2
Most common word: 'and' (101)

- Actual: 

Word count: 1431
Unique words: 339
Characters (with spaces): 7731
Characters (no spaces): 6235
Average word length: 4.2
Most common word: 'and' (101)

- Status: ✓ Pass
...

### Test 5: User cancellation (Ctrl+C)
- Input: `input_long_file.txt`
- Expected: 
Operation cancelled by user.
- Actual: 

=== Text Statistics Analyzer (OOP) ===

[main] Initializing FileHandler and reading input file...
Please type the filename you want to read: 
Operation cancelled by user.

[main] Writing results to output file...
Please name the filename you want to write:
Operation cancelled by user.

- Status: ✓ Pass
...