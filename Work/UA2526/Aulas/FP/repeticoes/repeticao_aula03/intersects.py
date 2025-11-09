"""
Considere que a, b são os extremos de um intervalo real [a, b[
e que c, d são os extremos de outro intervalo [c, d[.

Complete a definição da função abaixo para verificar
se os intervalos se itersectam.
Admita que a < b e c < d.
"""
def intersects(a, b, c, d):
    if b > c and d > a:
        return True
    return False


def testIntersects(a, b, c, d, expected):
    """Call intersects, print result and check against expected result."""
    print(f"intersects({a}, {b}, {c}, {d})", end=" ")

    result = intersects(a, b, c, d)  # <-- Chamada à função!

    check = "OK" if result == expected else "FAIL"
    print(f"--> {result}    {check}")


def main():
    testIntersects(1, 6, 4, 8,  True)
    testIntersects(1, 6, 3, 5,  True)
    testIntersects(1, 6, 7, 8,  False)
    # Acrescente mais casos de teste...
    testIntersects(2, 5, 3, 10, True)
    testIntersects(-5, 2, -3, -1, True)
    testIntersects(6, 8, 1, 4, False)


main()

