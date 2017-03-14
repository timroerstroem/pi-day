'''
Find pi via the probability of coprimes.

https://www.youtube.com/watch?v=RZBhSi_PwHU

'''
import random
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


limit = input("Enter highest number to be used: ")
numbers = [random.sample(range(limit), 10000), random.sample(range(limit),
           10000)]
numar = numpy.array(numbers)+1
coprime = []

for i in len(numar[0]):
    if gcd(numar[0][i], numar[1][i]) == 1:
        coprime.append(1)
    else:
        coprime.append(0)

prob = sum(coprime)/len(coprime)

print("Pi is approximately " + math.sqrt(6/prob))
