class Error(Exception):
    pass

class OutOfLenght(Error):
    # When Array lenght different from number of element defined
    pass
class TypeDifferentError(Error):
    # Type different from specified
    pass

class UnsupportedOperationType(Error):
    pass

def check_data_type(items):
    try:
        types = str(items[1].value)
        if types == "int":
            type_check(items[2].children,int)
            return True
        elif types == "string":
            type_check(items[2].children,str)
            return True
        elif types == "bool":
            type_check(items[2].children,bool)
            return True
    except TypeDifferentError:
        print("The elements you enter doesn't is conform with the type specificed")
        return False

    
def type_check(elements,type_to_check):
    if(type_to_check != bool):
        for x in range(len(elements)):
                    if not isinstance(elements[x],type_to_check):
                        raise TypeDifferentError
    else:
        for x in range(len(elements)):
                    if not isinstance(bool(elements[x]),bool):
                        raise TypeDifferentError

def op_type(items):
    if (type(items[0])!=type(items[1])):
        raise UnsupportedOperationType

def handler(e):
    #SKIP TOKEN SEMICOLON
    if e.token.type == "SEMICOLON":
        return True
    
    #Unhandled error
    return False