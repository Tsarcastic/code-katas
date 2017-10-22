"""Kata: List Filtering

Best Practice Solution by clawtros and others


def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]"""


def filter_list(l):
  'return a new list with the strings filtered out'
  new_list = []
  for i in l:
    if type(i) is int:
        new_list.append(i)
  return new_list
          