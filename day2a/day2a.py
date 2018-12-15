import sys

index = {}

word_list = sys.stdin.readlines()
word_length = len(word_list[0])

def main():
  for word in word_list:
    if "_" in word:
      print("ERROR: '_' symbol used in word set.")
      return
    for match_place in range(word_length):
      test_word = word[:match_place] + "_" + word[match_place+1:] 
      if test_word in index:
        print("match found:",test_word[:match_place] + test_word[match_place+1:])
        return    
      index[test_word] = word

 
main()
