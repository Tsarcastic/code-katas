def iq_test(numbers):
    count = 0
    isEven = 1
    new = numbers.split(' ')
    if int(new[0]) % 2 == 1:
        isEven *= -1
    if int(new[1]) % 2 == 1:
        isEven *= -1
    if int(new[2]) % 2 == 1:
        isEven *= -1
    for i in new:
        count += 1
        if isEven == -1:
            if int(i) % 2 == 1:
                value = count
        else:
            if int(i) % 2 != 1:
                value = count
    print(value)

iq_test('3 3 2')