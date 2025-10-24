#!/usr/bin/env python3
"""
Test Integer Size Inference (8/16/32-bit optimization)

Demonstrates automatic detection of optimal integer sizes for massive
performance improvements on 8-bit CPUs like the Intel 8080.
"""

import sys
sys.path.insert(0, 'src')

from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer


def test_integer_sizes(source, title):
    """Test integer size inference"""
    print(f"\n{'='*70}")
    print(f"{title}")
    print(f"{'='*70}")
    print("\nProgram:")
    print(source)
    print()

    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        program = parser.parse()

        analyzer = SemanticAnalyzer()
        analyzer.analyze(program)

        # Extract integer size section from report
        report = analyzer.get_report()
        lines = report.split('\n')

        in_section = False
        for line in lines:
            if 'Integer Size Inference' in line:
                in_section = True
            if in_section:
                print(line)
                if line.startswith('Warnings') or line.startswith('Errors'):
                    break

        if not analyzer.integer_ranges:
            print("Integer Size Inference (8/16/32-bit optimization):")
            print("  No optimizable integer sizes detected")

    except Exception as e:
        print(f'Error: {e}')
        import traceback
        traceback.print_exc()


# =================================================================
# Example 1: Small FOR loop (8-bit unsigned)
# =================================================================
example1 = """100 FOR I = 1 TO 10
110   PRINT I
120 NEXT I
"""

test_integer_sizes(example1, "Example 1: Small FOR Loop (8-bit unsigned)")


# =================================================================
# Example 2: String processing loop (8-bit unsigned - LEN)
# =================================================================
example2 = """100 INPUT A$
110 FOR I = 1 TO LEN(A$)
120   C = ASC(MID$(A$, I, 1))
130   PRINT CHR$(C)
140 NEXT I
"""

test_integer_sizes(example2, "Example 2: String Processing (8-bit unsigned)")


# =================================================================
# Example 3: Character codes (8-bit unsigned - ASC)
# =================================================================
example3 = """100 C = ASC("A")
110 PRINT C
"""

test_integer_sizes(example3, "Example 3: Character Code (8-bit unsigned)")


# =================================================================
# Example 4: Large loop (8-bit unsigned, max 255)
# =================================================================
example4 = """100 FOR I = 0 TO 255
110   PRINT I
120 NEXT I
"""

test_integer_sizes(example4, "Example 4: Loop to 255 (8-bit unsigned)")


# =================================================================
# Example 5: Medium loop (16-bit unsigned)
# =================================================================
example5 = """100 FOR I = 1 TO 1000
110   PRINT I
120 NEXT I
"""

test_integer_sizes(example5, "Example 5: Loop to 1000 (16-bit unsigned)")


# =================================================================
# Example 6: Signed 8-bit range
# =================================================================
example6 = """100 FOR I = -50 TO 50
110   PRINT I
120 NEXT I
"""

test_integer_sizes(example6, "Example 6: Signed Range (8-bit signed)")


# =================================================================
# Example 7: String position (8-bit unsigned - INSTR)
# =================================================================
example7 = """100 P = INSTR(A$, "HELLO")
110 IF P > 0 THEN PRINT "Found at"; P
"""

test_integer_sizes(example7, "Example 7: String Position (8-bit unsigned)")


# =================================================================
# Example 8: Memory peek (8-bit unsigned)
# =================================================================
example8 = """100 B = PEEK(1000)
110 PRINT B
"""

test_integer_sizes(example8, "Example 8: Memory Peek (8-bit unsigned)")


# =================================================================
# Example 9: Character frequency counter (realistic example)
# =================================================================
example9 = """100 DIM FREQ(255)
110 FOR I = 0 TO 255
120   FREQ(I) = 0
130 NEXT I
140 INPUT A$
150 FOR I = 1 TO LEN(A$)
160   C = ASC(MID$(A$, I, 1))
170   FREQ(C) = FREQ(C) + 1
180 NEXT I
"""

test_integer_sizes(example9, "Example 9: Character Frequency Counter (Real-world)")


# =================================================================
# Example 10: Mixed sizes
# =================================================================
example10 = """100 FOR I = 1 TO 100
110   FOR J = 1 TO 10
120     FOR K = 1 TO 1000
130       PRINT I; J; K
140     NEXT K
150   NEXT J
160 NEXT I
"""

test_integer_sizes(example10, "Example 10: Nested Loops with Mixed Sizes")


print(f"\n{'='*70}")
print("INTEGER SIZE INFERENCE TESTS COMPLETE")
print(f"{'='*70}")
print("\nPerformance Impact on Intel 8080:")
print("  8-bit operations:  ~5-10 cycles")
print("  16-bit operations: ~10-20 cycles")
print("  32-bit operations: ~80-100+ cycles")
print("\n  Speedup: 10-20x for 8-bit vs 32-bit!")
print(f"{'='*70}\n")
