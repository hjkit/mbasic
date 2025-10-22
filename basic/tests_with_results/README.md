# Tests With Expected Results

This directory contains MBASIC 5.21 test programs with their expected output.

## Purpose

Unlike the programs in `bas_tests1/`, which are real-world programs we found but don't know the expected output for, these are **test cases** where we know exactly what the correct output should be.

## Format

For each test:
- **`test_name.bas`** - The MBASIC program
- **`test_name.txt`** - The expected output when the program is run

## Running Tests

To validate the interpreter/compiler:
1. Run the `.bas` file
2. Compare the output to the `.txt` file
3. Output should match exactly (or within acceptable floating-point tolerance)

## Current Tests

### test_operator_precedence.bas

Tests operator precedence to ensure operations are performed in the correct order.

**How it works:**
- The program itself checks each result and reports PASS/FAIL
- Each test assigns `RESULT = expression` and `EXPECTED = correct_value`
- A subroutine checks if RESULT equals EXPECTED
- Tracks pass/fail counts and prints summary at end

**Key test cases:**
- `3*3+1` should be 10, not 12 (multiplication before addition)
- `10-8/2` should be 6, not 1 (division before subtraction)
- `2*3^2` should be 18, not 36 (exponentiation before multiplication)
- `10\3+1` should be 4, not 3 (integer division before addition)
- `10 MOD 3+1` should be 2, not 0 (MOD before addition)
- `-2^2` should be -4, not 4 (exponentiation before negation)
- `0 OR 1 AND 0` should be 0, not 1 (AND before OR)
- And 13 more tests...

**MBASIC Operator Precedence (highest to lowest):**
1. Parentheses `()`
2. Exponentiation `^`
3. Negation (unary `-`)
4. Multiplication `*`, Division `/`, Integer Division `\`
5. Modulo `MOD`
6. Addition `+`, Subtraction `-`
7. Relational `=`, `<>`, `<`, `>`, `<=`, `>=`
8. Logical NOT
9. Logical AND
10. Logical OR
11. Logical XOR
12. Logical EQV
13. Logical IMP

**Note:** In MBASIC, TRUE is -1 and FALSE is 0.

## Adding New Tests

When adding new tests:
1. Create a descriptive test name (e.g., `test_string_functions.bas`)
2. Add comments explaining what each test validates
3. Create the corresponding `.txt` file with exact expected output
4. Update this README with a description of the new test
