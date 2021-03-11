from lark import Transformer

from symbol_table import st, SymbolNotExistentException

class TreeTransformer(Transformer):

    # Relational operators
    def less(self, items):
        return items[0] < items[1]

    def great(self, items):
        return items[0] > items[1]

    # Basic operands translation
    def factor(self, items):
        if items[0].type == 'NUMBER':
            return float(items[0].value)
        elif items[0].type == 'IDENTIFIER':
            try:
                return st.get(items[0].value)
            except SymbolNotExistentException:
                print("ERROR: Variable " + items[0].value + " does not exist.")

    
    def term(self, items):
        return items[0]

    def expression(self, items):
        return items[0]

    # Arithmetic Operations
    def addition(self, items):
        return items[0] + items[1]

    def subtraction(self, items):
        return items[0] - items[1]

    def multiplication(self, items):
        return items[0] * items[1]

    def division(self, items):
        return items[0] / items[1]
