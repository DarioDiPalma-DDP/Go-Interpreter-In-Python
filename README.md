# Go-Interpreter-In-Python
A Go Interpreter written in Python using Lark a modern parsing library for Python<br/>

Golang Grammar: https://golang.org/ref/spec<br/>
Lark: https://lark-parser.readthedocs.io/en/latest/index.html#<br/>

# Go-Interpreter-in-Python

Creation of a Golang interpreter written in Python using a modern parsing library.

The restriction included:
Data types: 
> Integer, Boolean, String, Array Type

Arithmetic operators: 
> Addition(+), Subtraction(-), Multiplication(*), Division (/)

Comparison Operators: 
> Equal to(a == b), Not equal to(a != b), Greater than(a > b), Less than (a < b), Greater or equal to (a >= b), Less or equal to (a <= b)

Logical Operators: 
> Logical NOT (!a), Logical AND (a && b), Logical OR (a || b)

Branching instructions: 
> If Statement, Else Statement, Else If Statement

Loop Instructions: 
> For Statement (works as While in Go)

Input Instructions: 
> Keyboard input

Output Instructions: 
> Print in command window

Execution methods: 
> REPL mode, Script file mode


# Execution mode 
1. Install Python<br/>
2. pip install lark<br/>

REPL mode:<br/>
- python main.py<br/>
Script mode:<br/>
- python main.py -s (--script) script/file/location.go<br/>
Debug mode (displays parse tree):<br/>
- python main.py -d (--debug)