#! /usr/bin/env python

def calcSqrt(x,eps):
	if x<0:
		return None
	low = 0.0
	high = max(x,1.0)
	value = 0.5*(low+high)
	while abs(value**2-x) > eps:
		if value**2 > x:
			high = value
		else:
			low = value
		value = 0.5*(low+high)
	return value

def calcSqrt2(x,eps):
	if x<0:
                return None
	value = 0.5*x
        while abs(value**2-x) > eps:
		value = 0.5*(value+x/value)
	return value

print calcSqrt(25.0,0.0001)
print calcSqrt2(25.0,0.0001)

print calcSqrt(0.5,0.0001)
print calcSqrt2(0.5,0.0001)
