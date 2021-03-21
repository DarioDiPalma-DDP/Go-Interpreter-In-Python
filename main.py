import argparse

from lark import Lark,UnexpectedInput

import transformer
import interpreter
import error_handle

parser = Lark.open("grammar.lark", parser="lalr", start="program")

def main():
    # Initialize the argument parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--script", "-s", help="set script file location")
    arg_parser.add_argument("--debug", "-d", help="enable debug mode", action='store_true')

    # Read arguments from the command line
    args = arg_parser.parse_args()

    # Check for --width
    if args.script:
        with open(args.script) as f:
            read_data = f.read()
            tree = parser.parse(read_data, on_error=error_handle.handler)
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

def start_repl(debug_mode):
    while True:
        try:
            s = input(">>> ")
            if s == "":
                continue
        #except EOFError:
            #break
        
        #try:
            tree = parser.parse(s,on_error=error_handle.handler)
        except UnexpectedInput as u:
            exc_class = u.match_examples(parser.parse,{
                error_handle.GoMissingValue: ["var x =",
                                              "var x int =",
                                              "x :=",
                                              "var x",
                                              "var x int"]
            }, use_accepts=True)
            if not exc_class:
                raise
            raise exc_class(u.get_context(s),u.line,u.column)

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