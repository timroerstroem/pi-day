'''
Find pi via the probability of coprimes.

https://www.youtube.com/watch?v=RZBhSi_PwHU

'''
import numpy
import math


def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        guess = a
        largest = b
    else:
        guess = b
        largest = a

    while True:
        if largest - guess == guess:
            return guess
        elif largest - guess > guess:
            largest = largest - guess
            continue
        else:
            temp = largest - guess
            largest = guess
            guess = temp
            continue


'''
Convert input to float and then to int. It's ugly, but it allows the user to
input numbers in scientific notation.
'''
limit = numpy.int64(float(input("Highest integer to use: ")))
num = numpy.int64(float(input("Number of integers to use: ")))
numar = numpy.random.randint(1, high=limit, size=(2, num), dtype='int64')
coprime = []

for i in range(len(numar[0])):
    if gcd(numar[0][i], numar[1][i]) == 1:
        coprime.append(1)
    else:
        coprime.append(0)

prob = sum(coprime)/len(coprime)

print("Pi is approximately " + repr(math.sqrt(6/prob)))
