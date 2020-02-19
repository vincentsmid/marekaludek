import math
from decimal import *

getcontext().prec = 10

def inputt():
    x6 = int(input("x6:"))
    x5 = int(input("X5:"))
    x4 = int(input("x4:"))
    x3 = int(input("X3:"))
    x2 = int(input("x2:"))
    x1 = int(input("x1:"))
    x0 = int(input("x0:"))
    output = [x0, x1, x2, x3, x4, x5, x6]
    return output

#-- vzorec na polynom druheho radu - kvadraticky vzorec
def qr (a, b, c):
    sqr = Decimal(math.sqrt(b*b-4*a*c))
    x = Decimal((-b + sqr)) / Decimal(2*a)
    x2 = Decimal((-b - sqr)) / Decimal(2*a)
    return x, x2

def sestirad(x0, x1, x2, x3, x4, x5, x6, d):
    dx5 = x6 * d
    sx5 = dx5 + x5
    dx4 = sx5 * d
    sx4 = dx4 + x4
    dx3 = sx4 * d
    sx3 = dx3 + x3
    dx2 = sx3 * d
    sx2 = dx2 + x2
    dx1 = sx2 * d
    sx1 = dx1 + x1
    dx0 = sx1 * d
    sx0 = dx0 + x0
    return sx0, d

factor = int(input("Zadejte kolik řádů má Váš polynom: "))

if factor == 2:
    inputt = inputt()
    outputt = qr(inputt[2], inputt[1], inputt[0])
    print(outputt)
elif factor == 6:
    input6 = inputt()
    for d in range(-10, 10):
        output6 = sestirad(input6[0], input6[1], input6[2], input6[3], input6[4], input6[5], input6[6], d)
        d += 1
        print (output6)
