def calculate_years(principal, interest, tax, desired):
    years = 0
    P = principal
    while desired > P:
        I = P * interest
        T = I * tax
        P = P + I - T
        years += 1
    return years