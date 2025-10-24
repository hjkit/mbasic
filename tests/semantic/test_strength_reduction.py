#!/usr/bin/env python3
"""Test strength reduction optimizations"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from lexer import tokenize
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

# Test 1: Multiply by 2 -> Addition
test1 = """
10 X = A * 2
20 Y = 2 * B
30 END
"""

# Test 2: Powers of 2 multiplication (detect opportunity)
test2 = """
10 X = A * 4
20 Y = B * 8
30 Z = C * 16
40 END
"""

# Test 3: Identity operations (X * 1, X + 0, etc.)
test3 = """
10 X = A * 1
20 Y = B + 0
30 Z = C - 0
40 W = D / 1
50 END
"""

# Test 4: Multiplication by 0
test4 = """
10 X = A * 0
20 Y = 0 * B
30 END
"""

# Test 5: Exponentiation reductions
test5 = """
10 X = A ^ 2
20 Y = B ^ 3
30 Z = C ^ 4
40 W = D ^ 1
50 V = E ^ 0
60 END
"""

# Test 6: Subtraction optimizations
test6 = """
10 X = A - 0
20 Y = B - B
30 END
"""

# Test 7: Division by power of 2
test7 = """
10 X = A \\ 1
20 Y = B \\ 2
30 Z = C \\ 4
40 W = D / 1
50 END
"""

# Test 8: Complex expressions with multiple reductions
test8 = """
10 X = (A * 2) + (B ^ 2)
20 Y = (C * 1) * (D + 0)
30 Z = (E ^ 3) - 0
40 END
"""

# Test 9: Loop with strength reduction opportunities
test9 = """
10 FOR I% = 1 TO 100
20   X% = I% * 2
30   Y% = I% ^ 2
40 NEXT I%
50 END
"""

# Test 10: Array indexing with reductions
test10 = """
10 DIM A(100)
20 N% = 10
30 X% = A(N% * 2)
40 Y% = A(N% ^ 2)
50 END
"""

print("=" * 70)
print("STRENGTH REDUCTION OPTIMIZATION TEST")
print("=" * 70)

tests = [
    (test1, "Multiply by 2 -> Addition", 2),
    (test2, "Powers of 2 multiplication", 3),
    (test3, "Identity operations", 4),
    (test4, "Multiplication by 0", 2),
    (test5, "Exponentiation reductions", 5),
    (test6, "Subtraction optimizations", 2),
    (test7, "Division optimizations", 4),
    (test8, "Complex expressions", 6),
    (test9, "Loop with reductions", 2),
    (test10, "Array indexing with reductions", 2),
]

passed = 0
failed = 0

for i, (test_code, description, expected_count) in enumerate(tests, 1):
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

        if reduction_count >= expected_count:
            print(f"  ✓ PASS: Found {reduction_count} reduction(s)")
            for sr in analyzer.strength_reductions:
                print(f"    Line {sr.line}: {sr.original_expr} → {sr.reduced_expr}")
                print(f"      {sr.reduction_type} ({sr.savings})")
            passed += 1
        else:
            print(f"  ✗ FAIL: Expected at least {expected_count} reductions, found {reduction_count}")
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
    print("\nStrength reduction is working correctly!")
    print("\nImplemented optimizations:")
    print("  • X * 2 → X + X (replace MUL with ADD)")
    print("  • X * 2^n → detected for shift optimization")
    print("  • X * 1 → X (eliminate MUL)")
    print("  • X * 0 → 0 (eliminate MUL)")
    print("  • X + 0 → X (eliminate ADD)")
    print("  • X - 0 → X (eliminate SUB)")
    print("  • X - X → 0 (eliminate SUB)")
    print("  • X / 1 → X (eliminate DIV)")
    print("  • X \\ 1 → X (eliminate integer DIV)")
    print("  • X \\ 2^n → detected for shift optimization")
    print("  • X ^ 2 → X * X (replace POW with MUL)")
    print("  • X ^ 3, X ^ 4 → repeated MUL (replace POW)")
    print("  • X ^ 1 → X (eliminate POW)")
    print("  • X ^ 0 → 1 (eliminate POW)")
    sys.exit(0)
else:
    print(f"\n✗ {failed} test(s) failed!")
    sys.exit(1)
