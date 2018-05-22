def encode(s):
  e = []
  i = 0
  for c in s:
    # if first character, add
    if len(e) is 0:
      e.append(c)
      i = 1
    # if not first character, and last character is same as current, increment counter
    elif e[-1] is c:
      i += 1
    # if not first character and new letter, save counter and move on
    else:
      e[-1] = str(i) + e[-1]
      e.append(c)
      i = 1
  # add last character count
  e[-1] = str(i) + e[-1]
  return "".join(e)

def decode(s):
  d = ""
  i = ""
  for l in s:
    # if digit, add to current counter
    if l.isdigit():
      # add as string so "2" and then "1" would turn into 21, not 3
      i += l
    # if not digit, add letter i times (counter before letter)
    else:
      for _ in range(int(i)):
        d += l
      i = ""
  return d

print(decode(encode('AAAAAAAAAAAAAABBBBBCCDDDDDDDAAA')) == 'AAAAAAAAAAAAAABBBBBCCDDDDDDDAAA')