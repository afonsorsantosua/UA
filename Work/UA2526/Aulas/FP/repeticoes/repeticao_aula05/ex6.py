

def shorten(str):
    sigla = ''
    for caracteres in str:
        if caracteres.isupper() == True:
            sigla += caracteres
        else:
            continue
    return sigla


print(shorten('Universidade de Aveiro'))
print(shorten('United Nations Organization'))