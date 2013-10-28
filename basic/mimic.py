#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  f = open(filename, 'r')
  content_file = f.read()
  f.close()

  mimic_dict = {}
  list_words = content_file.split()
  mimic_dict[''] = list_words[0]

  i = 1
  while i < len(list_words):
    if mimic_dict.get(list_words[i], []) == []:
      mimic_dict[list_words[i]] = []
    if i + 1 < len(list_words):
      mimic_dict[list_words[i]].append(list_words[i + 1])
    else:
      mimic_dict[list_words[i]].append('')
    i += 1
  return mimic_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  printed_column = 0
  for i in xrange(0, 200):
    print word,
    printed_column += len(word)
    # if printed_column >= 70:
    #   printed_column = 0
    #   print
    if isinstance(mimic_dict[word], list):
      word = random.choice(mimic_dict[word])
    else:
      word = random.choice([mimic_dict[word]])
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
