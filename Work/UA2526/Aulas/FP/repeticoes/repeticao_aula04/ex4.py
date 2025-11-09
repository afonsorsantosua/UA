def factorial(n):
    assert isinstance(n, int), "n should be an int"
    assert n >= 0            , "n should not be negative"
    # Complete aqui
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    resultado = 1
    while n != 1:
        resultado *= n
        n -= 1
    return resultado