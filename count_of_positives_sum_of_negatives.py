def count_positives_sum_negatives(arr):
    #your code here
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        else:
            neg += x
    if len(arr) > 1 and pos == 0 and neg == 0:
        return [0,0]
    elif pos == 0 and neg == 0:
        return []
    return [pos, neg]