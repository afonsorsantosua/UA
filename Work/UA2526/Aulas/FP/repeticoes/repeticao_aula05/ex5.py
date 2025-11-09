

def countDigits(str):
    contar = 0
    for caracteres in str:
        if caracteres.isdigit() == True:
            contar += 1
        else:
            continue
    return contar

def main():
    str = input()
    print("str:", repr(str))
    print("result:", countDigits(str) )


if __name__ == "__main__":
    main()



