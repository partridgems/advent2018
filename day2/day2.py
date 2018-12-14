import sys

twos = 0
threes = 0

def process_word(box_id):
  dic = {}
  for char in box_id:
    dic[char] = dic.get(char, 0) + 1
  return dic

for line in sys.stdin.readlines():
  word_count = process_word(line)
  has_two = False
  has_three = False
  for count in word_count.values():
    if count == 2 and not has_two:
      twos += 1
      has_two = True
    elif count == 3 and not has_three:
      threes += 1
      has_three = True
  
print(twos * threes)




