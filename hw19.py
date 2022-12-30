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

user_input = int(input('Number, please: '))
polynomial_list = polynominal (user_input)
polynomial_str = ' '.join(polynomial_list)
if len(polynomial_str)==0:
    with open ('polynominal.txt', 'w') as add_poly:
        add_poly.write(polynomial_str)
    print('Your polynominal is x = 0 and I wrote it in polynominal.txt')
else:
    with open ('polynominal.txt', 'w') as add_poly:
        add_poly.write(polynomial_str)    
    print (f'Your polynominal is {polynomial_str} and I wrote it in polynominal.txt')