#!/usr/bin/env python3
"""Test algebraic simplification optimizations"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from lexer import tokenize
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

# Test 1: Boolean AND optimizations
test1 = """
10 X = A AND 0
20 Y = B AND -1
30 Z = C AND C
40 END
"""

# Test 2: Boolean OR optimizations
test2 = """
10 X = A OR -1
20 Y = B OR 0
30 Z = C OR C
40 END
"""

# Test 3: Boolean XOR optimizations
test3 = """
10 X = A XOR 0
20 Y = B XOR B
30 END
"""

# Test 4: NOT optimizations
test4 = """
10 X = NOT(NOT A)
20 Y = NOT 0
30 Z = NOT -1
40 END
"""

# Test 5: Double negation
test5 = """
10 X = -(-A)
20 Y = -(0)
30 END
"""

# Test 6: Mixed Boolean operations
test6 = """
10 X = (A AND -1) OR 0
20 Y = (B OR -1) AND (C XOR 0)
30 END
"""

# Test 7: Complex Boolean expressions
test7 = """
10 IF A AND 0 THEN PRINT "Never"
20 IF B OR -1 THEN PRINT "Always"
30 END
"""

# Test 8: Boolean with variables
test8 = """
10 FLAG = -1
20 X = A AND FLAG
30 Y = B OR (NOT FLAG)
40 END
"""

# Test 9: Nested NOT
test9 = """
10 X = NOT(NOT(NOT A))
20 END
"""

# Test 10: All Boolean identities
test10 = """
10 A1 = X AND 0
20 A2 = X AND -1
30 O1 = X OR 0
40 O2 = X OR -1
50 X1 = X XOR 0
60 N1 = NOT 0
70 N2 = NOT -1
80 END
"""

print("=" * 70)
print("ALGEBRAIC SIMPLIFICATION TEST")
print("=" * 70)

tests = [
    (test1, "AND optimizations", 3),
    (test2, "OR optimizations", 3),
    (test3, "XOR optimizations", 2),
    (test4, "NOT optimizations", 3),
    (test5, "Double negation", 2),
    (test6, "Mixed Boolean operations", 4),
    (test7, "Boolean in conditionals", 2),
    (test8, "Boolean with variables", 0),  # FLAG is a variable, not constant
    (test9, "Nested NOT", 2),  # NOT(NOT(NOT A)) -> NOT A (2 reductions)
    (test10, "All Boolean identities", 7),
]

passed = 0
failed = 0

for i, (test_code, description, expected_min) in enumerate(tests, 1):
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

        reduction_count = len(analyzer.strength_reductions)

        if reduction_count >= expected_min:
            print(f"  ✓ PASS: Found {reduction_count} reduction(s)")
            for sr in analyzer.strength_reductions:
                print(f"    Line {sr.line}: {sr.original_expr} → {sr.reduced_expr}")
                print(f"      {sr.reduction_type} ({sr.savings})")
            passed += 1
        else:
            print(f"  ✗ FAIL: Expected at least {expected_min} reductions, found {reduction_count}")
            for sr in analyzer.strength_reductions:
                print(f"    Line {sr.line}: {sr.original_expr} → {sr.reduced_expr}")
            failed += 1

    except Exception as e:
        print(f"  ✗ FAIL: Exception: {e}")
        import traceback
        traceback.print_exc()
        failed += 1

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Passed: {passed}/{len(tests)}")
print(f"Failed: {failed}/{len(tests)}")

if failed == 0:
    print("\n✓ All tests passed!")
    print("\nAlgebraic simplification is working correctly!")
    print("\nImplemented optimizations:")
    print("\nBoolean AND:")
    print("  • X AND 0 → 0 (FALSE)")
    print("  • X AND -1 → X (TRUE)")
    print("  • X AND X → X")
    print("\nBoolean OR:")
    print("  • X OR -1 → -1 (TRUE)")
    print("  • X OR 0 → X (FALSE)")
    print("  • X OR X → X")
    print("\nBoolean XOR:")
    print("  • X XOR 0 → X")
    print("  • X XOR X → 0")
    print("\nBoolean NOT:")
    print("  • NOT(NOT X) → X (double negation)")
    print("  • NOT 0 → -1 (NOT FALSE)")
    print("  • NOT -1 → 0 (NOT TRUE)")
    print("\nNegation:")
    print("  • -(-X) → X (double negation)")
    print("  • -(0) → 0")
    print("\nPlus strength reduction from earlier:")
    print("  • X * 1 → X, X * 0 → 0")
    print("  • X + 0 → X, X - 0 → X")
    print("  • X - X → 0, X / 1 → X")
    sys.exit(0)
else:
    print(f"\n✗ {failed} test(s) failed!")
    sys.exit(1)
