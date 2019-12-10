def run_intcode(_intcode):
  intcode = _intcode.copy()
  i = 0
  while i<len(intcode):
    if intcode[i]==1:
      intcode[ intcode[i+3] ] = intcode[ intcode[i+1] ] + intcode[ intcode[i+2] ]
      i += 4
    elif intcode[i]==2:
      intcode[ intcode[i+3] ] = intcode[ intcode[i+1] ] * intcode[ intcode[i+2] ]
      i += 4
    elif intcode[i]==99:
      return intcode
    else:
      #print('error!!!')
      break

import numpy as np
intcode = np.genfromtxt('input.txt',delimiter=',',dtype=int)

intcode[1] = 12
intcode[2] = 2

#intcode = [1,1,1,4,99,5,6,0,99]
output = run_intcode(intcode)
#print(output)

for noun in range(100):
  intcode[1] = noun
  for verb in range(100):
    intcode[2] = verb
    tmp = run_intcode(intcode)
    if tmp[0]==19690720:
      print(noun,verb,tmp)
      break
  if tmp[0]==19690720:
    break
