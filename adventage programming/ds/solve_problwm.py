arr = [i for i in range(1,101)]
left = 0
right = len(arr) -1
mid = (left + right) / 2
goal = 101

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

result = binary_search(arr, goal)

if result:
    print(f"Target {goal} found at index {result}")
else:
    print(f"Target {goal} not found in the list")


# lower_counter = 0
# higher_counter = 0
# lower_helper = arr[0]
# higher_helper = arr[0]

# for num in arr[1:]:
#     if num < lower_helper:
#         lower_helper = num
#         lower_counter += 1
#     elif num > higher_helper:
#         higher_helper = num
#         higher_counter += 1

# print("Lower", lower_counter)
# print("Higher", higher_counter)


# arr1 = [-2, -3, 4, -1, -2, 1, 5, -3]

