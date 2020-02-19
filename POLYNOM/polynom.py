x6 = int(input("x6:"))
x5 = int(input("X5:"))
x4 = int(input("x4:"))
x3 = int(input("X3:"))
x2 = int(input("x2:"))
x1 = int(input("x1:"))
x0 = int(input("x0:"))

d = int(input("delitel:"))

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

if sx0 == 0:
    print("yes")
    print(sx0)
else:
    print("no")
    print(sx0)

