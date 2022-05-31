import numpy as np

def make_chain(obj, orbits):
  next_object = orbits[obj]
  chain = [ next_object ]
  while next_object != 'COM':
    next_object = orbits[ next_object ]
    chain.append( next_object )
  return chain

#data = np.genfromtxt('test2.txt',delimiter=')',dtype=str)
data = np.genfromtxt('input.txt',delimiter=')',dtype=str)

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
  for center, orbiters in orbited_by.items():
    if center in depth:
      for orb in orbiters:
        depth[ orb ] = depth[ center ] + 1
    else:
      continue

print(sum(depth.values()))

orbits = dict( zip(data[:,1],data[:,0]) )

chain = {}
for obj in ['YOU','SAN']:
  chain[obj] = make_chain(obj,orbits)

#print(chain)

distance_to_intersection = {
  'YOU' : 0,
  'SAN' : 0
}

from itertools import permutations
for first,second in permutations(['YOU','SAN'], 2):
  for obj in chain[first]:
    if obj in chain[second]:
      break
    else:
      distance_to_intersection[first] += 1

print(distance_to_intersection, sum(distance_to_intersection.values()))
