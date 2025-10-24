#!/usr/bin/env python3
"""Test uninitialized variable detection"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from lexer import tokenize
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

# Test 1: Use before assignment
test1 = """
10 PRINT X
20 X = 10
30 END
"""

# Test 2: Assignment before use - no warning
test2 = """
10 X = 10
20 PRINT X
30 END
"""

# Test 3: FOR loop variable - no warning
test3 = """
10 FOR I = 1 TO 10
20 PRINT I
30 NEXT I
40 END
"""

# Test 4: INPUT statement - no warning
test4 = """
10 INPUT A
20 PRINT A
30 END
"""

# Test 5: READ statement - no warning
test5 = """
10 DATA 10, 20, 30
20 READ X
30 PRINT X
40 END
"""

# Test 6: LINE INPUT - no warning
test6 = """
10 LINE INPUT A$
20 PRINT A$
30 END
"""

# Test 7: Multiple uninitialized uses
test7 = """
10 Y = X + Z
20 PRINT X
30 X = 10
40 Z = 20
50 END
"""

# Test 8: Array element uninitialized (arrays are implicitly dimensioned)
test8 = """
10 DIM A(10)
20 PRINT A(5)
30 END
"""

# Test 9: Uninitialized in expression
test9 = """
10 A = 5
20 B = A + C
30 C = 10
40 END
"""

# Test 10: Initialized in condition
test10 = """
10 IF X > 0 THEN PRINT "POSITIVE"
20 X = 10
30 END
"""

# Test 11: Conditional initialization path
test11 = """
10 INPUT A
20 IF A > 0 THEN X = 10
30 PRINT X
40 END
"""

# Test 12: Initialized in one branch, used after
test12 = """
10 INPUT A
20 IF A > 0 THEN GOTO 50
30 X = 10
40 GOTO 60
50 X = 20
60 PRINT X
70 END
"""

# Test 13: DEF FN with uninitialized variable
test13 = """
10 DEF FNTEST(A) = A + B
20 PRINT FNTEST(5)
30 B = 10
40 END
"""

# Test 14: Multiple variables, some initialized
test14 = """
10 A = 10
20 B = A + C
30 D = B + E
40 C = 20
50 E = 30
60 END
"""

print("=" * 70)
print("UNINITIALIZED VARIABLE DETECTION TEST")
print("=" * 70)

tests = [
    (test1, "Use before assignment", 1, ["X"]),
    (test2, "Assignment before use", 0, []),
    (test3, "FOR loop variable", 0, []),
    (test4, "INPUT statement", 0, []),
    (test5, "READ statement", 0, []),
    (test6, "LINE INPUT", 0, []),
    (test7, "Multiple uninitialized", 3, ["X", "Z"]),  # X used twice before init
    (test8, "Array element", 0, []),  # Arrays auto-initialize to 0
    (test9, "Uninitialized in expr", 1, ["C"]),
    (test10, "Uninitialized in condition", 1, ["X"]),
    (test11, "Conditional init path", 0, []),  # X is initialized in THEN branch before use
    (test12, "Initialized in all branches", 0, []),  # Initialized in both branches
    (test13, "DEF FN uninitialized", 1, ["B"]),
    (test14, "Multiple mixed", 2, ["C", "E"]),
]

passed = 0
failed = 0

for i, (test_code, description, expected_count, expected_vars) in enumerate(tests, 1):
    print(f"\nTest {i}: {description}")

    try:
        tokens = tokenize(test_code)
        parser = Parser(tokens)
        program = parser.parse()
        analyzer = SemanticAnalyzer()
        success = analyzer.analyze(program)

        if not success:
            print(f"  ✗ FAIL: Analysis failed")
            print(f"    Errors: {analyzer.errors}")
            failed += 1
            continue

        warnings = analyzer.uninitialized_warnings
        actual_count = len(warnings)
        actual_vars = sorted(set(w.variable for w in warnings))
        expected_vars_sorted = sorted(expected_vars)

        if actual_count == expected_count and actual_vars == expected_vars_sorted:
            print(f"  ✓ PASS: Found {actual_count} warning(s) for variables: {actual_vars if actual_vars else 'none'}")
            for w in warnings:
                print(f"    Line {w.line}: {w.variable} used in {w.context}")
            passed += 1
        else:
            print(f"  ✗ FAIL: Expected {expected_count} warning(s) for {expected_vars_sorted}")
            print(f"          Got {actual_count} warning(s) for {actual_vars}")
            for w in warnings:
                print(f"    Line {w.line}: {w.variable} used in {w.context}")
            failed += 1

    except Exception as e:
        print(f"  ✗ FAIL: Exception: {e}")
        import traceback
        traceback.print_exc()
        failed += 1

print("\n" + "=" * 70)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 70)

if failed > 0:
    sys.exit(1)
