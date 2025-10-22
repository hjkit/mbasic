#!/usr/bin/env python3
"""
Analyze token usage across all successfully parsing BASIC files.

This script:
1. Reads all .bas files from bas_tests1/ and tests_with_results/
2. Tokenizes each file that parses successfully
3. Counts how many times each token type is used
4. Identifies unused tokens
5. Prints a sorted report of token usage
"""

import sys
from pathlib import Path
from collections import Counter

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lexer import tokenize
from parser import Parser
from tokens import TokenType


def analyze_file(filepath):
    """
    Tokenize and parse a file, return token counts or None if it fails.

    Returns:
        Counter of token types, or None if parsing fails
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Tokenize
        tokens = list(tokenize(content))

        # Verify it parses (we only count tokens from parseable files)
        parser = Parser(tokens)
        ast = parser.parse()

        # Count token types
        token_counts = Counter(tok.type for tok in tokens)
        return token_counts

    except Exception:
        return None


def main():
    """Analyze token usage across all test files"""

    # Find all .bas files in test directories
    test_dirs = [
        Path('basic/bas_tests1'),
        Path('basic/tests_with_results')
    ]

    bas_files = []
    for test_dir in test_dirs:
        if test_dir.exists():
            bas_files.extend(sorted(test_dir.glob('*.bas')))

    if not bas_files:
        print("Error: No .bas files found")
        return 1

    print("=" * 70)
    print("Token Usage Analysis")
    print("=" * 70)
    print()
    print(f"Analyzing {len(bas_files)} BASIC files...")
    print()

    # Collect token counts from all successfully parsing files
    total_counts = Counter()
    success_count = 0
    fail_count = 0

    for filepath in bas_files:
        file_counts = analyze_file(filepath)
        if file_counts is not None:
            total_counts.update(file_counts)
            success_count += 1
        else:
            fail_count += 1

    print(f"Successfully analyzed: {success_count}/{len(bas_files)} files")
    if fail_count > 0:
        print(f"Failed to parse: {fail_count} files")
    print()

    # Get all token types from TokenType enum
    all_token_types = set(TokenType)
    used_tokens = set(total_counts.keys())
    unused_tokens = all_token_types - used_tokens

    # Print unused tokens
    print("=" * 70)
    print(f"UNUSED TOKENS ({len(unused_tokens)} tokens never used)")
    print("=" * 70)
    print()

    if unused_tokens:
        for token_type in sorted(unused_tokens, key=lambda t: t.name):
            print(f"  {token_type.name}")
    else:
        print("  (All tokens are used!)")

    print()

    # Print used tokens sorted by frequency
    print("=" * 70)
    print(f"TOKEN USAGE BY FREQUENCY ({len(used_tokens)} tokens used)")
    print("=" * 70)
    print()

    # Sort by count (descending)
    sorted_tokens = sorted(total_counts.items(), key=lambda x: (-x[1], x[0].name))

    # Calculate total
    total_token_count = sum(total_counts.values())

    print(f"{'Token Type':<30} {'Count':>10} {'Percent':>8}")
    print("-" * 70)

    for token_type, count in sorted_tokens:
        percent = 100 * count / total_token_count
        print(f"{token_type.name:<30} {count:>10,} {percent:>7.2f}%")

    print("-" * 70)
    print(f"{'TOTAL':<30} {total_token_count:>10,} {100.0:>7.2f}%")

    print()

    # Print summary statistics
    print("=" * 70)
    print("SUMMARY STATISTICS")
    print("=" * 70)
    print()
    print(f"Total tokens processed:  {total_token_count:,}")
    print(f"Unique token types used: {len(used_tokens)}/{len(all_token_types)}")
    print(f"Token types unused:      {len(unused_tokens)}/{len(all_token_types)}")
    print(f"Coverage:                {100*len(used_tokens)/len(all_token_types):.1f}%")
    print()

    # Show top 10 most used tokens
    print("Top 10 Most Used Tokens:")
    for i, (token_type, count) in enumerate(sorted_tokens[:10], 1):
        print(f"  {i:2}. {token_type.name:<25} {count:>10,} times")

    print()

    # Show 10 least used tokens (that are used)
    if len(sorted_tokens) > 10:
        print("10 Least Used Tokens (that are used):")
        for i, (token_type, count) in enumerate(reversed(sorted_tokens[-10:]), 1):
            print(f"  {i:2}. {token_type.name:<25} {count:>10,} times")

    print()
    print("=" * 70)

    return 0


if __name__ == '__main__':
    sys.exit(main())
