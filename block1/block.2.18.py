# a)


s = 5
print(s)

s = 57
print(s)

# б)


s = 6
print(s)

s = 4
s = -5.2 * s
print(s)


s = 0
print(s)

# в)


s = -7.5
print(s)
try:
    s = 2 * s
    print(s)
except NameError as e:
    print(e)

# г)


s = 45
print(s)

s = -25
print(s)


try:
    s = s + k
    print(s)
except NameError as e:
    print(e)
