#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
from matplotlib import pyplot as plt


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


def main():
	x = [i for i in range(20,31)]
	cpp_y = []
	py_y = []
	numba_y = []

	for n in x:
		start = pc()
		cpp_main(n)
		end = pc()
		cpp_y.append(end-start)
	plt.plot(x, cpp_y, label="C++")
	
	for n in x:
		start = pc()
		py_main(n)
		end = pc()
		py_y.append(end-start)
	plt.plot(x, py_y, label="Python")
	
	for n in x:
		start = pc()
		numba_main(n)
		end = pc()
		numba_y.append(end-start)
	plt.plot(x, numba_y, label="Numba")
	
	plt.xlabel("n")
	plt.ylabel("Time (s)")
	plt.legend()
	plt.savefig("Melker_GOAT.png")

if __name__ == '__main__':
	main()