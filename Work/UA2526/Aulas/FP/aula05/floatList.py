def pedir_numeros():
    print("Digite um número por linhas (introduza enter quando terminar)")

    numero_introduzido = []
    while True:
        entrada = input()

        if entrada == '':
            break
    
        try:
            numero = int(entrada)
        except ValueError:
            print('Erro')
    
    return numeros

lista_final = pedir_numeros()

def countLower(lst, v):
    count = 0

    for num in lst:
        if num < v:
            count += 1
    
    return count

valor_v = 5

def minmax(lst):
    if not lst:
        return (None, None)
    
    minimo = lst[0]
    maximo = lst[0]

    for numero in lst[1:]:
        if numero < minimo:
            minimo = numero
        
        if numero > maximo:
            maximo = numero

    return (minimo, maximo)

lista_a = [42, 15, 99 , 7, 20, 500, 33]
min_a, max_a = minmax(lista_a)

def analise_lista():
    lista_de_numeros = pedir_numeros()

    if not lista_de_numeros:
        print("A lista está vazia. O programa terminou.")
        return
    
    min_val, max_val = minmax(lista_de_numeros)

    print(f"Lista introduzida: {lista_de_numeros}")
    print(f"Valor Mínimo: {min_val}")
    print(f"Valor Máximo: {max_val}")
    print(f"Média entre o Mínimo e o Máximo: {media_min_max:.2f}")

    contagem_inferior_a_media = countLower(lista_de_numeros, media_min_max)

    print(f"\nTOTAL: {contagem_inferior_a_media} números são inferiores à média ({media_min_max:.2f}).")



print(f"A lista de números que introduziu foi: {lista_final}.")
print("Foram introduzidos ", len(lista_final), " números.")
print("O valor de comparação (v) é: ", valor_v)
print("foram introduzidos ", countLower(lista_final, valor_v), "números inferiores a ", valor_v, ".")
print(f"Lista A: {lista_a}")
print(f"Mínimo: {min_a}, Máximo: {max_a}")