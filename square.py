"""
In this problem, you are given a number n. Your task is to return the sum of the first 1000 decimal places of the square root of n.

Example

sum_decimal(2) = 4482

The square root of 2 equals 1.4142135623....., so the answer is calculated as 4 + 1 + 4 + 2 + 1 + ..., 1000 digits altogether. This sum equals 4482.

"""

#too lazy to found another cool way to do this
import decimal
decimal.getcontext().prec = 1010


def sum_decimal(n):
    q, = decimal.Decimal(n).sqrt()
    c = 0
    p = str(d).split(".")
    if len(p) == 1: 
        return 0    
    
    for x in p[1][:1000]:
        #if b:
        #    if i < 1000:
                c+=int(x)
        #    i+=1        
    return c

print sum_decimal(10000)