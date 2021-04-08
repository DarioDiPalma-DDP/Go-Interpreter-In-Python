# Go-Interpreter-In-Python
A Go Interpreter written in Python using Lark a modern parsing library for Python, with @markserver<br/>

Golang Grammar: https://golang.org/ref/spec<br/>
Lark: https://lark-parser.readthedocs.io/en/latest/index.html#<br/>

#

### Supported restriction:
Data types: 
> * Integer
> * Boolean
> * String
> * Array Type

Arithmetic operators: 
> * Addition(+) 
> * Subtraction(-)
> * Multiplication(*)
> * Division (/)

Comparison Operators: 
> * Equal to(a == b)
> * Not equal to(a != b)
> * Greater than(a > b)
> * Less than (a < b)
> * Greater or equal to (a >= b)
> * Less or equal to (a <= b)

Logical Operators: 
> * Logical NOT (!a)
> * Logical AND (a && b)
> * Logical OR (a || b)

Branching instructions: 
> * If Statement 
> * Else Statement
> * Else If Statement

Loop Instructions: 
> * For Statement (works as While in Go)

Input Instructions: 
> * Keyboard input

Output Instructions: 
> * Print in command window

Execution methods: 
> * REPL mode
> * Script file mode

### Errors handled
1. Lexical error (missing or wrong symbols)

2. Syntax error: 
    * UnmatchedParenthesis number in statement
    * MissingValue in variable declaration

3. Semantic error: 
    * ArrayOutOfLenght when we declare an array
    * TypeDifferentError for variable type declaration 
    * UnsupportedOperationType for all operation of different type

# Execution mode 
1. Install Python (3.9.4 our version if you have problems)<br/>
2. pip install lark<br/>

REPL mode:
> python main.py

Script mode:
> python main.py -s (--script) script_test\test_*.go (PATH_to_file\file.go)

Debug mode (displays parse tree):
> python main.py -d (--debug)<br/>
Supported both of REPL and Script mode