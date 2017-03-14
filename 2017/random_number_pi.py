'''
Find pi via the probability of coprimes.

https://www.youtube.com/watch?v=RZBhSi_PwHU

'''
import numpy


def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        lo = a
        hi = b
    else:
        lo = b
        hi = a
    while True:
        if hi % lo == 0:
            return lo
        else:
            hi, lo = lo, hi % lo
            continue


'''
Convert input to float and then to int. It's ugly, but it allows the user to
input numbers in scientific notation.
'''
limit = numpy.uint64(2**63)
# numpy.int64(numpy.float64(input("Highest integer: ")))
num = numpy.uint64(5e7)
# numpy.int64(numpy.float64(input("Number of integer pairs: ")))
numar = numpy.random.randint(1, high=limit, size=(2, num), dtype='uint64')
coprime = []

for i in range(len(numar[0])):
    if gcd(numar[0][i], numar[1][i]) == 1:
        coprime.append(1)

pi = numpy.sqrt(6/(len(coprime)/num))

print("Pi is approximately " + repr(pi) + " (off by "
      + str(round((pi-numpy.pi)/numpy.pi * 100, 3)) + " %)")
