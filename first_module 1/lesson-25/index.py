
# def a (b, c):
#     for i in range(b):
#             for i in range(c):
#                 print(i * 2)

# def a (d):
#     for i in range(d):
#         print(i * 2)
# a(2)




# a  = [1,8,15,29,41,43,58,120,156]
# def sol(a):
#     for num in a:
#         if num == 58:   
#             print('True') 
# sol(a)




# def sol(list, num):
#     mid = 0
#     start = 0
#     end = len(list) -1 
#     step = 1

#     while start <= end:
#         print(f"syblist in  step {step} : {str(list[start:end + 1])}" )
#         step += 1

#         mid = (start + end) // 2

#         if num == list[mid]:
#             return mid
#         if num < list[mid]:
#             end = mid - 1 
#         else:
#             start = mid + 1
#     return 'error'
# print(sol([1,8,13,22,24,44,58,67,89,99,101,121,141], 300))
    



