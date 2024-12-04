################    task1    #####################
def bubble_sort_ascending(unsorted_list):
    n = len(unsorted_list)
    def _swap(unsorted_list, i, j):
        unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                _swap(unsorted_list, j, j + 1)
    return unsorted_list

def bubble_sort_descending(unsorted_list):
    n = len(unsorted_list)
    def _swap(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]
    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] < unsorted_list[j + 1]:
                _swap(unsorted_list, j, j + 1)
    return unsorted_list

def bubble_sort_early_stop(unsorted_list):
    n = len(unsorted_list)
    def _swap(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]
    for i in range(n):
        is_sorted = True
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                _swap(unsorted_list, j, j + 1)
                is_sorted = False
        if is_sorted:
            break
    return unsorted_list

def test_bubble_sort():
    assert bubble_sort_ascending([]) == []
    assert bubble_sort_ascending([5]) == [5]
    assert bubble_sort_ascending([3,1,2]) == [1,2,3]
    assert bubble_sort_descending([3,1,2]) == [3,2,1]
    assert bubble_sort_early_stop([1,2,3]) == [1,2,3]

test_bubble_sort()


# ################   task2    #####################
def square(n):
    return n * n

def cached_square(n, cache={}):
    if n in cache:
        print("Taken from cache:")
        return cache[n]
    else:
        print("Calculating result:")
        result = square(n)
        cache[n] = result
        return result

print(cached_square(4))
print(cached_square(4))
print(cached_square(5))
print(cached_square(5))


################   task3    #####################
steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"]

scenario_1 = frozenset(steps_1)
scenario_2 = frozenset(steps_2)
scenario_3 = frozenset(steps_3)

total_scenarios = {"Test Case 1": scenario_1, "Test Case 2": scenario_2, "Test Case 3": scenario_3, }
new_steps = ["open browser", "navigate to page", "fill form"]

def check_scenario(test_name, new_steps, existing_scenarios):
    steps_set = frozenset(
        new_steps)  # Convert new steps list to frozenset to ensure immutability and facilitate comparison

    if test_name in existing_scenarios:
        # If the test name is in the dictionary, check if the steps match
        if existing_scenarios[test_name] == steps_set:
            print(f"Scenario '{test_name}' already exists with the same steps.")
        else:
            print(f"Scenario '{test_name}' exists, but with different steps.")
    else:
        # If the test name is not in the dictionary, it does not exist
        print(f"Scenario '{test_name}' does not exist.")

def test_scenario_check():
    check_scenario("Test Case 1", ["open browser", "navigate to page", "click login"], total_scenarios)
    check_scenario("Test Case 2", ["open browser", "navigate to page", "fill form"], total_scenarios)
    check_scenario("Test Case 3", ["open browser", "navigate to page", "fill form"], total_scenarios)
    check_scenario("Test Case 4", ["open browser", "click on settings"], total_scenarios)
test_scenario_check()
