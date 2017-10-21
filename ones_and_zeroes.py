def binary_array_to_number(arr):
  # your code
  tote = 0
  if arr[0] == 1:
      tote += 8
  if arr[1] == 1:
      tote += 4
  if arr[2] == 1:
      tote += 2
  if arr[3] == 1:
      tote += 1
  return tote
