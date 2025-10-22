#!/usr/bin/env python3
"""
Run all tests in tests_with_results/ directory and verify they parse correctly.
This script verifies the test PROGRAMS parse - it does NOT execute them.
To actually run the tests and check output, you need a MBASIC interpreter.
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lexer import tokenize
from parser import Parser


def main():
    """Test all .bas files in tests_with_results/"""

    test_dir = Path('basic/tests_with_results')
    if not test_dir.exists():
        print(f"Error: {test_dir} directory not found")
        return 1

    bas_files = sorted(test_dir.glob('*.bas'))

    if not bas_files:
        print(f"No test files found in {test_dir}")
        return 1

    print("=" * 70)
    print(f"Testing {len(bas_files)} test program(s)")
    print("=" * 70)
    print()

    success = []
    fail = []

    for filepath in bas_files:
        try:
            with open(filepath, 'r') as f:
                content = f.read()

            tokens = list(tokenize(content))
            parser = Parser(tokens)
            ast = parser.parse()

            success.append(filepath.name)
            print(f"✓ {filepath.name:40} parses successfully")

            # Check if corresponding .txt file exists
            txt_file = filepath.with_suffix('.txt')
            if txt_file.exists():
                print(f"  → Expected output: {txt_file.name}")
            else:
                print(f"  ⚠ Missing expected output file: {txt_file.name}")

        except Exception as e:
            fail.append((filepath.name, str(e)))
            print(f"✗ {filepath.name:40} FAILED")
            print(f"  Error: {str(e)[:100]}")

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Tests parsing:  {len(success)}/{len(bas_files)}")
    print(f"Tests failing:  {len(fail)}/{len(bas_files)}")

    if len(success) == len(bas_files):
        print()
        print("✓ All test programs parse successfully!")
        print()
        print("To actually RUN these tests and verify output:")
        print("  1. Compile or interpret each .bas file")
        print("  2. Compare output with corresponding .txt file")
        return 0
    else:
        print()
        print("✗ Some test programs failed to parse")
        return 1


if __name__ == '__main__':
    sys.exit(main())
