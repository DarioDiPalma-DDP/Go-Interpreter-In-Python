class SymbolTable():
    def __init__(self, extend={}):
            self.__st = extend

    def get(self, ident):
        if ident in self.__st:
            return self.__st[ident]
        else:
            raise SymbolNotExistentException
    
    def set(self, ident, value):
        self.__st[ident] = value


class SymbolTableExcpetion(Exception):
    pass

class SymbolNotExistentException(SymbolTableExcpetion):
    pass

st = SymbolTable()