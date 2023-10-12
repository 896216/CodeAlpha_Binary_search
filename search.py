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

    return -1 

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,20,23,24,79,92,64]
target = int(input())

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element {target} is found at index {result}")
else:
    print(f"Element {target} is not found in the list")
