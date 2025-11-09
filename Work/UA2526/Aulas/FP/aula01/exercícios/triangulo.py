import math

a = float(input('Cateto A: '))
b = float(input('Cateto B: '))

hipotenusa = (a**2 + b**2)**(1/2)
angulo = math.acos(a/hipotenusa)

conversao_angulo = int(math.degrees(angulo))

print('Hipotenusa: ', hipotenusa)
print('Ângulo entre A e C: ', conversao_angulo, 'graus')