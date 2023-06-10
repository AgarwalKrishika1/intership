#maths
import math
a = 2.33
print("ceil ", math.ceil(a))
print("floor", math.floor(a))
b = -5
a = 3
print("absolute ", math.fabs(a))
print("factorial", math.factorial(a))
print("copysign", math.copysign(a,b))
print("gcd", math.gcd(a,b))
print("exponent", math.exp(2))
print("log", math.log(3,2))
print("log with base 2", math.log2(16))
print("log with base 10", math.log10(1000))
print("power 2 to 3", math.pow(2,3))
print("square root", math.sqrt(16))

a = math.pi/6
b = 5
c = 3
print("sin", math.sin(a))
print("cos", math.cos(a))
print("tan", math.tan(a))
print("hypotaneous", math.hypot(b,c))
d=30
print("value to degree", math.degrees(a))
print("value to radian", math.radians(d))

import time
print("hault for 5 seconds")
time.sleep(5)
print("time", time.gmtime())