import argparse

from lark import Lark, UnexpectedInput

import lark
import transformer
import interpreter
import error_handler

parser = Lark.open("grammar.lark", parser="lalr", start="program")


def main():
    # Initialize the argument parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--script", "-s", help="set script file location")
    arg_parser.add_argument(
        "--debug", "-d", help="enable debug mode", action="store_true"
    )

    # Read arguments from the command line
    args = arg_parser.parse_args()

    if args.script:
        with open(args.script) as f:
            read_data = f.read()
            try:
                tree = parse(read_data)
            except error_handler.MissingValue as e:
                print(e)
                exit()
            except error_handler.UnmatchedParenthesis as e:
                print(e)
                exit()

            if args.debug:
                print("DEBUG: Parse Tree:")
                print(tree.pretty())
            try:
                evals = interpreter.GoInterpreter().visit(tree)
                for eval in evals:
                    if eval is not None:
                        print(str(eval))
            except AttributeError:
                pass
            except TypeError:
                pass
    else:
        start_repl(args.debug)


def parse(s):
    try:
        tree = parser.parse(s)
    except UnexpectedInput as u:
        exc_class = u.match_examples(
            parser.parse,
            {
                error_handler.MissingValue: [
                    "var x =",
                    "var x int =",
                    "var x string =",
                    "x :=",
                ],
                error_handler.UnmatchedParenthesis: [
                    "var x = (a+b",
                    "var x = a+b)",
                    "var x = ((a+b)",
                    "var x = (a+b))",
                    "Printf((a)",
                    "Printf(a))",
                ],
            },
            use_accepts=True,
        )
        if not exc_class:
            raise
        raise exc_class(u.get_context(s), u.line, u.column)
    else:
        return tree


def start_repl(debug_mode):
    while True:
        try:
            s = input(">>> ")
            if s == "":
                continue
        except EOFError:
            break

        try:
            tree = parse(s)
        except lark.exceptions.UnexpectedToken:
            print("Operation Laxicaly wrong or not yet supported")
            continue
        except error_handler.MissingValue as e:
            print(e)
            continue
        except error_handler.UnmatchedParenthesis as e:
            print(e)
            continue

        if debug_mode:
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
