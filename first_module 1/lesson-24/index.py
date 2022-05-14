
# ? task 1
# ! work
# n = []
# sum = 0
# def fac(n):
#     if n == 1: return 1
#     return n * fac(n - 1)   
# print(fac(5))


# ? task none
# ! but work 

# n = int(input('enter a number - '))
# v = int(input('enter a number - '))

# for i in range(n,v + 1, + 1):
#     print(i)
# for i in range(n,v - 1, - 1):
#     print(i)



# ? task 2
# ! fucking task work


# num1 = int(input('enter a number A - '))
# num2 = int(input('enter a number B - '))

# def solution(a, b):
#     if a > b: 
#         if a == b: return str(a)
#         return str(a) + ' ' + solution(a - 1, b)
#     else:
#         if a == b: return str(a)
#         return str(a) + ' ' + solution(a + 1, b)

# print(solution(num1, num2))




# ? task 3
# ! need show to elbek oka



num1 = int(input('enter a number - '))

def solution(a):
    if a  == 1: return 1
    elif a > 1 and a < 2: return 0
    else: return (a/2)
if solution(num1) == 1: print('yes')
else: print('no')
solution(num1)



