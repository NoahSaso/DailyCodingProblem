# faster
def list_prod(inp):
  ret = []
  # first multiply every number in the list together
  total = 1
  for x in inp:
    total *= x
  # then for each entry, divide the total by the value in that spot
  for x in inp:
    ret.append(int(total / x))
  return ret

# slower
def list_prod_no_div(inp):
  ret = [1 for x in inp]
  inp_length = len(inp)
  for idx, x in enumerate(inp):
    # for each item, multiply all the numbers together except the one with this index
    # (using range because all we need is the index to compare to the index in the outer loop)
    for i in range(inp_length):
      if i is not idx: ret[i] *= x
  return ret

print(list_prod([1, 2, 3, 4, 5]), list_prod([3, 2, 1]))

print(list_prod_no_div([1, 2, 3, 4, 5]), list_prod_no_div([3, 2, 1]))