def quicksort(array):
    length=len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()
        items_greater = []
        items_lower = []
        for item in array:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)
print(quicksort([8,6,3,7,2,10]))
