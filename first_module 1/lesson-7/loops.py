
# loops это цыкл

# 2 вида цикла
# while 
# for


# for i in range( 10 ,21):

# range stop -> [0; stop)
# range (stert stop) -> [start stop)
# range (start stop step )

# for i in range(20):
    # print(i, end=' ') 


# for i in range(200, 100, -2):
    # print(i, end=' ')
#
# for i in range(1, 11):
    # print(f"9 * {i} = {9 * i}")
# num = int(input('enter number - '))
# num2 = int(input('enter number - '))

# def print_mult_table(num, up_to):
#     for i in range(1, up_to + 1):
#         print(f'{num} * {i} = {num * i }')
# print_mult_table(num, num2)



new_str = ' '
for letter in 'Elbek oka is Teacher':
    print(new_str + letter.swapcase(), end = ' ')
print(new_str)