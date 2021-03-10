from lark import Lark, Transformer

class MyTransformer(Transformer):
    def number(self, tok):
        return float(tok[0].value)
    def list(self, items):
        return list(items)
    def factor(self, items):
        return items[0]
    def term(self, items):
        return items[0]
    def expression(self, items):
        return items[0]
    def sum(self, items):
        return items[0]+items[1]
    def pair(self, key_value):
        k, v = key_value
        return k, v
    def dict(self, items):
        return dict(items)

calc_parser = Lark.open("grammar.lark", parser='lalr', start='statement')
calc = calc_parser.parse


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        tree = calc(s)
        print("Parse Tree:")
        print(tree.pretty())
        print("Evaluation:")
        print(MyTransformer().transform(tree))


if __name__ == '__main__':
    main()