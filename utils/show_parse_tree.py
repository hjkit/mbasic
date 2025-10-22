#!/usr/bin/env python3
"""
Display the parse tree (AST) produced by the parser.

This script takes a BASIC program and shows the hierarchical structure
of the Abstract Syntax Tree that the parser produces.
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lexer import tokenize
from parser import Parser


def show_node(node, indent=0, name=""):
    """
    Recursively display a parse tree node with indentation.

    Args:
        node: The AST node to display
        indent: Current indentation level
        name: Name/label for this node (e.g., "condition", "left")
    """
    prefix = "  " * indent

    # Get the node's class name
    node_type = type(node).__name__

    # Format the display name
    if name:
        display = f"{prefix}{name}: {node_type}"
    else:
        display = f"{prefix}{node_type}"

    # Add key information for certain node types
    if hasattr(node, 'name') and isinstance(node.name, str):
        display += f" (name='{node.name}')"
    elif hasattr(node, 'value'):
        if isinstance(node.value, str):
            display += f" (value='{node.value}')"
        elif isinstance(node.value, (int, float)):
            display += f" (value={node.value})"
    elif hasattr(node, 'operator'):
        display += f" (op={node.operator.name})"
    elif hasattr(node, 'line_number') and node_type in ['LineNode', 'GotoStatementNode', 'GosubStatementNode']:
        display += f" (line={node.line_number})"

    print(display)

    # Recursively show child nodes
    if hasattr(node, '__dict__'):
        for key, value in node.__dict__.items():
            # Skip metadata, type info, and problematic types
            if key in ['line_num', 'column', 'type_suffix', 'literal', 'operator']:
                continue

            # Skip enum types, primitives, and None
            if value is None or isinstance(value, (int, float, str, bool)):
                continue

            # Skip dict (like def_type_statements)
            if isinstance(value, dict):
                continue

            # Handle lists of nodes
            if isinstance(value, list) and value:
                # Only process if list contains AST nodes
                for i, item in enumerate(value):
                    if hasattr(item, '__dict__') and not isinstance(item, (str, int, float, bool)):
                        show_node(item, indent + 1, f"{key}[{i}]")
            # Handle single nodes
            elif hasattr(value, '__dict__') and not isinstance(value, (str, int, float, bool)):
                # Skip enum types
                if 'Enum' not in str(type(value).__bases__):
                    show_node(value, indent + 1, key)


def main():
    """Parse a BASIC program and display its parse tree"""

    if len(sys.argv) > 1:
        # Read from file
        filepath = Path(sys.argv[1])
        if not filepath.exists():
            print(f"Error: File not found: {filepath}")
            return 1

        with open(filepath, 'r') as f:
            code = f.read()

        print(f"Parse tree for: {filepath}")
    else:
        # Use example program
        code = '''10 REM Example program
20 X = 5 + 3
30 IF X > 5 THEN PRINT "Big" ELSE PRINT "Small"
40 FOR I = 1 TO 10
50   PRINT I
60 NEXT I
70 END
'''
        print("Parse tree for example program:")

    print("=" * 70)
    print()

    # Parse the code
    try:
        tokens = list(tokenize(code))
        parser = Parser(tokens)
        ast = parser.parse()

        # Show the parse tree
        show_node(ast, name="Program")

        print()
        print("=" * 70)
        print(f"Successfully parsed into AST with {len(ast.lines)} lines")

        # Count statement types
        from collections import Counter
        stmt_types = []
        for line in ast.lines:
            for stmt in line.statements:
                stmt_types.append(type(stmt).__name__)

        if stmt_types:
            print()
            print("Statement types in program:")
            for stmt_type, count in Counter(stmt_types).most_common():
                print(f"  {stmt_type}: {count}")

        return 0

    except Exception as e:
        print(f"Error parsing program: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
