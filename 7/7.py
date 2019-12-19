def get_digit(number, n):
  return number // 10**n % 10

def get_mode(value, nparam):
  return get_digit(value, nparam+1)

def run_intcode(_intcode,input_sequence=None):
  intcode = _intcode.copy()
  i = 0
  output = []
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
      intcode[ intcode[i+3] ] = param[1] + param[2]
      i += 4
    elif _intcode==2:
      intcode[ intcode[i+3] ] = param[1] * param[2]
      i += 4
    elif _intcode==3:
      if not input_sequence:
        input_signal = int(input('provide input: '))
      else:
        input_signal = next(input_sequence)
      intcode[ intcode[i+1] ] = input_signal
      input_signal = None
      i += 2
    elif _intcode==4:
      print( param[1] )
      output = param[1]
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
      return output
    else:
      print(f'error at step {i} ({intcode[i]})!!!')
      break

import numpy as np
from itertools import permutations
intcode = np.genfromtxt('input.txt',delimiter=',',dtype=int)

#intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#phase_setting = [4,3,2,1,0]

#intcode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#intcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

signal_to_thruster = {}
for phase_setting in permutations(range(5), 5):
  input_signal = 0
  for amp in range(5):
#    print('Start machine ',amp)
    input_signal = run_intcode(intcode, iter([phase_setting[amp],input_signal]))
  signal_to_thruster[ phase_setting ] = input_signal

max_signal = max(signal_to_thruster.values())

for phase_setting, signal in signal_to_thruster.items():
  if signal==max_signal:
    print(f'maximal signal ({max_signal}) for phase setting sequence {phase_setting}')
