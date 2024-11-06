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


test_case1 = ["open browser", "navigate to page", "fill form"]
test_case2 = ["open browser", "navigate to page", "click login"]
test_case3 = ["open browser", "navigate to page", "click login"]
scenarios = {
    'my_test_case1': frozenset(test_case1),
    'my_test_case2': frozenset(test_case2),
    'my_test_case3': frozenset(test_case3)
}
def check_scenario_exists(name):
    if name in scenarios:
        print(f'{name} exists.')
        print("Steps:", list(scenarios[name]))
    else:
        print(f'{name} is new.')
name_input = str(input("Enter the name of the test case to check: "))
check_scenario_exists(name_input)
