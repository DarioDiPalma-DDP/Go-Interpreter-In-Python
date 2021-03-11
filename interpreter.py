from lark.visitors import Interpreter

from symbol_table import st

class GoInterpreter(Interpreter):
    def conditional(self, tree):
        print(tree)

    def assignment(self, tree):
        st.set(tree.children[0].value, tree.children[1])