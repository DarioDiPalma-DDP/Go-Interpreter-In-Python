class Error(Exception):
    pass

class OutOfLenght(Error):
    # When Array lenght different from number of element defined
    pass
class TypeDifferentError(Error):
    # Type different from specified
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
    except TypeDifferentError:
        print("The elements you enter doesn't is conform with the type specificed")
        return False

    
def type_check(elements,type_to_check):
    for x in range(len(elements)):
                    if not isinstance(elements[x],type_to_check):
                        raise TypeDifferentError