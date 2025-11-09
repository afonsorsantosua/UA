ATP1 = float(input("Digite a nota da ATP1: "))
ATP2 = float(input("Digite a nota da ATP2: "))

CTP = ((0.15 * ATP1 + 0.15 * ATP2) / 0.3)

API = float(input("Digite a nota da API: "))
APF = float(input("Digite a nota da APF: "))

CP = ((0.2 * API + 0.5 * APF) / 0.7)

NF = ((0.3 * CTP) + (0.7 * CP))

if (NF < 66):
    print("Reprovado por Nota Mínima")
    ATPR = float(input("Introduza a nota de recurso ATPR: "))
    APR = float(input("Introduza a nota de recurso APR: "))
    NR = (0.3 * ATPR) + (0.7 * APR)
    if (NR < 66):
        print("Reprovado.")
    else:
        print("Aprovado em recurso.")
else:
    print("Aprovado")