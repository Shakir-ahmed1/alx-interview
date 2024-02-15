#!/usr/bin/python3
""" prime game implimentation """


def count_primes(n):
    """ generates prime numbers"""
    prime = [True for _ in range(n + 1)]
    # Mark 0 and 1 as not prime
    prime[0] = prime[1] = False
    # Loop from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If i is prime, mark all its multiples as not prime
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    # Return the number of True values in the array
    return sum(prime)


def isWinner(x, nums):
    """ determines who is the winner in the prime game"""
    maria = 0
    ben = 0
    for n in nums:
        primes = count_primes(n)
        if primes % 2 == 1:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return "Maria"
    elif maria < ben:
        return "Ben"
    else:
        return None