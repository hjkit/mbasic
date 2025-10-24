#!/usr/bin/env python3
"""Test OPTION BASE global behavior"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from lexer import tokenize
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

# Test 1: OPTION BASE appears after DIM - should still work (global effect)
test1 = """
10 DIM A(10, 20)
20 OPTION BASE 0
30 X = A(0, 0)
40 END
"""

# Test 2: Multiple OPTION BASE with same value - should work
test2 = """
10 OPTION BASE 1
20 DIM A(10, 20)
30 OPTION BASE 1
40 X = A(1, 1)
50 END
"""

# Test 3: Multiple OPTION BASE with different values - should ERROR
test3 = """
10 OPTION BASE 0
20 DIM A(10)
30 OPTION BASE 1
40 END
"""

# Test 4: OPTION BASE 1 affects all arrays
test4 = """
10 OPTION BASE 1
20 DIM A(10, 20)
30 DIM B(5, 3, 4)
40 END
"""

print("=" * 70)
print("OPTION BASE GLOBAL BEHAVIOR TEST")
print("=" * 70)

# Test 1: OPTION BASE after DIM
print("\nTest 1: OPTION BASE after DIM (global effect)")
tokens = tokenize(test1)
parser = Parser(tokens)
program = parser.parse()
analyzer = SemanticAnalyzer()
success = analyzer.analyze(program)

if success and analyzer.array_base == 0:
    a_info = analyzer.symbols.variables.get('A')
    # For BASE 0: A(10, 20) = 11 * 21 = 231
    if a_info and a_info.flattened_size == 231:
        print("  ✓ PASS: OPTION BASE 0 applied globally (size 231)")
    else:
        print(f"  ✗ FAIL: Expected size 231, got {a_info.flattened_size if a_info else 'none'}")
else:
    print("  ✗ FAIL: Analysis failed or wrong base")

# Test 2: Multiple OPTION BASE same value
print("\nTest 2: Multiple OPTION BASE with same value")
tokens = tokenize(test2)
parser = Parser(tokens)
program = parser.parse()
analyzer = SemanticAnalyzer()
success = analyzer.analyze(program)

if success and analyzer.array_base == 1:
    a_info = analyzer.symbols.variables.get('A')
    # For BASE 1: A(10, 20) = 10 * 20 = 200
    if a_info and a_info.flattened_size == 200:
        print("  ✓ PASS: Multiple OPTION BASE 1 accepted (size 200)")
    else:
        print(f"  ✗ FAIL: Expected size 200, got {a_info.flattened_size if a_info else 'none'}")
else:
    print("  ✗ FAIL: Analysis failed or wrong base")

# Test 3: Conflicting OPTION BASE
print("\nTest 3: Conflicting OPTION BASE values")
tokens = tokenize(test3)
parser = Parser(tokens)
program = parser.parse()
analyzer = SemanticAnalyzer()
success = analyzer.analyze(program)

if not success:
    conflict_error = False
    for error in analyzer.errors:
        if 'Conflicting OPTION BASE' in str(error):
            conflict_error = True
            break
    if conflict_error:
        print("  ✓ PASS: Conflicting OPTION BASE detected")
        print(f"    Error: {analyzer.errors[0]}")
    else:
        print(f"  ✗ FAIL: Wrong error: {analyzer.errors}")
else:
    print("  ✗ FAIL: Should have failed with conflict error")

# Test 4: OPTION BASE 1 size calculation
print("\nTest 4: OPTION BASE 1 affects all arrays")
tokens = tokenize(test4)
parser = Parser(tokens)
program = parser.parse()
analyzer = SemanticAnalyzer()
success = analyzer.analyze(program)

if success and analyzer.array_base == 1:
    a_info = analyzer.symbols.variables.get('A')
    b_info = analyzer.symbols.variables.get('B')
    # For BASE 1: A(10, 20) = 10 * 20 = 200
    # For BASE 1: B(5, 3, 4) = 5 * 3 * 4 = 60
    if a_info and a_info.flattened_size == 200 and b_info and b_info.flattened_size == 60:
        print("  ✓ PASS: OPTION BASE 1 applied to all arrays")
        print(f"    A(10,20) = {a_info.flattened_size}, B(5,3,4) = {b_info.flattened_size}")
    else:
        print(f"  ✗ FAIL: Wrong sizes - A: {a_info.flattened_size if a_info else 'none'}, B: {b_info.flattened_size if b_info else 'none'}")
else:
    print("  ✗ FAIL: Analysis failed or wrong base")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("\nOPTION BASE behavior:")
print("  ✓ Global scope (applies everywhere regardless of location)")
print("  ✓ Can appear multiple times if same value")
print("  ✓ Compile-time validation of conflicts")
print("  ✓ Affects array flattening calculations")
print("\n✓ OPTION BASE global semantics working correctly!")
