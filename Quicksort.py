# QuickSort in descending order

# define a function that takes the pivot element , left index and the right index and returns the pivot index location in the original list.

def pivotindex(list1, first_index , last_index):
    
    left = first_index +1
    right = last_index 
    pivot = list1[first_index]
    while True:
        while left< right and list1[left] <= pivot:
            left = left+ 1

        while left< right and list1[right] >= pivot:
            right = right - 1

        if left > right:
            break
        else:
            list1[left] , list1[right]  = list1[right] , list1[left]
    list1[first_index] , list1[right] = list1[right] , list1[first_index]
    return right # pivot current index location


def QuickSort(list1 , first_index , last_index):
    if first_index < last_index:

    # define a variable which stores the value of the pivot index 
        p = pivotindex(list1 , first_index , last_index)
        # Divide the array into 2sub-arrays from the pivot index
        pivotindex(list1 , first_index , p-1)
        pivotindex(list1 , p+1, last_index)


list1 = []
n = int(input('Array size'))
for i in range(n):
    f = int(input())
    list1.append(f)

QuickSort(list1 , 0 , len(list1) - 1)
print(list1)

