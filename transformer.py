from lark import Transformer

from symbol_table import st, SymbolNotExistentException

from error_handler import *

class TreeTransformer(Transformer):

    # Variable assignment
    def assignment(self, items):
        ident = items[0]
        if (len(items)==3 and check_data_type(items)): # there is type specification
            if len(ident.children) == 1: # var x int = 2
                st.set(ident.children[0], items[2].children[0])
            else:   # var x,y int = 2,3 || var x,y,z int = 1
                if len(items[2].children) == 1:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[2].children[0])
                else:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[2].children[i])

        elif(len(items)==2): # No type specification
            if len(ident.children) == 1: # var x = 2
                st.set(ident.children[0], items[1].children[0])
            else:   # var x,y = 2,3 || var x,y,z = 1
                if len(items[1].children) == 1:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[1].children[0])
                else:
                    for i in range(len(ident.children)):
                        st.set(ident.children[i], items[1].children[i])
        else:
            print("There was an Error in your declaration")

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


    def array_assignment(self, items):
        try:
            length = items[1].children[0].value
            array_type = items[1].children[1].value
            elements = items[2].children
            if int(length) != len(elements):
                raise OutOfLenght
            elif array_type == "int":
                type_check(elements,int)
            elif array_type == "string":
                type_check(elements,str)
            elif array_type == "bool":
                type_check(elements,bool)
            st.set(items[0].children[0], elements)
        except OutOfLenght:
            print("Lenght of array don't coincide with the number of elements")
        except TypeDifferentError:
            print("The elements you enter doesn't is conform with the type specificed")

    # Relational operators
    def less(self, items):
        return items[0] < items[1]

    def great(self, items):
        return items[0] > items[1]

    def great_eq(self, items):
        return items[0] >= items[1]

    def less_eq(self, items):
        return items[0] <= items[1]

    def equal(self, items):
        return items[0] == items[1]

    def not_equal(self, items):
        return items[0] != items[1]

    # Operands translation
    def factor(self, items):
        if items[0].type == 'NUMBER':
            return int(items[0].value)
        elif items[0].type == 'IDENTIFIER':
            if (items[0].value == "true" or items[0].value == "false"):
                return items[0].value
            try:
                return st.get(items[0].value)
            except SymbolNotExistentException:
                print("ERROR: Variable " + items[0].value + " does not exist.")
        elif items[0].type == 'STRING':
            return str(items[0].value.strip('"'))

    def index(self, items):
        array = st.get(items[0].value)
        return array[items[1]]
    
    def term(self, items):
        return items[0]

    def expression(self, items):
        return items[0]

    # Arithmetic Operations
    def addition(self, items):
        try:
            op_type(items)
            return items[0] + items[1]
        except UnsupportedOperationType:
            print("The operation you enter isn't supported by type")

    def subtraction(self, items):
        try:
            op_type(items)
            return items[0] - items[1]
        except UnsupportedOperationType:
            print("The operation you enter isn't supported by type")

    def multiplication(self, items):
        try:
            op_type(items)
            return items[0] * items[1]
        except UnsupportedOperationType:
            print("The operation you enter isn't supported by type")

    def division(self, items):
        try:
            op_type(items)
            return items[0] / items[1]
        except UnsupportedOperationType:
            print("The operation you enter isn't supported by type")

    # Boolean logic
    def bool_and(self, items):
        return items[0] and items[1]

    def bool_or(self, items):
        return items[0] or items[1]

    def bool_not(self, items):
        return not items[0]

    def bool_logic(self, items):
        return items[0]

    # Keyboard input
    def scanf(self, items):
        return input(items[0])