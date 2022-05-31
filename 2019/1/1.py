import numpy as np

data = np.loadtxt('input.txt')
fuel_for_modules = sum(data//3 - 2)

print(fuel_for_modules)

fuel_per_module = data//3 - 2
for i in range(len(fuel_per_module)):
  tmp_fuel = fuel_per_module[i]//3 - 2
  while tmp_fuel>0:
    fuel_per_module[i] += tmp_fuel
    tmp_fuel = tmp_fuel//3 - 2

print(sum(fuel_per_module))
