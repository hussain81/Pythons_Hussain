import math
pi = math.pi

def Cos(x):
  y = math.cos(x)
  return y

def area(radius):
  return pi*radius**2

def volsph(radius):
  return 4.0*pi*radius**3/3.0

print (area(4),Cos(pi/3))
