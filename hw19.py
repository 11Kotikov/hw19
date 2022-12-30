from math import e
from my_func import *
from random import randint
# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# d = int(input("Input how many signs you would prefer to see after comma\
# in Euler\'s number: "))
# print(f'Euler\'s number, with your given accuracy {d}, is {round(e, d)}')

# Задача 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# def prime_factors_list (n):
#     multipliers = []
#     count_mult = 0
#     i = 2
#     so_prime = n
#     while i<=n:
#         if n % i == 0:
#             multipliers.append(i)
#             n//=i
#             i = 2
#             count_mult +=1
#         else: 
#             i+=1
#     if count_mult <= 1:
#         multipliers = [1,so_prime]
#         return print(f'"{so_prime}" is a prime number, it divides only {multipliers}')
#     else:
#         multipliers.append(so_prime)
#         multipliers.insert(0,1)
#         return print (f'Your number was "{so_prime}" and its prime factors are {multipliers}')
        
# user_input = checking_number(input('Input possitive and integer number\
#  to find out its prime factors: '))
# prime_factors_list (user_input)

# Задача 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

# size_list = int(input("Please, input quantity of elements: "))
# print ("Now, input some integer numbers, don't even\
#  try to use the same ones, I'll delete it anyway  ")
# new_list = create_your_own_list(size_list)
# print (f'Your own list was: {new_list}')
# new_set = list(set(new_list))
# print (f'Now your list without the same numbers {new_set}')

# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# user_input = checking_number(input('Integer number > 0, please: '))
# polynomial_list = polynominal (user_input)
# polynomial_str = ' '.join(polynomial_list)
# if len(polynomial_str)==0:
#     with open ('polynominal.txt', 'w') as add_poly:
#         add_poly.write(polynomial_str)
#     print('Your polynominal is x = 0 and I wrote it in "polynominal.txt"')
# else:
#     with open ('polynominal.txt', 'w') as add_poly:
#         add_poly.write(polynomial_str)    
#     print (f'Your polynominal is {polynomial_str} and I wrote it in "polynominal.txt"')

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# with open ('tut_mnogochlen1.txt', 'w') as chlen1:
#     chlen1.write('5*x^3 + x^2 + 10*x + 9 = 0')
# with open ('tut_mnogochlen2.txt', 'w') as chlen2:
#     chlen2.write('3*x^3 + 2*x^2 + x = 0')

with open ('tut_mnogochlen1.txt', 'r') as chlen_sum1:
    a = chlen_sum1.readline()
c = []
# a_r = a_r[0].split('+')
# print (a_r)
for i in range(len(a)):
    a_r = a[i].replace(' ','').split('=')
    c.append(a_r)
c = [j for i in c for j in i]    
for i in range(len(c)):
    if '' in c:
        c.remove('')
print (c)

with open ('tut_mnogochlen2.txt', 'r') as chlen_sum2:
    b = chlen_sum2.readline()
d = []
for i in range(len(b)):
    b_r = b[i].replace(' ','').split('=')
    d.append(b_r)
d = [j for i in d for j in i]    
for i in range(len(d)):
    if '' in d:
        d.remove('')
print (d)




exit()

c = []
i=len(a)-1
while(i >= 0):
    if a[i].isdigit() and b[i].isdigit:
        x = int(a[i])
        y = int (b[i])
        c.append(x+y)
        print(c)
        i=i-1
    else:
        c.append(a[i])
        print(c)
        i=i-1
