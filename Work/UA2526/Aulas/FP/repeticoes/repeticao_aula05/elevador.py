
ALTURA = 3.0  # Altura em metros de um andar
VIAGENS = 4   # Número de viagens diárias feitas por cada morador

def distanciaElevador(predio):
    distancia_por_piso = []
    for andar, moradores in enumerate(predio):
        distancia_metros = VIAGENS * moradores * andar * ALTURA
        distancia_por_piso.append(distancia_metros)
    soma = sum(distancia_por_piso)
    return soma

def pedidoUtilizador():
    pisos = int(input('Quantos pisos tem o prédio? '))
    moradores = []
    for piso in range(0, pisos):
        numero_moradores = int(input(f'Digite o número de moradores no piso {piso}: '))
        moradores.append(numero_moradores)
    return moradores



def main():
    # Numero de moradores em cada piso de um prédio:
    predio = pedidoUtilizador()  # 4 moradores no piso 0, 2 no piso 1, ...
    
    # Calcular distância percorrida pelo elevador num dia
    m_por_dia = distanciaElevador(predio)

    # E a distância percorrida num ano
    km_por_ano = m_por_dia * 365

    # Mostrar resultado
    print("No predio", predio)
    print("o elevador percorre", m_por_dia, "m por dia")
    print("ou seja,", km_por_ano, "km por ano") 



if __name__ == "__main__":
    main()

