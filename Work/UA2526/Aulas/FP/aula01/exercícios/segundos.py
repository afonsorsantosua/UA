horas = int(input('Horas? '))
minutos = int(input('Minutos? '))
segundos = int(input('Segundos? '))

total = horas * 3600 + minutos + 60 + segundos

print('Total de segundos: ', total)