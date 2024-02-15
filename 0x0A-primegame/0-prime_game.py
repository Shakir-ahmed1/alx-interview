#!/usr/bin/python3
""" prime game implimentation """


def memoize(f):
    """ memoization helper """
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def count_primes(n):
    """ generates prime numbers"""
    prime = [True for _ in range(n + 1)]
    prime[0] = False
    if len(prime) > 1:
        prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return sum(prime)


count_primes = memoize(count_primes)


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
