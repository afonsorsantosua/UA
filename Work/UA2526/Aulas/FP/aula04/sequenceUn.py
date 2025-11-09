print("n", "Un")
Un = 100
n = 0
while Un > 0:
   n = n + 1
   print(n, Un)
   Un = 1.01*Un - 1.01

print('São ', n+1, 'termos positivos.')