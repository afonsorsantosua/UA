def tax(r):
    if r <= 1000 :
        return 0.1 * r
    elif r <= 2000 :
        return 0.2 * r - 100
    else:
        return 0.3 * r - 300
    
print("Imposto para 800: ", tax(800))
print("Imposto para 1500: ", tax(1500))
print("Imposto para 2500: ", tax(2500))