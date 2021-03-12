from lark import Lark

import transformer
import interpreter

parser = Lark.open("grammar.lark", parser="lalr", start="statement")

def main():
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