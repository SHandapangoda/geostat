import numpy as np
import math 


h = []
x = math.pow(10,-11)
y = math.pow(10,24)
z = math.pow(10,3)
G = 6.67 * x
M = 5.97 * y
R = 6.371 * z
pi = 22 / 7
T = []
m = 100
r = 0 
# range of height with time 
for T in range(24):

    h = math.pow((G * M * math.pow(T*60*60,2) / 4 * math.pow(pi,2)),1/3) - R
    print("Height @ ",T*60*60,"s ",h/1000,"km")

print("Hours taken :",T+1)


