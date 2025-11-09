
def parseMDY(date):
    """Return (year, month, day) from date in MM/DD/YYYY format."""
    a = 0
    for i in date:
        if i == "/":
            a += 1
    if a == 0:
        string = "0/0/" + date
        r = string.split("/")
    else:
        r = date.split("/")
    ano = int(r[2])
    mes = int(r[0])
    dia = int(r[1])
    return ano, mes, dia


def yearsBetween(date1, date2):
    """Return integer number of years between two (y, m, d) dates."""
    if date1[1] < date2[1]:
        resultado = date2[0] - date1[0]
    elif date1[1] > date2[1]:
        resultado = date2[0] - date1[0] - 1
    else:
        if date1[2] <= date2[2]:
            resultado = date2[0] - date1[0]
        else:
            resultado = date2[0] - date1[0] - 1
    return resultado



def main():
    # Test parseMDY
    print(f"{parseMDY('12/25/2024') = }")  # (2024, 12, 25)
    print(f"{parseMDY('4/25/1974') = }")   # (1974, 4, 25)
    print(f"{parseMDY('1755') = }")        # (1755, 0, 0)

    # Test yearsBetween
    print(f"{yearsBetween((1900, 6, 1), (1935, 5, 31)) = }")  # 34
    print(f"{yearsBetween((1900, 6, 1), (1935, 6, 1)) = }")   # 35
    print(f"{yearsBetween((1900, 6, 1), (1936, 5, 31)) = }")  # 35


# This program may be used as a module too
if __name__ == "__main__":
    main()

