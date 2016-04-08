"""
You are given 3 points on the Cartesian plane that form a triangle. Find the area of this triangle.

Example

TriangleCoordinates([[2, 7], [12, 7], [6, 17]]) = 50
"""

def TriangleCoordinates(n):
    (a,z),(b,m),(c,v) = n
    return 0.5 * abs(a* (m-v) + b*(v-z) + c*(z-m))


print TriangleCoordinates([[2, 7], [12, 7], [6, 17]])