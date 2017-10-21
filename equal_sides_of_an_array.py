arr = [10, -80, 10, 10, 15, 35, 20]
n = 0
left_sum = 0
right_sum = sum(arr)

for i in arr:
    if left_sum <= right_sum:
        left_sum += arr[n]
        right_sum -= arr[n]
        n += 1

#print(n)
#print(len(arr) - 1)
print(n - 1)

#while sum(arr[:n]) < sum(arr[n:]):
   # print("Side 1 is " + str(sum(arr[:n])) + " side 2 is " + str(sum(arr[n:])))
   # n += 1
#print(n - 1)

#side1 = sum(array[:1])
#side2 = sum(array[1:])
##print(sum(array[:0]))
#Right side needs to be n + 1