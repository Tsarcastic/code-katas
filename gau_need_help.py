# Best Practice
# def f(n):
    # return sum(range(n+1))

def f(n):
    sum = 0
    if type(n) is int:
        while n > 0:
            sum += n
            n -= 1
    if sum == 0: 
        return None
    return sum