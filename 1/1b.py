import numpy as np

data = np.loadtxt('input.txt')
fuel_for_modules = sum(data//3 - 2)

print(fuel_for_modules)

fuel_for_fuel = 0
tmp_fuel = fuel_for_modules
while tmp_fuel>6:
  module_fuel = tmp_fuel//3 - 2
#  print(module_fuel)
  fuel_for_fuel += module_fuel
  tmp_fuel = module_fuel

print(fuel_for_modules + fuel_for_fuel)