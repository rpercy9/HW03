import math

"""
Created on Wed Apr 24 13:37:50 2019

@author: simlab
"""
"""

a=np.degrees(45)
aradians=45*np.pi/180
print(aradians)
"""

while True:
    try:
        degrees = float(input("Please enter angle: "))
        x = math.radians(degrees)
        n = v = 0
        while n < 15:
            a = math.factorial(2 * n + 1)
            v += (((-1) ** n) / a) * x ** (2 * n + 1)
            n += 1
        print(round(v, 6))
        break
    except (SyntaxError, NameError, EOFError) as error:
        print("Invalid")
