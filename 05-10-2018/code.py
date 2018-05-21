def length_longest_file_path(fs_s):
  paths, curr_files = [], []
  # split the file system string by newlines
  for file in fs_s.split("\n"):
    # file_level is number of tabs, because an indentation is in the next folder
    # curr_level is the most recent level based on the files we've seen already
    file_level, curr_level = (file.count("\t") + 1), len(curr_files)
    filename = file.replace("\t", '')
    # if file level is equal to current level, remove last file/folder before adding
    # (sibling in same directory)
    if file_level is curr_level:
      curr_files.pop()
    # if file level is less than current level, remove last two files because we need
    # to get out of current folder
    # (for efficiency, change above if statement from 'is' to '<=' and remove one of the
    # two 'pop()' calls below, but I wrote it this way for readability and comprehension)
    if file_level < curr_level:
      curr_files.pop()
      curr_files.pop()
    curr_files.append(filename)

    paths.append('/'.join(curr_files))
  # return length of maximum string in paths list
  return len(max(paths, key=len))

print(length_longest_file_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") is 32)