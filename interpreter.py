from lark.visitors import Interpreter

import transformer
from symbol_table import st

# Transfomer visits a sub-tree bottom-up and run appropriate methods
trans = transformer.TreeTransformer()

# Interpreter is used to visit the root tree top-down
class GoInterpreter(Interpreter):
    def conditional(self, tree):
        conds = tree.find_data('condition')
        for cond in conds:
            trans_tree = trans.transform(cond)
            print("DEBUG: Transformed condition")
            print(trans_tree)
            if trans_tree.children[0]:
                print("DEBUG: Condition is True")
                self.visit_children(tree)

    def while_loop(self, tree):
        print("DEBUG: Relation tree")
        rel = tree.children[0]
        print(rel)

        while trans.transform(rel):
            trans_tree = trans.transform(rel)
            print("DEBUG: Transformed relation")
            print(trans_tree)
            blocks = tree.find_data('block_statement')
            for block in blocks:
                self.visit_children(block)

    def for_loop(self, tree):
        assign = tree.children[0]
        trans.transform(assign)

        rel = tree.children[1]
        ident = tree.children[2]
        while trans.transform(rel):
            trans_tree = trans.transform(rel)
            print("DEBUG: Transformed relation")
            print(trans_tree)
            blocks = tree.find_data('block_statement')
            for block in blocks:
                print(block)
                self.visit_children(block)

            cur_value = st.get(ident)
            st.set(ident, cur_value+1)


    def block_statement(self, tree):
        return trans.transform(tree)

    def declaration(self, tree):
        return trans.transform(tree)
    
    def assignment(self, tree):
        return trans.transform(tree)

    def short_assignment(self, tree):
        return trans.transform(tree)

    def expression(self, tree):
        return trans.transform(tree)
    
    def call(self, tree):
        if tree.children[0].value == 'print':
            return trans.transform(tree.children[1])
