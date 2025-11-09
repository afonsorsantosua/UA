n = int(input("Digite um número inteiro não negativo: "))

def factorial(n):
    assert isinstance(n, int), "n should be an int"
    assert n >= 0            , "n should not be negative"
    # Complete aqui
    if n <= 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
        
    return resultado

print(n, ' fatorial é: ', factorial(n))