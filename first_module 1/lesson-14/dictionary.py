# month = {
# 'january ': 31,
# 'february ': 28,
# 'march ': 31,
# 'april ': 30,
# 'may ': 31,
# 'june ': 30,
# 'july ': 31,
# 'august ': 31,
# 'september ': 30,
# 'octobr ': 31,
# 'november ': 30,
# 'december ': 31,
# }

# print(month['july '])


# num1 = str(input('enter sentense - '))

# num2 = str(input('enter sentense - '))

# num3 = str(input('enter sentense - '))

# num4 = str(input('enter sentense - '))

# def calculator(num1, num2, num3, num4):

#     if num1 == 'add':
#         print(2 + 5)

#     elif num2 == 'subtract':
#         print(2 - 5)

#     elif num3 == 'multiply':
#         print(2 * 5)

#     elif num4 == 'divide':
#         print(2 / 5)

# calculator(num1, num2, num3, num4)

# sign = {
#     'add': '+',
#     'subtract': '-',
#     'multiply': '*',
#     'divide': '/'
# }

# def calculator(n1, n2, action):
#     return eval(f'{n1}{sign[action]}{n2}')

# print(calculator(2, 5, 'add'))

import re
def isCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


point = {1: 'aeioulnstr',
         2: 'dg',
         3: 'bcmp',
         4: 'fhvwy',
         5: 'k',
         8: 'jx',
         10: 'qz'}

points2 ={1: 'авеинорст',
          2: 'дклмпу',
          3: 'бгёья',
          4: 'йы',
          5: 'жзхцч',
          8: 'шэю',
          10: 'фщ,'}

text = input('enter a sentence - ').lower()

# if isCyrillic(text):
#     print(sum([k for i in text for k, v in point.items()if i in v]))
    
if isCyrillic(text):
    print(sum([k for i in text for k, v in points2.items()if i in v]))

print(isCyrillic(text))