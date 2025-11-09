def pedir_numeros():
    
    numeros = []
    print("Digite um número por linha (ou 'fim' para terminar): ")

    while True:
        entrada = input("> ").strip() # O .strip() remove espaços em branco no início e fim

        # 1. Condição de Parada
        if entrada.lower() == 'fim' or not entrada:
            # Se a entrada for 'fim' (em qualquer caixa) ou vazia, o loop é interrompido.
            break

        # 2. Tentativa de Conversão e Tratamento de Erro
        try:
            # Tenta converter a entrada para um inteiro
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            # Se a conversão falhar (o usuário digitou texto que não é número)
            print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim' para terminar.")
            # O loop continua, pedindo nova entrada

    return numeros

# Exemplo de como usar a função:

lista_final = pedir_numeros()

print("\n--- Resultado ---")
print(f"Você digitou {len(lista_final)} números.")
print(f"Lista de números: {lista_final}")