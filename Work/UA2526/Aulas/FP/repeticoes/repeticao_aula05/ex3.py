

def inputFloatList():
    print('Introuduza uma sequência de números (pressionar ENTER para terminar): ')
    lst = []
    i = input('>> ')
    try:
        while i != '':
            i = int(i)
            lst.append(i)
            i = input('>> ')
        lst.sort()
        return lst
    except ValueError:
        print('Não pode ser introduzida uma string.')


def countLower(lst, v):
    menores = []
    for item in lst:
        if item < v:
            menores.append(item)
        else:
            continue
    menores2 = len(menores)
    return menores2


def minmax(lst):
    lst.sort()
    menor = lst[0]
    maior = lst[-1]
    return menor, maior



def main():
    n = inputFloatList()
    print(f'Sequência introduzida: {n}.')

    v = int(input('Introduza um valor para contar quantos existem na sequência menores que o valor introduzido: '))
    m = countLower(n, v)
    print(f'Há {m} valores menores do que {v}.')

    extremos = minmax(n)
    print(f'O menor e o maior valores são, respetivamente {extremos}.')


if __name__ == '__main__':
    main()