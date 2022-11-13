
import math

 #define a function to do integration of f(x) btw. a and b:
def Integral(n, a, b):
    dx = (b - a) / n
    intgr = 0.0
    for i in range(1, n):

      intgr = intgr + dx * abs(math.sin(dx*(i+1/2)+a))

    return intgr