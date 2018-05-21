def mis_int(arr):
  # use set so that checking 'x + 1 not in s' is O(1) and not O(n)
  s = set(arr)
  # sort array so values are ascending
  arr.sort()
  for x in arr:
    # finding lowest missing positive integer, so ignore negatives
    if x < 0: continue
    # check if next larger integer exists; if it doesn't, it's the missing one
    if x + 1 not in s: return x + 1

# TODO: Constant space (already in linear time)

print(mis_int([3, 4, -1, 1]), mis_int([1, 2, 0]))
