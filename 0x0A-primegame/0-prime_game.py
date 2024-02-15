#!/usr/bin/python3
""" prime game implimentation """


def get_primes(limit):
    """ generates prime numbers"""
    primes = []
    for number in range(2, limit):
        temp = []
        for num in range(2, number):
            if (number % num == 0):
                temp.append(number)
        if len(temp) == 0:
            primes.append(number)
    return primes


def isWinner(s, nums):
    """ determines who is the winner in the prime game"""
    players = ['Maria', 'Ben']
    results = [0, 0]
    index = 0
    for n in nums:
        primes = get_primes(n + 1)
        index = 0
        for p in range(n + 1):
            if primes == []:
                results[(index + 1) % 2] += 1
                break
            else:
                primes.pop(0)
                index = (index + 1) % 2
    if results[0] > results[1]:
        return players[0]
    else:
        return players[1]
