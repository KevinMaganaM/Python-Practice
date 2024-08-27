def binary_search(list, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(list)-1

    if high < low:
        return -1
    
    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return list.index(target)
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, high)
    

list1 = [1,3,5,10,12]

print(binary_search(list1, 10))