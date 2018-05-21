def autocomplete(s, strs):
  autostrs = []
  for st in strs:
    # if given string is at beginning of any words, they are valid so add
    if s in st and st.index(s) is 0: autostrs.append(st)
  return autostrs

print(autocomplete("de", ["dog", "deer", "deal"]))