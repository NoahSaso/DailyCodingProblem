def longest_substr(s, k):
  # array of all substrings of max length k unique characters
  substrs = []
  for idx, c in enumerate(s):
    curr_chars = [c]
    # iterate over all letters in string after current one
    for idx2, c2 in enumerate(s[idx + 1:]):
      # if next letter exists in current letters, fine to let in because not unique
      # converting list to set strips all unique items, so if length of unique items
      # in current substring list is still less than accepted 'k' value, allow in new
      # unique character
      if c2 in curr_chars or len(set(curr_chars)) < k:
        curr_chars.append(c2)
      else:
        # if unique character length is satisifed (len(set) == k) and new letter,
        # don't add letter and instead add substring to all substring array
        substrs.append("".join(curr_chars))
        break
      # if this is last letter in string, add substring to all substring array and stop
      if idx2 is len(s[idx + 1:]) - 1:
        substrs.append("".join(curr_chars))
        break
  # find longest substring and return
  longest = ""
  for substr in substrs:
    if len(longest) < len(substr): longest = substr
  return longest

print(longest_substr("abcba", 2) is 'bcb')
print(longest_substr("bbbbbcba", 2) is 'bbbbbcb')
