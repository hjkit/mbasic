#!/usr/bin/env python3
"""Test multi-dimensional array flattening"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from lexer import tokenize
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

test_program = """
10 REM === Test array flattening ===
20 DIM A(10, 20)
30 DIM B(5, 3, 4)
40 FOR I = 1 TO 10
50   FOR J = 1 TO 20
60     X = A(I, J)
70     Y = A(I, J)
80   NEXT J
90 NEXT I
100 PRINT "A(I,J) should be flattened and detected as CSE"

200 REM === Test 3D array ===
210 FOR P = 1 TO 5
220   FOR Q = 1 TO 3
230     FOR R = 1 TO 4
240       Z1 = B(P, Q, R)
250       Z2 = B(P, Q, R)
260     NEXT R
270   NEXT Q
280 NEXT P
290 PRINT "B(P,Q,R) should be flattened and detected as CSE"

300 END
"""

print("=" * 70)
print("ARRAY FLATTENING TEST")
print("=" * 70)

print("\nParsing test program...")
tokens = tokenize(test_program)
parser = Parser(tokens)
program = parser.parse()

print("Performing semantic analysis with array flattening...")
analyzer = SemanticAnalyzer()
success = analyzer.analyze(program)

if not success:
    print("\n✗ Analysis failed!")
    for error in analyzer.errors:
        print(f"  {error}")
    sys.exit(1)

print("\n" + "=" * 70)
print("RESULTS")
print("=" * 70)

# Check array declarations
print("\nArray Declarations:")
for var_name, var_info in sorted(analyzer.symbols.variables.items()):
    if var_info.is_array:
        print(f"  {var_name}:")
        print(f"    Original dimensions: {var_info.dimensions}")
        print(f"    Flattened size: {var_info.flattened_size}")

# Check for CSEs in flattened array accesses
print(f"\nCommon Subexpressions: {len(analyzer.common_subexpressions)}")
for cse in sorted(analyzer.common_subexpressions.values(), key=lambda x: x.first_line):
    print(f"\n  {cse.expression_desc}")
    print(f"    Lines: {cse.first_line}, {', '.join(map(str, cse.occurrences))}")
    print(f"    Variables used: {', '.join(sorted(cse.variables_used))}")

# Validation
print("\n" + "=" * 70)
print("VALIDATION")
print("=" * 70)

errors = []

# Test 1: Array A should be flattened
a_info = analyzer.symbols.variables.get('A')
if a_info:
    expected_size = 11 * 21  # (10+1) * (20+1) for BASE 0
    if a_info.flattened_size == expected_size:
        print(f"✓ Test 1 PASS: A(10,20) flattened to size {expected_size}")
    else:
        print(f"✗ Test 1 FAIL: Expected size {expected_size}, got {a_info.flattened_size}")
        errors.append("Test 1")
else:
    print("✗ Test 1 FAIL: Array A not found")
    errors.append("Test 1")

# Test 2: Array B should be flattened
b_info = analyzer.symbols.variables.get('B')
if b_info:
    expected_size = 6 * 4 * 5  # (5+1) * (3+1) * (4+1) for BASE 0
    if b_info.flattened_size == expected_size:
        print(f"✓ Test 2 PASS: B(5,3,4) flattened to size {expected_size}")
    else:
        print(f"✗ Test 2 FAIL: Expected size {expected_size}, got {b_info.flattened_size}")
        errors.append("Test 2")
else:
    print("✗ Test 2 FAIL: Array B not found")
    errors.append("Test 2")

# Test 3: Flattened array accesses should be detected as CSE
cse_found = False
for cse in analyzer.common_subexpressions.values():
    # Variables are stored in uppercase
    if 'a' in cse.expression_desc.lower() and 'I' in cse.variables_used and 'J' in cse.variables_used:
        cse_found = True
        print(f"✓ Test 3 PASS: Flattened A(I,J) detected as CSE")
        break

if not cse_found:
    print("✗ Test 3 FAIL: Flattened A(I,J) not detected as CSE")
    errors.append("Test 3")

# Test 4: 3D array accesses should also be CSE
cse_3d_found = False
for cse in analyzer.common_subexpressions.values():
    if 'b' in cse.expression_desc.lower() and 'P' in cse.variables_used:
        cse_3d_found = True
        print(f"✓ Test 4 PASS: Flattened B(P,Q,R) detected as CSE")
        break

if not cse_3d_found:
    print("✗ Test 4 FAIL: Flattened B(P,Q,R) not detected as CSE")
    errors.append("Test 4")

if errors:
    print(f"\n✗ {len(errors)} test(s) failed: {', '.join(errors)}")
    sys.exit(1)
else:
    print("\n✓ All tests passed!")
    print("\nArray flattening is working! Multi-dimensional array accesses")
    print("are transformed into flattened indices, allowing CSE detection")
    print("on the index calculations.")
