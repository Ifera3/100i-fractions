#!python3

# program to add 2 fractions
# return the sum of the 2 fractions as a tuple with numerator and
# denominator in lowest terms


def sum(n1,d1,n2,d2):
    if d1 != d2:
        n1 = n1 * d2
        n2 = n2 * d1
        d1 = d1 * d2
        d2 = d2 * d1
    n = n1 + n2
    d = d1
    for i in range(d):
        if (n % (d - i)) == 0 and (d % (d - i)) == 0:
            anser = tuple((n / (d - i), d / (d - i)))
            return anser
    else:
        return tuple((n, d))


if __name__ == "__main__":
    assert sum(1,3,2,1) == (7,3)
    assert sum(1,4,3,4) == (1,1)
    assert sum(5,2,3,5) == (31,10)
