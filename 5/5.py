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
      for j in range(1,3):
        if get_mode(intcode[i],j) == 0:
          param[j] = intcode[ intcode[i+j] ]
        elif get_mode(intcode[i],j) == 1:
          param[j] = intcode[i+j]
#    elif intcode[i] in [3,4]:
#      if get_mode(intcode[i],1) == 0:
#        param[1] = intcode[ intcode[i+1] ]
#      elif get_mode(intcode[i],1) == 1:
#        param[1] = intcode[i+1]

    if _intcode==1:
      #intcode[ intcode[i+3] ] = intcode[ intcode[i+1] ] + intcode[ intcode[i+2] ]
      intcode[ intcode[i+3] ] = param[1] + param[2]
      i += 4
    elif _intcode==2:
      #intcode[ intcode[i+3] ] = intcode[ intcode[i+1] ] * intcode[ intcode[i+2] ]
      intcode[ intcode[i+3] ] = param[1] * param[2]
      i += 4
    elif _intcode==3:
      intcode[ intcode[i+1] ] = input('provide input: ')
      #param[1] = input('provide input: ')
      i += 2
    elif _intcode==4:
      #print( param[1] )
      print( intcode[ intcode[i+1] ] )
      i += 2
    elif _intcode==5:
      if param[1]==0:
        i += 2
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

intcode = [3,9,8,9,10,9,4,9,99,-1,8]
#intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
output = run_intcode(intcode)
#print(output)
