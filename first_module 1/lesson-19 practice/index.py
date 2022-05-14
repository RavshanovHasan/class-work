
# ! fucking task work
# ? task 1 

# a = int(input('enter a number - '))
# number = open(f'{a}.txt', 'w', encoding='utf-8')

# sum = 0

# for i in range(1,11) :
#     number.write(f'{a}x{i} {a*i}\n')



# number = close()


# ! facking task work 
# ? task 2 
# student = ['hasan',  'sardor','abduvali']
# age = [18, 17, 16]

# f = open('data.txt', 'w', encoding='utf-8')

# for n in range(len(student)):
#     f.write(f'{student[n]} - {age[n]}\n')


from random import randint
from turtle import color

def generate_color():       
    red = randint(0,225)
    green = randint(0,225)
    blue = randint(0,225)
    return f'rgb{red},{green},{blue}'

def write_color(color):
    with open('colors.txt', 'a', encoding='utf-8') as file:
        file.write(f'{color}\n')
write_color(generate_color())