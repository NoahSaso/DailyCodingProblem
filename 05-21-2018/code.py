# very brute force
# idea for better solution: use basic math to calculate spaces that would fit
# I'll probably write this soon
def justify(words, k):
  justified = [words[0]]
  for word in words[1:]:
    current_line_length = len(justified[-1])
    # if room left in current line
    if current_line_length < k:
      added = False
      # if current length + 1 space + length of next word still allowed, add
      if current_line_length + 1 + len(word) <= k:
        justified[-1] += f" {word}"
        added = True
      # if wasn't added (word too long) or last word
      if not added or word is words[-1]:
        spaces = [i for i, l in enumerate(justified[-1]) if l == ' ']
        # if no spaces in line (one word), add spaces to end until k
        if len(spaces) == 0:
          while len(justified[-1]) < k:
            justified[-1] += ' '
        # else if more than one word, pad with spaces until reach line length
        else:
          spaces_idx = i = 0
          while len(justified[-1]) < k:
            # add 1 space to where other space is
            justified[-1] = justified[-1][:spaces[spaces_idx] + i] + ' ' + justified[-1][spaces[spaces_idx] + i:]
            # set spaces_idx to next index of a space or reset to beginning
            spaces_idx = (0 if spaces_idx == (len(spaces) - 1) else(spaces_idx + 1))
            i += 1
        # if wasn't added in previous line, move on to next line
        if not added:
          justified.append(word)
        # if last word, run spaces for single word
        if word is words[-1]:
          while len(justified[-1]) < k:
            justified[-1] += ' '

  return justified

expected = ["the  quick brown", # 1 extra space on the left
            "fox  jumps  over", # 2 extra spaces distributed evenly
            "the   lazy   dog"] # 4 extra spaces distributed evenly

print(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16) == expected)