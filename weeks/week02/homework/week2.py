################    task1    #####################
#buble sorting Asc
# def bubble_sort_ascending(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# msort = bubble_sort_ascending([1,3,2,4])
# print(msort)
#
# ##buble sorting Desc
# def bubble_sort_descending(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# msort = bubble_sort_descending([1,3,2,4])
# print(msort)
#
#
# ##buble sorting pause
# def bubble_sort_pause(arr):
#     for i in range(len(arr)):
#         is_sorted = True
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 is_sorted = False
#         if is_sorted:
#             break
#     return arr
# msort = bubble_sort_pause([1,3,2,4])
# print(msort)
#
#
# ################   task2    #####################
# def square(n, cache={}):
#     if n in cache:
#         print("taken from cache:")
#         return cache[n]
#     else:
#         print("Calculating result:")
#         result = n * n
#         cache[n] = result
#         return result
# print(square(4))
# print(square(4))
# print(square(5))
# print(square(5))

################   task3    #####################



###65
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
x = 0
if a1%2==0:
    x+=1

if a2%2==0:
    x += 1
if a3%2==0:
    x += 1
if a4%2==0:
    x += 1
if a5%2==0:
    x += 1
print(f'{x} valores pares')

