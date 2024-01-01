#  Implementing Stacks using lists

def merge_sort(arr):
    if len(arr)>1:

        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    
#  Recursion - already sorted the left and right subarrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0 # merged array index 
# Now sort the left sub array with the right sub array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i=+1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1

#  For elements which is not sorted 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1



arr = [12,-563,-3,2,2,-3,1,3,-4]    
merge_sort(arr)
print(arr)