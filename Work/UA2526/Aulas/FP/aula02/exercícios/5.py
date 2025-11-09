tempo_de_chamada = int(input("Digite o tempo de duração da chamada em segundos: "))

custo_menos_60 = 0.12

if tempo_de_chamada <= 60:
    print("O custo da chamada é: ", custo_menos_60, " €.")
else:
    custo_mais_60 = custo_menos_60 + (tempo_de_chamada - 60) * 0.002
    print("O custo da chamada é: ", custo_mais_60, " €.")