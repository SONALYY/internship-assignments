def next_greater_element(arr, index=0):
    if index >= len(arr):
        return []
    
    next_greater = -1
    for j in range(index + 1, len(arr)):
        if arr[j] > arr[index]:
            next_greater = arr[j]
            break
    
    return [next_greater] + next_greater_element(arr, index + 1)


print(next_greater_element([6, 8, 0, 1, 3]))  
print(next_greater_element([1, 3, 2, 4]))     
print(next_greater_element([10, 20, 30, 50])) 
print(next_greater_element([50, 40, 30, 10])) 
