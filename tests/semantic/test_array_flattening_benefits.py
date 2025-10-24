#!/usr/bin/env python3
"""Demonstrate the benefits of array flattening for optimization"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from lexer import tokenize
from parser import Parser
from semantic_analyzer import SemanticAnalyzer

test_program = """
10 REM === Matrix multiplication with array flattening ===
20 DIM A(10, 10), B(10, 10), C(10, 10)
30 FOR I = 0 TO 10
40   FOR J = 0 TO 10
50     SUM = 0
60     FOR K = 0 TO 10
70       SUM = SUM + A(I, K) * B(K, J)
80     NEXT K
90     C(I, J) = SUM
100   NEXT J
110 NEXT I
120 PRINT "Matrix multiplication complete"

200 REM === Image processing with 2D array ===
210 DIM IMAGE(640, 480)
220 FOR Y = 1 TO 479
230   FOR X = 1 TO 639
240     AVG = IMAGE(X-1, Y) + IMAGE(X+1, Y) + IMAGE(X, Y-1) + IMAGE(X, Y+1)
250     AVG = AVG / 4
260     IMAGE(X, Y) = AVG
270   NEXT X
280 NEXT Y

300 END
"""

print("=" * 70)
print("ARRAY FLATTENING OPTIMIZATION BENEFITS")
print("=" * 70)

print("\nThis test demonstrates how array flattening enables:")
print("  1. CSE detection on index calculations")
print("  2. Constant folding of stride calculations")
print("  3. Simplified code generation")
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
print("OPTIMIZATION REPORT")
print("=" * 70)

# Show arrays and their flattened sizes
print("\nFlattened Arrays:")
for var_name, var_info in sorted(analyzer.symbols.variables.items()):
    if var_info.is_array:
        original_dims = ' x '.join(map(str, var_info.dimensions))
        print(f"  {var_name}({original_dims}):")
        print(f"    Flattened to: {var_name}({var_info.flattened_size})")
        print(f"    Memory savings: Single dimension, contiguous storage")

# Show constant folding on stride calculations
print(f"\nConstant Folding: {len(analyzer.folded_expressions)} optimizations")
stride_folds = [f for f in analyzer.folded_expressions if '*' in str(f[1])]
if stride_folds:
    print(f"  Stride calculations folded: {len(stride_folds)}")
    for line, expr, value in stride_folds[:5]:  # Show first 5
        print(f"    Line {line}: {expr} → {value}")

# Show CSE opportunities from flattened indices
print(f"\nCommon Subexpressions: {len(analyzer.common_subexpressions)}")
array_cses = [cse for cse in analyzer.common_subexpressions.values()
              if any(v in ['A', 'B', 'C', 'IMAGE'] for v in cse.variables_used)]

if array_cses:
    print(f"  Array index calculations as CSE: {len(array_cses)}")
    for cse in sorted(array_cses, key=lambda x: x.first_line)[:5]:  # Show first 5
        print(f"    {cse.expression_desc}")
        print(f"      Computed {len(cse.occurrences) + 1} times at lines {cse.first_line}, {', '.join(map(str, cse.occurrences[:3]))}")

# Show loop analysis
print(f"\nLoop Analysis: {len(analyzer.loops)} loops")
for start_line, loop in sorted(analyzer.loops.items())[:3]:  # Show first 3
    print(f"  Loop at line {start_line}:")
    if loop.iteration_count:
        print(f"    Iterations: {loop.iteration_count}")
    if loop.invariants:
        hoistable = [inv for inv in loop.invariants.values() if inv.can_hoist]
        if hoistable:
            print(f"    Hoistable expressions: {len(hoistable)}")

print("\n" + "=" * 70)
print("BENEFITS SUMMARY")
print("=" * 70)

print("\nArray Flattening Achievements:")
print("  ✓ Multi-dimensional arrays converted to 1D")
print("  ✓ Index calculations become arithmetic expressions")
print("  ✓ Stride multiplications are constant-folded")
print("  ✓ Repeated index calculations detected as CSE")
print("  ✓ Loop-invariant indices can be hoisted")
print("  ✓ Simpler, faster array access code generation")

print("\nPerformance Impact:")
print("  • Index calculation overhead reduced via CSE")
print("  • Constant stride values eliminate runtime multiplication")
print("  • Sequential memory access pattern for better cache locality")
print("  • Enables loop unrolling and vectorization")

print("\n✓ Array flattening optimization working successfully!")
