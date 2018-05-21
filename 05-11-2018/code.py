def max_subarr(a, k):
  # for an array of length len(a), the number of iterations to cycle through
  # every consecutive subarry of length k is len(a) - k + 1, because index
  # len(a) - k is the start of the last subarray
  for n in range(0, (len(a) - k + 1)):
    # print max integer of the subarray from n to n + k
    print(max(a[n:n+k]))

max_subarr([10, 5, 2, 7, 8, 7], 3)