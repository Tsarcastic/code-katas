"""
Kata: Count of Positives Sum of Negatives.

Best Practice Solution by akii and others


def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
"""


def count_positives_sum_negatives(arr):
    """Count the number of positives and sums the negatives."""
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        else:
            neg += x
    if len(arr) > 1 and pos == 0 and neg == 0:
        return [0, 0]
    elif pos == 0 and neg == 0:
        return []
    return [pos, neg]
