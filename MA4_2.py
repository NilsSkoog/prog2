#!/usr/bin/env python3

from person import Person
from numba import njit

def cpp_main(n):
	Cpp = Person(n)
	return Cpp.fib()

def py_main(n):
	if n <= 1:
		return  n
	return py_main(n-1) + py_main(n-2)


if __name__ == '__main__':
	print(py_main(5))
