def max2(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 'Os valores são iguais.'
    
def max3(c, d):
    if c > d:
        return c
    elif d > c:
        return d
    else:
        return 'Os valores são iguais.'

print('Para os valores 4 e 3 o maior é: ', max2(4, 3))
print('Para os valores -3 e -2 o maior é: ', max2(-3, -2))
print('-' * 30)
print('Para os valores 5, 4 e 3 o maior é: ', max3(5, max(4, 3)))
print('Para os valores -7, 8 e 4 o maior é: ', max3(-7, max(8, 4)))