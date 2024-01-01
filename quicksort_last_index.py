#  L < R
#  l[i] < P
#  r[i] > p
#  last element is the pivot element

def pivot_index(list1 , first_index , last_index):
    left = first_index
    right = last_index - 1
    pivot = list1[last_index]
    while True:
        while left<=right and list1[left] >= pivot:
            left = left +1
        while left<=right and list1[right] <= pivot:
            right = right -1
        if left > right:
            break
        else:
            list1[left] , list1[right] = list1[right] , list1[left] 
    list1[last_index] , list1[left] = list1[left] , list1[last_index]
    return left # Current pivot location 

def quicksort(list1 , first_index , last_index):
    if first_index  < last_index:
        p = pivot_index(list1 , first_index , last_index)
        #  Divide the array into 2SA from the pivot element
        pivot_index(list1 , first_index , p-1)
        pivot_index(list1 , p+1 , last_index)

list1 = [12,-3,-3,4]
n = len(list1) - 1
quicksort(list1 , 0 , n)
print(list1)
