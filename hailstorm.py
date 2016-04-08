"""
The hailstone sequence is generated from a number n by the following set of rules:

if n is even, divide it by 2 to get n/2;
if n is odd, multiply it by 3 and add 1 to get 3n + 1.
Let the length of a hailstone sequence be the number of steps it takes to reach 1.

For example, the length of the hailstone sequence starting with 6 equals 8, since the sequence is generated is follows:
6 / 3 / 10 / 5 / 16 / 8 / 4 / 2 / 1.

Given a length l, find the minimum positive integer X such that the length of the sequence starting with X equals l.

Example

For l = 8, the output should be
hailstoneLength(l) = 6.
"""

def hailstoneLength(l):
    x=1
    while True:
        if solve(x) == l:
            return x
        x+=1


def solve(n):
    l = 0
    while n>1:
        if n%2 == 0:
            n/=2
        else:
            n=3*n+1
        l+=1
    return l



print hailstoneLength(8)