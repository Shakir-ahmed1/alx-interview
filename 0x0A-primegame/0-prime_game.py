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
    players = ['Maria', 'Ben']
    results = [0, 0]
    rounds = 0
    for n in nums:
        if rounds == x:
            break
        rounds += 1
        index = (count_primes(n) + 1) % 2
        results[index] += 1

    if results[0] > results[1]:
        return players[0]
    elif results[0] < results[1]:
        return players[1]
    else:
        return None
