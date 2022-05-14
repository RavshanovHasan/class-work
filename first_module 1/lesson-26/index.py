# try:
#     print(1/0)
# except:
#     print('fuck off')
# print(2)





# num1 = int(input('enter 1st number - '))
# while True:
#     try:
#         num2 = int(input('enter 2st number - '))
#         if num2 == 0: raise ZeroDivisionError('you are not able to divide by ZERO')
#     except ZeroDivisionError as error :
#         print(error)
#     else:
#         print(num1 / num2)
#         break



# with open('codes.txt', 'r', encoding='utf-8') as rf:
#     codes = []
#     for line in rf:
#         code = line.strip()
#         codes.append(int(code))

# class PinError(Exception):
#     pass
# i = 0
# while True:
#     pin = int(input('Enter your pin: '))
#     try:
#         if not(pin in codes):
#             i+=1
#             raise PinError('You have entered wrong PIN')
            
#     except PinError as err:
#         print(err)
#     else:
#         print("Success")
#         break
#     finally:
#         if i == 3:
#             print('Goodbye! Moshenyik!')




start = int(input('enter start - '))
end = int(input('enter end - '))

sum = 0
i = 0

class NotInRange(Exception):
    pass


while True:
    try:
        num = int(input(f'enter how many will number - '))
        if not(start <= num <= end):
            raise NotInRange('Enter a number from coorect diapozone - ')
    except NotInRange as err:
        print(err)
    else:
        sum = sum+  num
        i = i + 1
    finally:
        if i == 5:
            print(sum)
            break










