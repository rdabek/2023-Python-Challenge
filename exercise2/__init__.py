from exercise2.decorator import dec, reversecomp
from math import sin, exp, asin, log, tan, cos

print("Exercise 2a:")

print(str(dec(1, 2, '-', sin)))
print(str(dec(1, 2, '+', sin)))

print(str(dec(1, 2, '-', exp)))
print(str(dec(1, 2, '+', exp)))

try:
    print(str(dec(1, 2, '.', sin)))
except ValueError as err:
    print(err)

try:
    print(str(dec(1, 2, '.', exp)))
except ValueError as err:
    print(err)

print("Exercise 2b:")
funcList: list[callable] = [sin, asin, exp, log]
funcList2: list[callable] = [sin, tan, exp, cos, asin]

assert reversecomp(funcList, 0.5)(0.5) == 0.5
assert asin(cos(exp(tan(sin(0.5))))) == reversecomp(funcList2, 0.5)(0.5)

print("Succesfully computed everything.")

# Have func visualizing
#print(reversecomp(funcList, 0.5)(0.5))
#print(reversecomp(funcList2, 0.5)(0.5))
#print(asin(cos(exp(tan(sin(0.5))))))
