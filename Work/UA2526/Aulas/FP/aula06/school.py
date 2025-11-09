# Complete o programa!

# a)
def loadFile(fname, lst):
    f = None
    try:
        f = open(fname, 'r', encoding='utf-8')

        next(f)

        for line in f:
            fields = line.strip().split('\t')

            if len(fields) == 5:
                numero_str, nome, nota1_str, nota2_str, nota3_str, nota4_str = fields

                try:
                    numero = int(numero_str)
                    nota1 = float(nota1_str)
                    nota2 = float(nota2_str)
                    nota3 = float(nota3_str)

                    aluno = (numero, nome, nota1, nota2, nota3)
                    lst.append(aluno)

                except ValueError:
                    print(f'Linha inválida no ficheiro {fname}')
    except FileNotFoundError:
        print(f'Erro ao encontar o ficheiro {fname}.')
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    nota1 = reg[2]
    nota2 = reg[3]
    nota3 = reg[4]

    media = (nota1 + nota2 + nota3) / 3

    return round(media, 2)

# c) Crie a função printPauta aqui...
...
def printPauta(lst):
    """
    Imprime a pauta (lista de registos de alunos) num formato legível,
    incluindo o número, nome e a nota final calculada.
    """
    print("-" * 50)
    print(f"{'Nº':<5} {'Nome':<30} {'Nota Final':>10}")
    print("-" * 50)

    for aluno in lst:
        # Extrai o número (índice 0) e o nome (índice 1)
        numero = aluno[0]
        nome = aluno[1]

        # Calcula a nota final usando a função criada
        n_final = notaFinal(aluno)

        # Imprime a linha
        print(f"{numero:<5} {nome:<30} {n_final:>10.2f}")

    print("-" * 50)

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort(key=operator.itemgetter(1))
    
    # mostrar a pauta
    print("\n--- Pauta Final ---")
         printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()


