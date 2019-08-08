"""
Kata: Money, Money, Money.

Best Practice Solution by clawtros and others
"""


def calculate_years(principal, interest, tax, desired):
    """Calculate the years."""
    years = 0
    p = principal
    while desired > p:
        i = p * interest
        t = i * tax
        p = p + i - t
        years += 1
    return years


print(calculate_years(1000, .1, .12, 1100))
print(calculate_years(2000, .3, .08, 1100))
print(calculate_years(1000, .01, .22, 1050))
print(calculate_years(1100, .1, .17, 1300))
