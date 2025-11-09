
# isLeapYear(year) deve devolver True se year é um ano bissexto
# e False se é um ano comum.  Corrija-a.
# (See: https://en.wikipedia.org/wiki/Leap_year)
def isLeapYear(year):
    return year%4 == 0 and year%100 != 0 or year%400 == 0


# monthDays deve devolver o número de dias de um dado mês num dado ano.
# Por exemplo, monthDays(2004, 2) deve devolver 29.
# Corrija-a.
def monthDays(year, month):
    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2:
        leap_year = isLeapYear(year)
        if leap_year == True:
            days = 29
        else:
            days = 28
    else:
        days = MONTHDAYS[month]
    return days


# nextMonth deve devolver o mês seguinte ao mês (e ano) dado.
# Por exemplo, nextMonth(2016, 12) deve devolver (2017, 1).
def nextMonth(year, month):
    if month < 12:
        month += 1
    else:
        year += 1
        month = 1
    return year, month


# nextDay deve devolver o dia a seguir a uma dada data.
# Por exemplo, nextDay(2017, 1, 31) deve devolver (2017, 2, 1)
def nextDay(year, month, day):
    month_days = monthDays(year, month)
    if day < month_days:
        day += 1
    elif month < 12:
        month += 1
        day = 1
    else:
        year += 1
        month = 1
        day = 1
    return year, month, day


# Defina uma função dateIsValid que deve
# devolver True se os seus argumentos formarem uma data válida
# e devolver False no caso contrário.
# Por exemplo, dateIsValid(1980, 2, 29) deve devolver True,
# dateIsValid(1980, 2, 30) deve devolver False.
def dateIsValid(year, month, day):
    if month <= 12:
        month_days = monthDays(year, month)
        if day > month_days:
            return False
        else:
            return True
    else:
        return False


# Defina uma função previousDay que devolva o dia anterior a uma dada data.
# Por exemplo, previousDay(1980, 3, 1) deve devolver (1980, 2, 29)
def previousDay(year, month, day):
    if day != 1:
        day -= 1
    else:
        if month == 1:
            year -= 1
            day = 31
            month = 12
        else:
            month -= 1
            day = monthDays(year, month)
    return year, month, day


# Defina uma função previousMonth
# que devolva o mês anterior ao mês (e ano) dado.
# Por exemplo, previousMonth(1980, 3) deve devolver (1980, 2),
# previousMonth(1980, 1) deve devolver (1979, 12).
def previousMonth(year, month):
    if month != 1:
        month -= 1
    else:
        year -= 1
        month = 12
    return year, month

def main():
    print('2004', isLeapYear(2004), ' --> True')
    print('2003', isLeapYear(2003), ' --> False')
    print('1900', isLeapYear(1900), ' --> False')

    print('2004, 2: ', monthDays(2004, 2), ' --> 29')
    print('2017, 1: ', monthDays(2017, 1), ' --> 31')

    print('2016, 12: ', nextMonth(2016, 12), ' --> (2017, 1)')
    print('2016, 1: ', nextMonth(2016, 1), ' --> (2016, 2)')

    print('2017, 1, 31: ', nextDay(2017, 1, 31), ' --> (2017, 2, 1)')
    print('2016, 2, 28: ', nextDay(2016, 2, 28), ' --> (2016, 2, 29)')

    print('1980, 2, 29: ', dateIsValid(1980, 2, 29), ' --> True')
    print('1980, 2, 30: ', dateIsValid(1980, 2, 30), ' --> False')

    print('1980, 3, 1: ', previousDay(1980, 3, 1), ' --> (1980, 2, 29)')
    print('2002, 2, 2: ', previousDay(2002, 2, 2), ' --> (2002, 2, 1)')

    print('1980, 3: ', previousMonth(1980, 3), ' --> (1980, 2)')
    print('2080, 1: ', previousMonth(2080, 1), ' --> (2079, 12)')

if __name__ == "__main__":
    main()