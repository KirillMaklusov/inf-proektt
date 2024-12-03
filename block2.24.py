from math import sqrt, sin
a = int(input("Введите число: "))
x = int(input("Введите число x: "))
# print(f"sqrt(2 * a) + sin(abs(3 * a)) / 3,56 = {sqrt(2 * a) + \
#                                                  sin(abs(3 * a)) / 3.56}")
print(f"sin(3.2 + sqrt(1 - x) / abs(5 * x)) = {sin(3.2 + sqrt(1 + x) / abs(5 * x)) }")
