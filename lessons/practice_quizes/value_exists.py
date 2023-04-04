"""Value exist"""
def value_exist(xs: dict[str,int], y: int) -> bool:
    """Return true if int exists as value in dictionary"""
    exists: bool = False
    for value in xs:
        if xs[value] == y:
            exists: bool = True
    return exists

test_dict: dict[str,int] = { " a " : 2 , " b " : 4 , " c " : 7 , " d " : 1}
print(value_exist(test_dict, 5))
    
