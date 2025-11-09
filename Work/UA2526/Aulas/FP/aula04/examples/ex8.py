lista_numeros = []

print("Introduza um número de cada vez. Clique ENTER para terminar.")

while True:
    entrada = input("Introduza um número ou ENTER: ")
    
    if entrada.lower() == '':
        break  # Sai do loop
    
    try:
        # Tenta converter a entrada para inteiro
        numero = int(entrada)
        lista_numeros.append(numero)
    except ValueError:
        # Lida com a situação em que a entrada não é um número e não é 'fim'
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print("A lista de números é:", lista_numeros)