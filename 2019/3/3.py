import numpy as np
from matplotlib import pyplot as plt

def compute_size(wire):
  left = 0
  right = 0
  up = 0
  down = 0
  for step in wire:
    if step.startswith('L'):
      left += int( step[1:] )
    elif step.startswith('R'):
      right += int( step[1:] )
    elif step.startswith('U'):
      up += int( step[1:] ) 
    elif step.startswith('D'):
      down += int( step[1:] )
  w = {
      'l' : left,
      'r' : right,
      'u' : up,
      'd' : down
      }
  return w

def draw_map(wire, size):
  wire_map = np.zeros( (size['l']+size['r'], size['u']+size['d']), dtype=bool )
  start_x = size['l']
  end_x = size['l']
  start_y = size['d']
  end_y = size['d']
  print('start at ',start_x,start_y)
  for step in wire:
    if step.startswith('L'):
      end_x = start_x - int( step[1:] )
    elif step.startswith('R'):
      end_x = start_x + int( step[1:] )
    elif step.startswith('U'):
      end_y = start_y + int( step[1:] )
    elif step.startswith('D'):
      end_y = start_y - int( step[1:] )
    wire_map[ min(start_x,end_x):max(start_x,end_x)+1, min(start_y,end_y):max(start_y,end_y)+1 ] = True
    start_x = end_x
    start_y = end_y
  return wire_map

def compute_steps(wire, stop):
  if stop==(0,0):
    return 0
  tmp_x = 0
  tmp_y = 0
  total_steps = 0
  for step in wire:
    for d in range(int( step[1:] )):
      total_steps += 1
      if step.startswith('L'):
        tmp_x -= 1
      elif step.startswith('R'):
        tmp_x += 1
      elif step.startswith('U'):
        tmp_y += 1
      elif step.startswith('D'):
        tmp_y -= 1
      #print((tmp_x, tmp_y), stop)
      if (tmp_x, tmp_y) == stop:
        return total_steps

wires = np.genfromtxt('input.txt',dtype=str,delimiter=',')
#wires = np.genfromtxt('test.txt',dtype=str,delimiter=',',skip_footer=2)

w1 = compute_size(wires[0])
w2 = compute_size(wires[1])
size = {
    'l' : max( w1['l'], w2['l']),# + 1,
    'r' : max( w1['r'], w2['r']) + 1,
    'u' : max( w1['u'], w2['u']) + 1,
    'd' : max( w1['d'], w2['d']),# + 1,
    }

print('size computed:',size)
wire_map1 = draw_map(wires[0],size)
wire_map2 = draw_map(wires[1],size)

print('draw maps completed')
intersections_map = wire_map1 & wire_map2

print('map intersection computed')

intersections_idx = np.where(intersections_map)
print('intersections found')

intersections_x = intersections_idx[0]-size['l']
intersections_y = intersections_idx[1]-size['d']

print('intersections_idx:', intersections_x, intersections_y)

intersections_distances = abs(intersections_x) + abs(intersections_y)

print('distances computed:', intersections_distances)
intersections_distances.sort()
print('sorted distances:', intersections_distances)

steps = {}
for i in range(2):
  steps[i] = np.zeros_like(intersections_x)
  for j,intx in enumerate(zip(intersections_x, intersections_y)):
    steps[i][j] = compute_steps(wires[i], intx)

combined_steps = np.sort(steps[0] + steps[1])
print('combined steps:', combined_steps)


#draw1 = 3*np.array(wire_map1,dtype=int)
#draw2 = np.array(wire_map2,dtype=int)
##plt.imshow( np.rot90(wire_map1 + wire_map2) )
#plt.imshow( np.rot90(draw1 + draw2) )
#plt.show()
