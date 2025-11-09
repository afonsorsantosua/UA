

def main():
    while ( True ):
        file_name = input('File name: ')
        try:
            file = open(file_name, 'r')
            for line in file:
                print(line, end='')
            break
        except IOError:
            print('File does not exist.')
    file.close()

if (__name__ == '__main__'):
    main()