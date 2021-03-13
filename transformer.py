from lark import Transformer

from symbol_table import st, SymbolNotExistentException

def isDataType(items):
    try:
        types = str(items[1].value)
        if (types == "int" or types == "string" or types == "bool"):
            """ TO-DO Gestire i tipi
            for i in range(len(items[2].children)):
                if not(isinstance(items[2].children[i],int) or isinstance(items[2].children[i],bool)):
                    print("Error not Int or Bool")
            """
            return True
        else: 
            return False
    except AttributeError:
        return False

    
def TypeCheck(items):
    return 0

class TreeTransformer(Transformer):

    # Var declaration
    def declarations(self, items):
        print("Funziono?")

    # Variable assignment
    def assignment(self, items):
        ident = items[0]
        if (isDataType(items)): #there is Type specification
            if len(ident.children) == 1: # var x int = 2
                st.set(ident.children[0], items[2])
            else:   # var x,y int = 2,3 || var x,y,z int = 1
                if len(items[2].children) == 1:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[2].children[0])
                else:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[2].children[i])

        else: # No type specification
            if len(ident.children) == 1: # var x = 2
                st.set(ident.children[0], items[1])
            else:   # var x,y = 2,3 || var x,y,z = 1
                if len(items[1].children) == 1:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[1].children[0])
                else:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[1].children[i])

    # x := 2
    def short_assignment(self, items):
        ident = items[0]
        if len(ident.children) == 1: # x := 2
                st.set(ident.children[0], items[1].children[0])
        else: # x,y := 2,3 || x,y,z := 1
            if len(items[1].children) == 1:
                for i in range(len(ident.children)):
                    st.set(ident.children[i], items[1].children[0])
            else:
                for i in range(len(ident.children)):
                    st.set(ident.children[i], items[1].children[i])

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

    # x,y,z
    #def ident_list(self, items):
    #    print(items[0])
    #    i = 0
    #    for item in items:
    #        items
    #        return item