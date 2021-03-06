
import math

def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = math.floor((end+start)/2)

    if len(arr) == 0:
        return -1

    while mid != end-1 or start+1 != mid:
        if(target < arr[mid]):
           end = mid
           mid = math.floor((end+start)/2)
        elif(target > arr[mid]):
           start = mid
           mid = math.floor((end+start)/2)
        else:
            return mid

    return -1