def divisoresProprios(n):
    assert n > 0
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    return lst

def numeroDeficiente(a):
    lista = divisoresProprios(a)
    if sum(lista) < a:
        return 'Número deficiente'
    elif sum(lista) == a:
        return 'Número perfeito'
    else:
        return 'Número abundante'
    


a = int(input('Introduza um número: '))
print(divisoresProprios(a))
print(numeroDeficiente(a))