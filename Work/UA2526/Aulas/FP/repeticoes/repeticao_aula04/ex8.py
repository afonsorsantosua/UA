
def inNumero():
    print('Introduza uma sequência de números (pressione ENTER para terminar):')
    sequencia = input('>> ')
    lista = []

    while sequencia != '':
        sequencia = int(sequencia)
        lista.append(sequencia)
        sequencia = input('>> ')

        if sequencia == '':
            soma = sum(lista)
            contagem = len(lista)
            media = soma / contagem
            media = float(media)

    return 'Sequência introduzida:', lista, 'Média da lista introduzida: ', media

n = inNumero()
print(n)