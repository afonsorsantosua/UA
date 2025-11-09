# exercicio_8_media_sentinela.py

def calcular_media_sequencia():
    """
    Lê uma sequência de números (terminada por uma linha vazia/ENTER) 
    e calcula a média dos números válidos.
    """
    soma = 0.0
    contagem = 0
    
    print("Introduza os números reais (um por linha).")
    print("Pressione ENTER numa linha vazia para terminar a sequência e calcular a média.")
    
    # 1. Primeira leitura (para inicializar a variável de controlo do loop)
    linha = input("Número: ") 
    
    # 2. Loop controlado por sentinela (linha vazia)
    while linha != "":
        try:
            # Tenta converter a linha para um número float
            numero = float(linha)
            soma += numero
            contagem += 1
            
        except ValueError:
            # Se a linha não for um número válido
            print(f"'{linha}' não é um número válido. Este valor será ignorado.")
            
        # Pede o próximo input dentro do loop, garantindo que a variável 'linha'
        # é atualizada para a condição de saída.
        linha = input("Número: ")

    print("-" * 30)

    # 3. Saída e cálculo final
    if contagem > 0:
        media = soma / contagem
        print(f"Total de números válidos: {contagem}")
        # Formata a média para ter 4 casas decimais (ou o que for preferível)
        print(f"A média dos números introduzidos é: {media:.4f}")
    else:
        print("Não foi introduzido nenhum número válido.")

if __name__ == "__main__":
    calcular_media_sequencia()