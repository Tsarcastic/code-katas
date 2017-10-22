"""Kata: Sum of the firth nth term of Series"""

def series_sum(n):
    divide_by = 1.00
    tally = 0
    while n > 0:
        tally += (1 / divide_by)
        divide_by += 3
        n -= 1
    return str(format(tally, '.2f'))

print(series_sum(1))
