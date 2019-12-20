with open('input.txt') as f:
  data = f.readlines()[0].split()[0]

ncols = 25
nrows = 6
imsize = ncols*nrows

layers = []
for ind in range(0, len(data), imsize)[:-1]:
  layers.append( data[ind:ind+imsize] )

digit_frequency = {}
for l in layers:
  digit_frequency[l] = {}
  for i in range(3):
    digit_frequency[l][i] = l.count( str(i) )

min_zeros = imsize
nones = 0
ntwos = 0
for d in digit_frequency.values():
  if d[0] < min_zeros:
    min_zeros = d[0]
    nones = d[1]
    ntwos = d[2]

print(f'Fewest 0s: {min_zeros}, 1s = {nones}, 2s = {ntwos}, 1sX2s = {nones*ntwos}')

pixel_tower = []
for i in range(imsize):
  pixel_tower.append( [] )
  for l in layers:
    pixel_tower[i].append( int(l[i]) ) 

final_image = []
for t in pixel_tower:
  final_image.append(0)
  for p in t:
    final_image[-1] = p
    if p != 2:
      break

import numpy as np
from matplotlib import pyplot as plt
final_image = np.array(final_image)
final_image = final_image.reshape( nrows, ncols )
print(final_image)
plt.imshow(final_image)
plt.savefig('img.png')
plt.show()
