def sum_(x:int, y:int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError('Both inputs must be integers')
    return x + y

def minus_(x:int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError('Both inputs must be integers')
    return x - y