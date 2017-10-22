"""Kata: Sum of all the multiples of 3 or 5
Best practice by daddepledge & nickmariner


def find(n):
    return sum(e for e in range(1, n+1) if e % 3 == 0 or e % 5 == 0)
"""


def find(n):
    sum = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i# Code here
    return sum