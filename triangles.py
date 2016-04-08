"""
You are given a square that has a height of n.
Count the number of triangles formed by the squares sides and diagonals.

Example

Triangles(1) = 8.

There are 4 small triangles (one at each side of the square) and 4 large ones, each consists of two small triangles.

"""

def Triangles(n):
    return str(int(round((12*pow(n,3) + 18 * (n*n) + 4 * n + pow(1,n-1) )/4)))

print Triangles(4)