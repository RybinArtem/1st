import random

num = int(input())

def simnum(num):
    if num in [0,1]:
        return 'Особое число'
    else:
        for i in range(2,num):
            if num%i == 0:
                return 'Составное число'
        return 'Простое число'

func = simnum(num)
print(func)

