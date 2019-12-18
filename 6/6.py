import numpy as np

#data = np.genfromtxt('test.txt',delimiter=')',dtype=str)
data = np.genfromtxt('input.txt',delimiter=')',dtype=str)

print(data)

orbits = dict( zip(data[:,1],data[:,0]) )

orbited_by = {}

depth = {}

for orb in data:
  if orb[0] not in orbited_by:
    orbited_by[ orb[0] ] = [ orb[1] ]
  else:
    orbited_by[ orb[0] ].append( orb[1] )
  if orb[0]=='COM':
    depth[ orb[1] ] = 1

while len(depth)<len(data):
  print(len(depth))
  for center, orbiters in orbited_by.items():
    if center in depth:
      for orb in orbiters:
        depth[ orb ] = depth[ center ] + 1
    else:
      continue

print(sum(depth.values()))
