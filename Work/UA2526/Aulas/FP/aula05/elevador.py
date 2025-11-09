
ALTURA = 3
VIAGENS = 4

pisos = input('Quantos pisos tem o prédio? ')
moradores_piso0 = input('Quantos moradores no piso 0? ')
moradores_piso1 = input('Quantos moradores no piso 1? ')
moradores_piso2 = input('Quantos moradores no piso 2? ')


def main():
    # Numero de moradores em cada piso de um prédio:
    predio = [moradores_piso0, moradores_piso1, moradores_piso2]  # 4 moradores no piso 0, 2 no piso 1, ...

    def distanciaElevador(predio):
        total_metros = 0
        # Percorrer cada andar e calcular a distância percorrida
        for andar, moradores in enumerate(predio):
            distancia_andar = andar * ALTURA * 2 * VIAGENS * moradores
            total_metros += distancia_andar
        return total_metros

    
    # Calcular distância percorrida pelo elevador num dia
    m_por_dia = distanciaElevador(predio)

    # E a distância percorrida num ano
    km_por_ano = (m_por_dia * 365) / 1000

    # Mostrar resultado
    print("No predio", predio)
    print("o elevador percorre", m_por_dia, "m por dia")
    print("ou seja,", km_por_ano, "km por ano") 



if __name__ == "__main__":
    main()

