#! /usr/bin/env python
import time

def fibonacciR(n):
	if n<1:
		return None
	elif n==1 or n==2:
		return 1
	else:
		return fibonacciR(n-1)+fibonacciR(n-2)

def fibonacciI(n):
	if n<1:
		return None
        else:
		a = 1
		b = 1
		value = 1
		for i in range(2,n):
			value = a+b
			a = b
			b = value
		return value
		

index = 25

start = time.time()
value = fibonacciR(index)
end = time.time()
print value, end-start

start = time.time()
value = fibonacciI(index)
end = time.time()
print value, end-start

