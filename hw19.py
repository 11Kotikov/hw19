# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import e
d = int(input("Input how many signs you would prefer to see after comma\
in Euler\'s number: "))
print(f'Euler\'s number, with your given accuracy {d}, is {round(e, d)}')