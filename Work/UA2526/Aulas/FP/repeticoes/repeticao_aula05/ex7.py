

def ispalindrome(str):

    normal = []

    for caracteres in str:
        normal.append(caracteres)

    reverse = normal[::-1]

    if reverse == normal:
        return True
    else:
        return False

def main():
    print('Osso: ', ispalindrome('osso'))
    print('Lápis: ', ispalindrome('lápis'))

main()