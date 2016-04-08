def rewriteTheProduct(a, b, c, d):
    k = (a*a + b*b) * (c*c + d*d)
    return sorted([[i,j] for j in range(k) if j*j<k for i in range(j) if i*i + j*j == k])
    

print rewriteTheProduct(2,4,6,8)