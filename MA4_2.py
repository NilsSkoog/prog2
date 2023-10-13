#!/usr/bin/env python3

#from person import Person
from numba import njit

def cpp_main(n):
	Cpp = Person(n)
	return Cpp.fib()

def py_main(n):
	if n <= 1:
		return  n
	return py_main(n - 1) + py_main(n - 2)

@njit
def numba_main(n):
	if n <= 1:
		return n
	return numba_main(n - 1) + numba_main(n - 2)


if __name__ == '__main__':
	xaxel = [i for i in range(20,31)]
	print(xaxel)
	
	"""
	print(cpp_main(n))
	print(py_main(n))
	print(numba_main(n))
	"""