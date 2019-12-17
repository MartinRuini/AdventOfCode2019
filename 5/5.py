def get_digit(number, n):
  return number // 10**n % 10

def get_mode(value, nparam):
  return get_digit(value, nparam+1)

def run_intcode(_intcode):
  intcode = _intcode.copy()
  i = 0
  while i<len(intcode):
    _intcode = intcode[i] % 100
    param = {}
    if _intcode in [1,2,5,6,7,8]:
      nparams = 2
    elif _intcode in [4]:
      nparams = 1
    else:
      nparams = 0
    for j in range(1,nparams+1):
      if get_mode(intcode[i],j) == 0:
        param[j] = intcode[ intcode[i+j] ]
      elif get_mode(intcode[i],j) == 1:
        param[j] = intcode[i+j]

    if _intcode==1:
      #intcode[ intcode[i+3] ] = intcode[ intcode[i+1] ] + intcode[ intcode[i+2] ]
      intcode[ intcode[i+3] ] = param[1] + param[2]
      i += 4
    elif _intcode==2:
      #intcode[ intcode[i+3] ] = intcode[ intcode[i+1] ] * intcode[ intcode[i+2] ]
      intcode[ intcode[i+3] ] = param[1] * param[2]
      i += 4
    elif _intcode==3:
      intcode[ intcode[i+1] ] = int(input('provide input: '))
      #param[1] = input('provide input: ')
      i += 2
    elif _intcode==4:
      print( param[1] )
      #print( intcode[ intcode[i+1] ] )
      i += 2
    elif _intcode==5:
      if param[1]==0:
        i += 3
      else:
        i = param[2]
    elif _intcode==6:
      if param[1]==0:
        i = param[2]
      else:
        i += 3
    elif _intcode==7:
      if param[1]<param[2]:
        intcode[ intcode[i+3] ] = 1
      else:
        intcode[ intcode[i+3] ] = 0
      i += 4
    elif _intcode==8:
      if param[1]==param[2]:
        intcode[ intcode[i+3] ] = 1
      else:
        intcode[ intcode[i+3] ] = 0
      i += 4
    elif _intcode==99:
      return intcode
    else:
      print(f'error at step {i} ({intcode[i]})!!!')
      break

import numpy as np
intcode = np.genfromtxt('input.txt',delimiter=',',dtype=int)

#intcode = [3,9,7,9,10,9,4,9,99,-1,8]
#intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#intcode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
#intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
output = run_intcode(intcode)
#print(output)
