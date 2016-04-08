"""
Note: there is a much more mathematical and efficient way to do this, I DO NOT know maths 
For roots = [2, -3, 4], the output should be
vietasFormulas(roots) = [1, -3, -10, 24].

The polynomial would thus be (x - 2)(x + 3)(x - 4) = x3 - 3x2 - 10x + 24.
"""


def vietasFormulas(r):
    r = map(lambda x: x*-1,r)
    d = []
    z = []
    for p in r:
        d.append({1:1,0:p}) 
    while len(d)>1:
        d.append(mult(d.pop(0),d.pop(0)))

    d = d[0]
    for x in d:
        print x,d[x]
        z.append(d[x])
    z.reverse()
    return z



def mult(a,b):
    r = {}
    for i in a:
        for j in b:
            n = i+j
            if n in r:
                r[n]+= a[i]*b[j]
            else:
                r[n]= a[i]*b[j]
    print r
    return r
    
#roots = [1,2,3,4]
roots = [2, -3, 4]
#roots = [5,-5]
#roots = [8, -4, 1, 6, -27, 26, 4, -3]
#roots = [-29, 29, 18, -23, 24, 0]
print vietasFormulas(roots)