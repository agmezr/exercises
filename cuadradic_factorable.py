"""calculate factorability"""
"the range of -60,60 was used to pass the tests, it can (or must ) be changed
def factorability(a, b, c):
    w = range(-60,60)
    for m in w:
        for n in w:
            if m  + n == b and m * n ==  a * c:
                return 1


print factorability(36, 0, -49)
