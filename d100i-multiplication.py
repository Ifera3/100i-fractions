#!python3

# find the product of 2 fractions (improper or proper) that are not
# mixed numbers:

def product(n1,d1,n2,d2):
    # n1: numerator of first factor
    # d1: denominator of first factor
    num = n1 * n2
    den = d1 * d2
    return (num, den)

if __name__ == "__main__":
    assert product(3,4,1,2) == (3,8)
    assert product(5,3,1,4) == (5,12)
