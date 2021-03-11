from lark import Lark

import transformer
import interpreter

parser = Lark.open("grammar.lark", parser="lalr", start="statement")

def main():
    while True:
        try:
            s = input(">> ")
        except EOFError:
            break
        tree = parser.parse(s)
        print("Parse Tree:")
        print(tree.pretty())
        trans = transformer.TreeTransformer().transform(tree)
        if trans is not None:
            print("Transformation: " + str(trans))

        try:
            eval = interpreter.GoInterpreter().visit(trans)
            if eval is not None:
                print("Transformation: " + str(eval))
        except AttributeError:
            pass


if __name__ == "__main__":
    main()