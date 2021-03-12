from lark import Transformer

from symbol_table import st, SymbolNotExistentException

class TreeTransformer(Transformer):

    # Variable assignment
    def assignment(self, items):
        st.set(items[0].value, items[1])

    # Relational operators
    def less(self, items):
        return items[0] < items[1]

    def great(self, items):
        return items[0] > items[1]

    # Operands translation
    def factor(self, items):
        if items[0].type == 'NUMBER':
            return int(items[0].value)
        elif items[0].type == 'IDENTIFIER':
            try:
                return st.get(items[0].value)
            except SymbolNotExistentException:
                print("ERROR: Variable " + items[0].value + " does not exist.")
        elif items[0].type == 'STRING':
            return str(items[0].value.strip('"'))
    
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
