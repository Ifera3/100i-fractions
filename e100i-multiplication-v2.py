#!python3

# Duplicate of d100i-multiplication.py
# except this should accept mixed numbers:

def product(f1,f2):
    # f1: tuple representing first fraction
        # a tuple with length 2 is a numerator/denominator 
        # a tuple with length 3 is a whole number/numerator/denominator
    # f2 is the same as 1
    if len(f1) == 3:
        n1 = f1[1] + (f1[0] * f1[2])
        d1 = f1[2]
    else:
        n1 = f1[0]
        d1 = f1[1]
    if len(f2) == 3:
        n2 = f2[1] + (f2[0] * f2[2])
        d2 = f2[2]
    else:
        n2 = f2[0]
        d2 = f2[1]
    num = n1 * n2
    den = d1 * d2
    return (num, den)

if __name__ == "__main__":
    assert product((1,3),(4,1,2)) == (9,6)
    assert product( (3,4) , (5,3) ) == (15,12)
    assert product( (3,1,2) , (2,1,2) ) == (35,4)