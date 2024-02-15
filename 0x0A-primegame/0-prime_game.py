#!/usr/bin/python3
""" prime game implimentation """


def get_primes(limit):
    """ generates prime numbers"""
    primes = []
    for number in range(2, limit + 1):
        temp = []
        for num in range(2, number):
            if (number % num == 0):
                temp.append(number)
        if len(temp) == 0:
            primes.append(number)
    return primes


def isWinner(x, nums):
    """ determines who is the winner in the prime game"""
    players = ['Maria', 'Ben']
    results = [0, 0]
    rounds = 0
    for n in nums:
        if rounds == x:
            break
        rounds += 1
        primes = get_primes(n + 1)
        index = (len(primes)) % 2
        results[index] += 1

    if results[0] > results[1]:
        return players[0]
    elif results[0] < results[1]:
        return players[1]
    else:
        return None

print((get_primes(3)))