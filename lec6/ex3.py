def binary_search(list, target, left = None, right = None):
    if left is None:
        left = 0
    if right is None:
        right = len(list) - 1

    if left > right:
        return -1
    
    mid = (left + right) // 2

    if list[mid] == target:
        return mid
    
    elif left <= right:
        if int(list[mid]) > int(target):
            return binary_search(list, target, left, mid - 1)
        else:
            return binary_search(list, target, mid + 1, right)
    
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr, 5))