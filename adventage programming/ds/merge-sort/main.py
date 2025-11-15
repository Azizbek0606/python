# def merge(arr,left,mid,right):
#     n1 = mid - left + 1
#     n2 = right - mid

#     L = [0] * n1
#     R = [0] * n2

#     for i in range(n1):
#         L[i] = arr[left + i]

#     for j in range(n2):
#         R[j] = arr[mid + 1 + j]


#     i = 0
#     j = 0
#     k = left


#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
    
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1

#     while j < n2:
#         arr[k] <= R[j]
#         j += 1
#         k += 1


# def mergeSort(arr,left,right):
#     if left < right:
#         mid = (left + right) // 2

#         mergeSort(arr, left, mid)
#         mergeSort(arr, mid + 1, right)
#         mergeSort(arr,left, mid, right)

# if __nameSl__ == "__main__":
#     arr = [38,27,43,10]

#     mergeSort(arr, 0, len(arr) -1)
#     for i in arr:
#         print(i, end=" ")
#     print()


# def partition(arr, low, high):
    
#     pivot = arr[high]
    
#     i = low - 1
    
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             swap(arr, i, j)
    
#     swap(arr, i + 1, high)
#     return i + 1

# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]

# def quickSort(arr, low, high):
#     if low < high:
        
#         pi = partition(arr, low, high)
        
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)

# if __name__ == "__main__":
#     arr = [10, 7, 8, 9, 1, 5]
#     n = len(arr)

#     quickSort(arr, 0, n - 1)
    
#     for val in arr:
#         print(val, end=" ")


def cycle_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
        
    return nums

print(cycle_sort([4,3,2,1]))
