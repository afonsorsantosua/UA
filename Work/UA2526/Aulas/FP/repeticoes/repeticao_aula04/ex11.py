def isPrime(n):
    if n % 2 == 0:
        print(f'{n}: True')
    else:
        print(f'{n}: False')

def main():
    for i in range(1, 101):
        primo = isPrime(i)

main()