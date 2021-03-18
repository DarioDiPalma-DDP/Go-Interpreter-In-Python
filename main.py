import argparse

from lark import Lark

import transformer
import interpreter

parser = Lark.open("grammar.lark", parser="lalr", start="program")

def main():
    # Initialize the argument parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--script", "-s", help="set script file location")

    # Read arguments from the command line
    args = arg_parser.parse_args()

    # Check for --width
    if args.script:
        with open(args.script) as f:
            read_data = f.read()
            tree = parser.parse(read_data)
            print("DEBUG: Parse Tree:")
            print(tree.pretty())
            try:
                evals = interpreter.GoInterpreter().visit(tree)
                for eval in evals:
                    if eval is not None:
                        print(str(eval))
            except AttributeError:
                pass
    else:
        start_repl()

    
def start_repl():
    while True:
        try:
            s = input(">>> ")
            if s == "":
                continue
        except EOFError:
            break
        tree = parser.parse(s)
        print("DEBUG: Parse Tree:")
        print(tree.pretty())
        try:
            eval = interpreter.GoInterpreter().visit(tree)
            if eval is not None:
                print(str(eval))
        except AttributeError:
            pass


if __name__ == "__main__":
    main()