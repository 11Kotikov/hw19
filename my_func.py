from random import*
def checking_number (num_for_check):
    while num_for_check.isdigit()==False or num_for_check == '0':
        print ("it's not possitive and integer number>0, pls try again: ")
        num_for_check = input("Failure, try again:  ")
    else:
        return int(num_for_check)

def create_rand_list(num_of_el): 
    rand_list=[]
    if num_of_el == 0:
        print ("You made empty list, my congratulations, weirdo")
    else:
        for i in range(num_of_el):
            rand_list.append(random.randint(-8,8))
        return rand_list

def create_your_own_list(size_list):
    my_list = []
    for i in range(0, size_list):
        n = int(input(f"input number in element index {i}: "))
        my_list.append(n)
    return my_list

def polynominal (k):
    poly_list = []
    while k > 1:
        ratio  = randint(1,100)
        #print (ratio)
        if ratio !=0 and ratio !=1:
            poly_list.append(f'{ratio}*x^{k}')
            poly_list.append('+')
            k-=1
        
        elif ratio == 1:
            poly_list.append(f'x^{k}')
            poly_list.append('+')
            k-=1

        else:
            k-=1  
    else:
        ratio = randint(1,100)
        last_num = randint (1,100)
        #print(ratio)
        #print (last_num)
        if ratio > 1 and last_num !=0:
            poly_list.append(f'{ratio}*x + {last_num} = 0')

        elif ratio == 0 and last_num == 0:
            poly_list.append(f'= 0')  

        elif ratio == 0 and last_num >= 1:
            poly_list.append(f'{last_num} = 0')

        elif ratio == 1 and last_num == 0:
            poly_list.append(f'x = 0')

        elif ratio == 1 and last_num >= 1:
            poly_list.append(f'x + {last_num} = 0')

        else:
            poly_list.append(f'{ratio}*x = 0')

    if '= 0' in poly_list:
        poly_list.pop(poly_list.index("= 0")-1)
    elif '1 = 0' in poly_list and len(poly_list) == 1:
        return print ('What a crazy world do we live!? polynominal can\'t be TRUE, you have to run the program again')
    else:
        None
    return poly_list