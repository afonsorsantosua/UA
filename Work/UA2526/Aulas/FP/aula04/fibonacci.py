def fibonacci(number):
    if number == 1:
        print('0')
    elif number == 2:
        print('1')
    for i in range(3, number + 1):
        ...

enter_number = int(input("Enter a number: "))
fibonacci(enter_number)