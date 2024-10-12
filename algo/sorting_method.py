from typing import List
# selection sort

def selection_sort(arr: List):
    for i in range(len(arr)):
        minimal = i
        for j in range(i + 1, len(arr)):
            if arr[minimal] > arr[j]:
                minimal = j
        arr[minimal], arr[i] = arr[i], arr[minimal]
    return arr

arr = list(range(10,1,-1))
print(selection_sort(arr))
