# hours = int(input('enter hours - '))
# minutes = int(input ('enter minutes - '))
# delta = int(input('enter delta - '))
# newhour = int(hours + delta)%24

# if newhour < 10:
#     newhour = '0' + str(newhour)
# if minutes < 10:
#     minutes = '0' + str(minutes)
# print(f'{newhour} : {minutes}')

apartment = int(input('enter number of apartment - '))
floors = int(input('enter number of floor - '))
total = int(input('enter total number - '))

if apartment <= 0:
    print('erroraas')
elif apartment > total:
    print('erroe')
elif floors <= 0:
    print('erroe')
elif total % floors !=0:
    print('erroe')
else:
    a = apartment / (total / floors) + 0.49
    print('you are living on the ' + str(round(a)) + ' ' + 'floor')



