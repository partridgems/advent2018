import sys
import numpy
import re

def main():
  fabric = numpy.zeros((1000,1000))
  for claim in sys.stdin.readlines():
    nums = [int(x) for x in re.split(' @ |,|: |x',claim)[1:]]
    if len(nums) < 4:
      continue
    (b,l,t,r) =  (nums[0],nums[1],nums[0]+nums[2],nums[1]+nums[3])
#    print(b,t,l,r)
    fabric[b:t,l:r] += 1

  print(numpy.sum(fabric > 1))










main()
