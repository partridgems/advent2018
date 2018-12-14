import sys

freq = 0

for line in sys.stdin.readlines():

  if line[0] == '+':
    freq += int(line[1:])
  elif line[0] == '-':
    freq -= int(line[1:])
  else:
    print("Error. Invalid input")
  
print("Final frequency is", freq)

