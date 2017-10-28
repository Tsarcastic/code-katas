"""Kata: Money, Money, Money

Best Practice Solution by clawtros and others


def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]"""

def calculate_years(principal, interest, tax, desired):
    years = 0
    P = principal
    while desired > P:
        I = P * interest
        T = I * tax
        P = P + I - T
        years += 1
    return years

print(calculate_years(1000, .1, .12, 1100))
print(calculate_years(2000, .3, .08, 1100))
print(calculate_years(1000, .01, .22, 1050))
print(calculate_years(1100, .1, .17, 1300))