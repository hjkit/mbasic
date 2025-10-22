"""
MBASIC 5.21 Interactive Command Mode

Implements the interactive REPL with:
- Line entry and editing
- Direct commands (RUN, LIST, SAVE, LOAD, NEW, etc.)
- Immediate mode execution
"""

import sys
import re
from pathlib import Path
from lexer import tokenize
from parser import Parser
from runtime import Runtime
from interpreter import Interpreter
import ast_nodes


class InteractiveMode:
    """MBASIC 5.21 interactive command mode"""

    def __init__(self):
        self.lines = {}  # line_number -> line_text
        self.current_file = None
        self.runtime = None  # Persistent runtime for immediate mode
        self.interpreter = None  # Persistent interpreter
        self.program_runtime = None  # Runtime for RUN (preserved for CONT)
        self.program_interpreter = None  # Interpreter for RUN (preserved for CONT)

    def start(self):
        """Start interactive mode"""
        print("MBASIC 5.21 Interpreter")
        print("Ready")
        print()

        while True:
            try:
                # Read input
                line = input()

                # Process line
                if not line.strip():
                    continue

                self.process_line(line)

            except EOFError:
                # Ctrl+D to exit
                print()
                break
            except KeyboardInterrupt:
                # Ctrl+C
                print()
                print("Break")
                continue
            except Exception as e:
                print(f"?{type(e).__name__}: {e}")

    def process_line(self, line):
        """Process a line of input (numbered line or direct command)"""
        line = line.strip()

        # Check if it's a numbered line
        match = re.match(r'^(\d+)\s*(.*)', line)
        if match:
            line_num = int(match.group(1))
            rest = match.group(2)

            if not rest:
                # Delete line
                if line_num in self.lines:
                    del self.lines[line_num]
            else:
                # Add/replace line
                self.lines[line_num] = line
        else:
            # Direct command
            self.execute_command(line)

    def execute_command(self, cmd):
        """Execute a direct command or immediate mode statement"""
        cmd_stripped = cmd.strip()

        # Parse command and arguments (preserve case for arguments)
        parts = cmd_stripped.split(None, 1)
        command = parts[0].upper() if parts else ""
        args = parts[1] if len(parts) > 1 else ""

        # Meta-commands (editor commands that manipulate program source)
        # Only AUTO is a true meta-command that can't be parsed
        # Everything else (LIST, DELETE, RENUM, FILES, LOAD, SAVE, etc.) goes through parser
        if command == "AUTO":
            self.cmd_auto(args)
        elif command == "":
            pass  # Empty command
        else:
            # Everything else (including LIST, DELETE, RENUM, FILES, RUN, LOAD, SAVE, MERGE, SYSTEM, NEW, PRINT, etc.)
            # goes through the real parser as immediate mode statements
            try:
                self.execute_immediate(cmd)
            except Exception as e:
                print(f"?{type(e).__name__}: {e}")

    def cmd_run(self):
        """RUN - Execute the program"""
        if not self.lines:
            print("?No program")
            return

        try:
            # Build program text
            program_text = self.get_program_text()

            # Parse
            tokens = list(tokenize(program_text))
            parser = Parser(tokens)
            ast = parser.parse()

            # Execute
            runtime = Runtime(ast)
            interpreter = Interpreter(runtime)
            # Pass reference to interactive mode so statements like LIST can access the line editor
            interpreter.interactive_mode = self

            # Save runtime for CONT
            self.program_runtime = runtime
            self.program_interpreter = interpreter

            interpreter.run()

        except Exception as e:
            print(f"?{type(e).__name__}: {e}")

    def cmd_cont(self):
        """CONT - Continue execution after STOP or Break"""
        if not self.program_runtime or not self.program_runtime.stopped:
            print("?Can't continue")
            return

        try:
            # Clear stopped flag
            self.program_runtime.stopped = False

            # Restore execution position
            self.program_runtime.current_line = self.program_runtime.stop_line
            self.program_runtime.current_stmt_index = self.program_runtime.stop_stmt_index
            self.program_runtime.halted = False

            # Resume execution - we need to continue from where we stopped,
            # not restart from the beginning. We'll use run_from_current()
            # which doesn't call setup() and continues from current position.
            self.program_interpreter.run_from_current()

        except Exception as e:
            print(f"?{type(e).__name__}: {e}")

    def cmd_list(self, args):
        """LIST [start][-][end] - List program lines"""
        if not self.lines:
            return

        # Parse range
        start = None
        end = None

        if args:
            # Handle various formats: LIST 100, LIST 100-200, LIST -200, LIST 100-
            if '-' in args:
                parts = args.split('-', 1)
                if parts[0]:
                    start = int(parts[0])
                if parts[1]:
                    end = int(parts[1])
            else:
                # Single line or start
                start = int(args)
                end = start

        # Get sorted line numbers
        line_numbers = sorted(self.lines.keys())

        # Filter by range
        for line_num in line_numbers:
            if start is not None and line_num < start:
                continue
            if end is not None and line_num > end:
                continue

            print(self.lines[line_num])

    def cmd_new(self):
        """NEW - Clear program"""
        self.lines.clear()
        self.current_file = None
        print("Ready")

    def cmd_save(self, filename):
        """SAVE "filename" - Save program to file"""
        if not filename:
            print("?Syntax error")
            return

        # Remove quotes if present
        filename = filename.strip().strip('"').strip("'")

        if not filename:
            print("?Syntax error")
            return

        try:
            # Add .bas extension if not present
            if not filename.endswith('.bas'):
                filename += '.bas'

            program_text = self.get_program_text()

            with open(filename, 'w') as f:
                f.write(program_text)

            self.current_file = filename
            print(f"Saved to {filename}")

        except Exception as e:
            print(f"?{type(e).__name__}: {e}")

    def cmd_load(self, filename):
        """LOAD "filename" - Load program from file"""
        if not filename:
            print("?Syntax error")
            return

        # Remove quotes if present
        filename = filename.strip().strip('"').strip("'")

        if not filename:
            print("?Syntax error")
            return

        try:
            # Add .bas extension if not present
            if not filename.endswith('.bas'):
                filename += '.bas'

            with open(filename, 'r') as f:
                program_text = f.read()

            # Clear current program
            self.lines.clear()

            # Parse and load lines
            for line in program_text.split('\n'):
                line = line.strip()
                if not line:
                    continue

                match = re.match(r'^(\d+)\s', line)
                if match:
                    line_num = int(match.group(1))
                    self.lines[line_num] = line

            self.current_file = filename
            print(f"Loaded from {filename}")
            print("Ready")

        except FileNotFoundError:
            print(f"?File not found: {filename}")
        except Exception as e:
            print(f"?{type(e).__name__}: {e}")

    def cmd_merge(self, filename):
        """MERGE "filename" - Merge program from file into current program

        MERGE adds or replaces lines from a file without clearing existing lines.
        - Lines with matching line numbers are replaced
        - New line numbers are added
        - Existing lines not in the file are kept
        """
        if not filename:
            print("?Syntax error")
            return

        # Remove quotes if present
        filename = filename.strip().strip('"').strip("'")

        if not filename:
            print("?Syntax error")
            return

        try:
            # Add .bas extension if not present
            if not filename.endswith('.bas'):
                filename += '.bas'

            with open(filename, 'r') as f:
                program_text = f.read()

            # Don't clear current program - that's the difference from LOAD
            # Parse and merge lines
            lines_added = 0
            lines_replaced = 0

            for line in program_text.split('\n'):
                line = line.strip()
                if not line:
                    continue

                match = re.match(r'^(\d+)\s', line)
                if match:
                    line_num = int(match.group(1))
                    if line_num in self.lines:
                        lines_replaced += 1
                    else:
                        lines_added += 1
                    self.lines[line_num] = line

            print(f"Merged from {filename}")
            print(f"{lines_added} line(s) added, {lines_replaced} line(s) replaced")
            print("Ready")

        except FileNotFoundError:
            print(f"?File not found: {filename}")
        except Exception as e:
            print(f"?{type(e).__name__}: {e}")

    def cmd_delete(self, args):
        """DELETE start-end - Delete range of lines"""
        if not args or '-' not in args:
            print("?Syntax error")
            return

        try:
            parts = args.split('-', 1)
            start = int(parts[0]) if parts[0] else min(self.lines.keys())
            end = int(parts[1]) if parts[1] else max(self.lines.keys())

            # Delete lines in range
            to_delete = [n for n in self.lines.keys() if start <= n <= end]
            for line_num in to_delete:
                del self.lines[line_num]

        except Exception as e:
            print(f"?Syntax error")

    def cmd_renum(self, args):
        """RENUM [new_start][,increment] - Renumber program lines and update references

        Uses AST-based approach:
        1. Parse program to AST
        2. Build line number mapping (old -> new)
        3. Walk AST and update all line number references
        4. Serialize AST back to source
        """
        new_start = 10
        increment = 10

        if args:
            parts = args.split(',')
            if parts[0]:
                new_start = int(parts[0])
            if len(parts) > 1 and parts[1]:
                increment = int(parts[1])

        try:
            # Parse current program
            program_text = self.get_program_text()
            tokens = list(tokenize(program_text))
            parser = Parser(tokens)
            ast = parser.parse()

            # Build mapping from old line numbers to new line numbers
            old_lines = sorted(self.lines.keys())
            line_map = {}

            new_num = new_start
            for old_num in old_lines:
                line_map[old_num] = new_num
                new_num += increment

            # Walk AST and update line number references
            self._renum_ast(ast, line_map)

            # Serialize updated AST back to source
            self.lines = {}
            for line_node in ast.lines:
                line_text = self._serialize_line(line_node)
                self.lines[line_node.line_number] = line_text

            print("Renumbered")

        except Exception as e:
            print(f"?Error during renumber: {e}")

    def _renum_ast(self, ast, line_map):
        """Walk AST and update all line number references

        Args:
            ast: ProgramNode to update
            line_map: dict mapping old line numbers to new line numbers
        """
        # Update line numbers in each LineNode
        for line_node in ast.lines:
            if line_node.line_number in line_map:
                line_node.line_number = line_map[line_node.line_number]

            # Update references in statements
            for stmt in line_node.statements:
                self._renum_statement(stmt, line_map)

    def _renum_statement(self, stmt, line_map):
        """Recursively update line number references in a statement

        Args:
            stmt: Statement node to update
            line_map: dict mapping old line numbers to new line numbers
        """
        import ast_nodes

        stmt_type = type(stmt).__name__

        # GOTO statement
        if stmt_type == 'GotoStatementNode':
            if stmt.line_number in line_map:
                stmt.line_number = line_map[stmt.line_number]

        # GOSUB statement
        elif stmt_type == 'GosubStatementNode':
            if stmt.line_number in line_map:
                stmt.line_number = line_map[stmt.line_number]

        # ON...GOTO/GOSUB statement
        elif stmt_type == 'OnGotoStatementNode' or stmt_type == 'OnGosubStatementNode':
            stmt.target_lines = [
                line_map.get(line, line) for line in stmt.target_lines
            ]

        # IF statement with line number jumps
        elif stmt_type == 'IfStatementNode':
            if stmt.then_line_number is not None and stmt.then_line_number in line_map:
                stmt.then_line_number = line_map[stmt.then_line_number]
            if stmt.else_line_number is not None and stmt.else_line_number in line_map:
                stmt.else_line_number = line_map[stmt.else_line_number]

            # Also update statements within THEN/ELSE blocks
            for then_stmt in stmt.then_statements:
                self._renum_statement(then_stmt, line_map)
            for else_stmt in stmt.else_statements:
                self._renum_statement(else_stmt, line_map)

        # RESTORE statement
        elif stmt_type == 'RestoreStatementNode':
            if stmt.line_number_expr and hasattr(stmt.line_number_expr, 'value'):
                # It's a literal number
                if stmt.line_number_expr.value in line_map:
                    stmt.line_number_expr.value = line_map[stmt.line_number_expr.value]

        # RUN statement
        elif stmt_type == 'RunStatementNode':
            if hasattr(stmt, 'line_number') and stmt.line_number in line_map:
                stmt.line_number = line_map[stmt.line_number]

    def _serialize_line(self, line_node):
        """Serialize a LineNode back to source text

        Args:
            line_node: LineNode to serialize

        Returns:
            str: Source text for the line
        """
        # Start with line number
        parts = [str(line_node.line_number)]

        # Serialize each statement
        for i, stmt in enumerate(line_node.statements):
            stmt_text = self._serialize_statement(stmt)
            if i == 0:
                parts.append(' ' + stmt_text)
            else:
                parts.append(' : ' + stmt_text)

        return ''.join(parts)

    def _serialize_statement(self, stmt):
        """Serialize a statement node back to source text

        Args:
            stmt: Statement node to serialize

        Returns:
            str: Source text for the statement
        """
        import ast_nodes

        stmt_type = type(stmt).__name__

        # This is a simplified serializer - only handles common cases
        # For a complete implementation, we'd need to handle all statement types

        if stmt_type == 'PrintStatementNode':
            parts = ['print']
            for i, expr in enumerate(stmt.expressions):
                if i > 0 and i <= len(stmt.separators):
                    # Add separator from previous expression
                    sep = stmt.separators[i-1] if i-1 < len(stmt.separators) else ''
                    if sep:
                        parts.append(sep)
                parts.append(' ' if not parts[-1].endswith(' ') else '')
                parts.append(self._serialize_expression(expr))
            return ''.join(parts)

        elif stmt_type == 'GotoStatementNode':
            return f"goto {stmt.line_number}"

        elif stmt_type == 'GosubStatementNode':
            return f"gosub {stmt.line_number}"

        elif stmt_type == 'LetStatementNode':
            var_text = self._serialize_variable(stmt.variable)
            expr_text = self._serialize_expression(stmt.expression)
            return f"{var_text} = {expr_text}"

        elif stmt_type == 'EndStatementNode':
            return "end"

        elif stmt_type == 'ReturnStatementNode':
            return "return"

        elif stmt_type == 'StopStatementNode':
            return "stop"

        elif stmt_type == 'RemarkStatementNode':
            # Preserve comments using REM
            return f"rem {stmt.text}"

        elif stmt_type == 'IfStatementNode':
            parts = ['if ', self._serialize_expression(stmt.condition)]
            if stmt.then_line_number is not None:
                parts.append(f' then {stmt.then_line_number}')
            elif stmt.then_statements:
                parts.append(' then ')
                parts.append(' : '.join(self._serialize_statement(s) for s in stmt.then_statements))
            if stmt.else_line_number is not None:
                parts.append(f' else {stmt.else_line_number}')
            elif stmt.else_statements:
                parts.append(' else ')
                parts.append(' : '.join(self._serialize_statement(s) for s in stmt.else_statements))
            return ''.join(parts)

        elif stmt_type == 'ForStatementNode':
            var = self._serialize_variable(stmt.variable)
            start = self._serialize_expression(stmt.start_value)
            end = self._serialize_expression(stmt.end_value)
            parts = [f"for {var} = {start} to {end}"]
            if stmt.step_value:
                step = self._serialize_expression(stmt.step_value)
                parts.append(f" step {step}")
            return ''.join(parts)

        elif stmt_type == 'NextStatementNode':
            if stmt.variables:
                vars_text = ', '.join(self._serialize_variable(v) for v in stmt.variables)
                return f"next {vars_text}"
            return "next"

        elif stmt_type == 'OnGotoStatementNode':
            expr = self._serialize_expression(stmt.expression)
            lines = ','.join(str(line) for line in stmt.target_lines)
            return f"on {expr} goto {lines}"

        elif stmt_type == 'OnGosubStatementNode':
            expr = self._serialize_expression(stmt.expression)
            lines = ','.join(str(line) for line in stmt.target_lines)
            return f"on {expr} gosub {lines}"

        # For other statement types, use a generic approach
        # This is a fallback - ideally all statement types should be handled explicitly
        else:
            # Try to reconstruct from the original source if possible
            # For now, return a placeholder
            return f"rem {stmt_type}"

    def _serialize_variable(self, var):
        """Serialize a variable reference"""
        text = var.name
        if var.type_suffix:
            text += var.type_suffix
        if var.subscripts:
            subs = ','.join(self._serialize_expression(sub) for sub in var.subscripts)
            text += f"({subs})"
        return text

    def _serialize_expression(self, expr):
        """Serialize an expression node to source text"""
        import ast_nodes

        expr_type = type(expr).__name__

        if expr_type == 'NumberNode':
            return str(expr.value)

        elif expr_type == 'StringNode':
            return f'"{expr.value}"'

        elif expr_type == 'VariableNode':
            return self._serialize_variable(expr)

        elif expr_type == 'BinaryOpNode':
            left = self._serialize_expression(expr.left)
            right = self._serialize_expression(expr.right)
            return f"{left} {expr.operator} {right}"

        elif expr_type == 'UnaryOpNode':
            operand = self._serialize_expression(expr.operand)
            return f"{expr.operator}{operand}"

        elif expr_type == 'FunctionCallNode':
            args = ','.join(self._serialize_expression(arg) for arg in expr.arguments)
            return f"{expr.function_name}({args})"

        else:
            return "?"

    def cmd_auto(self, args):
        """AUTO [start][,increment] - Automatic line numbering mode

        AUTO - Start at 10, increment by 10
        AUTO 100 - Start at 100, increment by 10
        AUTO 100,5 - Start at 100, increment by 5
        AUTO ,5 - Start at 10, increment by 5
        """
        start = 10
        increment = 10

        if args:
            parts = args.split(',')
            # Handle "AUTO start" or "AUTO start,increment"
            if parts[0].strip():
                try:
                    start = int(parts[0].strip())
                except ValueError:
                    print("?Syntax error")
                    return
            # Handle "AUTO ,increment" or "AUTO start,increment"
            if len(parts) > 1 and parts[1].strip():
                try:
                    increment = int(parts[1].strip())
                except ValueError:
                    print("?Syntax error")
                    return

        # Enter AUTO mode
        current_line = start

        try:
            while True:
                # Check if line already exists
                if current_line in self.lines:
                    # Show asterisk for existing line
                    prompt = f"*{current_line} "
                else:
                    # Show line number for new line
                    prompt = f"{current_line} "

                # Read input
                try:
                    line_text = input(prompt)
                except EOFError:
                    # Ctrl+D exits AUTO mode
                    print()
                    break

                # Check if line is empty (just pressing Enter)
                if not line_text or not line_text.strip():
                    # Empty line exits AUTO mode
                    break

                # Add the line with its number
                full_line = str(current_line) + " " + line_text.strip()
                self.lines[current_line] = full_line

                # Move to next line number
                current_line += increment

        except KeyboardInterrupt:
            # Ctrl+C exits AUTO mode
            print()
            return

    def cmd_system(self):
        """SYSTEM - Exit to operating system"""
        print("Goodbye")
        sys.exit(0)

    def cmd_files(self, filespec):
        """FILES [filespec] - Display directory listing

        FILES - List all .bas files in current directory
        FILES "*.BAS" - List files matching pattern
        FILES "A:*.*" - List files on drive A (not supported, lists current dir)
        """
        import glob
        import os

        # Default pattern if no argument
        if not filespec:
            pattern = "*.bas"
        else:
            # Remove quotes if present
            pattern = filespec.strip().strip('"').strip("'")

            # If pattern is empty after stripping, use default
            if not pattern:
                pattern = "*.bas"

        # In MBASIC, FILES shows disk directory. We'll list matching files in current directory
        # Get matching files
        try:
            files = sorted(glob.glob(pattern))

            if not files:
                print(f"No files matching: {pattern}")
                return

            # Display files (MBASIC shows them in columns)
            # Simple format: one per line with size
            for filename in files:
                try:
                    size = os.path.getsize(filename)
                    # MBASIC shows file sizes in bytes or blocks
                    # We'll show bytes
                    print(f"{filename:<20} {size:>8} bytes")
                except OSError:
                    print(f"{filename:<20}        ? bytes")

            # Show count
            print(f"\n{len(files)} File(s)")

        except Exception as e:
            print(f"?{type(e).__name__}: {e}")

    def execute_immediate(self, statement):
        """Execute a statement in immediate mode (no line number)

        Uses persistent runtime so variables persist between statements.
        If a program has been run (or stopped), use the program runtime
        so immediate mode can examine/modify program variables.
        """
        # Build a minimal program with line 0
        program_text = "0 " + statement

        try:
            tokens = list(tokenize(program_text))
            parser = Parser(tokens)
            ast = parser.parse()

            # Choose which runtime to use:
            # - If program has been run (especially if stopped), use program runtime
            # - Otherwise use immediate mode runtime
            if self.program_runtime is not None:
                # Use program runtime so we can access program variables
                runtime = self.program_runtime
                interpreter = self.program_interpreter
            else:
                # Initialize immediate mode runtime if needed
                if self.runtime is None:
                    self.runtime = Runtime(ast)
                    self.runtime.setup()
                    self.interpreter = Interpreter(self.runtime)
                    # Pass reference to interactive mode for commands like LOAD/SAVE
                    self.interpreter.interactive_mode = self
                runtime = self.runtime
                interpreter = self.interpreter

            # Execute just the statement at line 0
            if ast.lines and len(ast.lines) > 0:
                line_node = ast.lines[0]
                # Update runtime's current line
                old_line = runtime.current_line
                old_index = runtime.current_stmt_index
                runtime.current_line = line_node
                runtime.current_stmt_index = 0

                # Execute each statement on line 0
                for stmt in line_node.statements:
                    interpreter.execute_statement(stmt)

                # Restore previous line/index (important for stopped programs)
                runtime.current_line = old_line
                runtime.current_stmt_index = old_index

        except Exception as e:
            print(f"?{type(e).__name__}: {e}")

    def get_program_text(self):
        """Get program as text"""
        lines = []
        for line_num in sorted(self.lines.keys()):
            lines.append(self.lines[line_num])
        return '\n'.join(lines) + '\n'
