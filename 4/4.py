import numpy as np

def get_digit(number, n):
  return number // 10**n % 10

def check_number(n):
  digit = {}
  for i in range(6):
    digit[i] = get_digit(n,i)
  cons_same = False
  for i in range(5):
    if digit[i]==digit[i+1]:
      cons_same = True
      break
  if cons_same and (np.array(list(digit.values()))== np.sort(np.array(list(digit.values())))[::-1]).all():
    return True
  return False

def check_number_partTwo(n):
  digit = {}
  for i in range(6):
    digit[i] = get_digit(n,i)
  cons_same = False
  for i in range(5):
    if cons_same and digit[i]==digit[i+1]:
      cons_same = False
      continue
    if digit[i]==digit[i+1]:
      cons_same = True
      break
  if cons_same and (np.array(list(digit.values()))== np.sort(np.array(list(digit.values())))[::-1]).all():
    return True
  return False

input_range = (234208, 765869)

good_numbers = []
for n in range(*input_range):
  if check_number(n):
    good_numbers.append(n)

print(good_numbers)
print(len(good_numbers))
