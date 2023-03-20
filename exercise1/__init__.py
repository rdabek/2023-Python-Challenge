from exercise1.real import real
from exercise1.complex import complex

a = real()
b = real()
a.re = 2
b.re = 3

c = complex()
d = complex()
c.re = 4
c.im = 2
d.re = 3
d.im = 3

e = complex()
f = complex()
e.re = 1
e.im = 1
f.re = 3
f.im = 3

print("Exercise 1:")
print("Is a < b? Ans: " + str(a.isLower(b)))
print("Is c < d? Ans: " + str(c.isLower(d)))
print("Is e < f? Ans: " + str(e.isLower(f)))