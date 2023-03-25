from exercise3.decorator import count
from math import sin, cos

print("Exercise 3:")

print("Decorator with sin:")
f = count(sin)
print(f(0.1))
print(f(0.2))

print("Decorator with cos:")
f = count(cos)
print(f(0.1))
print(f(0.2))