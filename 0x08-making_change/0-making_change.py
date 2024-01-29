#!/usr/bin/python3
""" a module to make a change"""
def makeChange(coins, total):
    """ making changes """
    if total <= 0:
        return 0
    coin_count = 0
    coins.sort(reverse=True)
    for coin in coins:
        while True:
            if total == 0:
                return coin_count
            elif coin > total:
                break
            elif coin <= total and coin >= 0:
                total -= coin
                coin_count += 1

    return -1



print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))