# the first part of this creates a dictionary of the indices of each
# acceptable word it can find in the given string -- then it gets the
# word lengths by subtracting adjacent indices and appends each to the list
def sentence_words(s, ws):
  # dictionary of indexes of each word in the string
  sentence = {}
  for w in ws:
    if w not in s: continue
    sentence[s.find(w)] = w

  # get a list of the word indices in ascending order
  idxs = sorted(sentence.keys())
  l = []
  # idx = index of index in indices array, x = actual index of word in sentence
  for idx, x in enumerate(idxs):
    # if index is last item in list of indices, then this is the index of the last word
    # and the word length must be the remaining space (string length - index of start of word)
    if idx is len(idxs) - 1:
      word_length = len(s) - x
    else:
      # word length of each non-last words is the distance between two adjacent indices
      word_length = idxs[idx + 1] - x
    l.append(s[x:x + word_length])
  return l

# this approach just adds one letter at a time to a string and tests if that string is
# an accepted word in the given set -- if it is, add to the final array, clear the string,
# and move on to the next letter
def sentence_words_2(s, ws):
  l = []
  curr_word = ""
  for c in s:
    curr_word += c
    if curr_word in ws:
      l.append(curr_word)
      curr_word = ""
  return l

print(sentence_words_2("thequickbrownfox", set(['quick', 'brown', 'the', 'fox'])))
print(sentence_words_2("bedbathandbeyond", set(['bed', 'bath', 'bedbath', 'and', 'beyond'])))