def balanced_brackets(inp):
  # if odd number, can't be balanced
  if len(inp) % 2 is not 0: return False
  # opening brackets
  opening = set('[{(')
  s = [] # functions as a stack (last in, first out)
  for c in inp:
    # if no items in stack, add first character
    if len(s) is 0: s.append(c)
    else:
      # if character (c) is closing bracket and last item in stack is opening of same
      # style bracket, remove opening from stack
      if (s[-1] is "[" and c is "]") or (s[-1] is "{" and c is "}") or (s[-1] is "(" and c is ")"): s.pop()
      # if character is new opening, add to stack
      elif c in opening: s.append(c)
      # if character is not opening (closing) and is not paired with an opening,
      # unbalanced string (return false)
      else: return False
  # balanced if no leftover openings in stack (because all were removed due to
  # correct closing brackets)
  return len(s) is 0

print(balanced_brackets("([])[]({})") is True and balanced_brackets("([)]") is False and balanced_brackets("((()") is False)