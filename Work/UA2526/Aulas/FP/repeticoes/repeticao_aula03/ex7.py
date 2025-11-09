def tax(r):
    if r <= 1000:
        return 0.1 * r
    elif 1000 < r <= 2000:
        return 0.2 *r - 100
    else:
        return 0.3 * r - 300

print('Para 800 €: ', tax(800))
print('Para 1500 €: ', tax(1500))
print('Para 3000 €: ', tax(3000))