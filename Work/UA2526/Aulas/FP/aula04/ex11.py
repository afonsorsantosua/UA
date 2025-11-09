def isPrime(n):
    if n%3 == 0 or n%5 == 0 or n%7 == 0 or n%9 == 0:
        return 'True'
    else:
        return 'False'

numero = input("Introduza um número: ")
isPrime(numero)