

def evenThenOdd(s):
    nova_ordem = s[0::2] + s[1::2]
    return nova_ordem



def numero(n):
    lst = []
    for i in range(1, n + 1):
        a = [i] * i
        lst.extend(a)
    return lst

def primeiro(lst):
    a = 0
    b = 0
    for i in lst:
        if lst[i] > lst[i - 1]:
            if lst[i] > a:
                a = lst[i]
                b = i
    return a[i]


# def main():
    lista_um = 'abcd'
    impr = evenThenOdd(lista_um)
    print(impr)

    n = numero(5)
    print(n)

    lista = [1, 2, 3, 4]
    # m = p





main()
