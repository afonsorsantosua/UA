A = int(input('Andares? '))
M = int(input('Moradores por andar? '))
t = 365
dp_primeiroA = 2*M*3*t
dp_ultimoA = 2*M*3*A*t
dp_m = (dp_primeiroA + dp_ultimoA)*A/2
dp_km = dp_m/1000
t_de_funcionamento = dp_m/3600
print('Distância percorrida pelo elevador em um ano em km: ', dp_km, 'km.')
print('Tempo de funcionamento do elevador em um ano em horas: ', t_de_funcionamento, 'horas.')