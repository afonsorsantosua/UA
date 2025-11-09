def max2(a, b):
    if a > b:
        return a
    else:
        return b

print("Com 4 e 3 o maior número é: ", max2(4, 3))
print("Com -3 e -2 o maior número é: ", max2(-3, -2))
print("Com 1000 e 453025 o maior número é: ", max2(1000, 453025))

def max3(a, b, c):
    return max2(a, max2(b, c))

print("Com 4, 5 e 6 o maior número é: ", max3(4, 11, 6))