#!/usr/bin/python3

import sys

freq = 0
seen = {0}
found = False

freq_changes = sys.stdin.readlines()



while not found:
  for line in freq_changes:
    freq += int(line)
    if freq in seen:
      print("Duplicate frequency:", freq)
      found = True
      break
    else:
      seen.add(freq)

 

