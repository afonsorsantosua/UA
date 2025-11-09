def main():
    """
    Função principal: Solicita o nome do ficheiro e imprime o seu conteúdo.
    Permite ao utilizador tentar novamente se o ficheiro não for encontrado.
    """
    
    # Loop que continua até que o utilizador consiga abrir um ficheiro
    while (True):
        try:
            # 1. Solicita o nome do ficheiro (ex: 'data.txt')
            file_name = input('File name: ')
            
            # 2. Abre o ficheiro. O 'with open' é a melhor prática, 
            #    pois fecha o ficheiro automaticamente quando termina.
            with open(file_name, 'r') as file:
                
                # 3. Itera sobre o ficheiro, imprimindo linha por linha
                #    .strip() remove o caractere de nova linha que a leitura
                #    do ficheiro adiciona, evitando linhas em branco duplas.
                for line in file:
                    print(line.strip())
            
            # 4. Se a leitura foi bem-sucedida, saímos do loop 'while'
            break
            
        except FileNotFoundError:
            # 5. Se o ficheiro não existir (erro mais comum), 
            #    imprime uma mensagem e o loop 'while' recomeça
            print('File does not exist. Please check the name and try again.')
        
# Inicia o programa
main()