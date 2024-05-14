import random

num = int(input())

def simnum(num):
    j = 0
    if num in [0,1]:
        return 'Особое число'
    else:
        for i in range(2,num+1):
            if num%i == 0:
                j += 1
        if j == 1:
            return 'Простое число'
        else:
            return 'Составное число'

func = simnum(num)
print(func)

