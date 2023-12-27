#  Ascending Way Selection Sort
def SelectionSort(list1):
    # Condition for finding the minimum
    for i in range(len(list1)):
        list1_min = list1[i]
        for j in range(i+1 , len(list1)):
            if list1_min > list1[j]:
                   list1_min = list1[j]
        
        # Finding the Index of the Minimum at each iteration
        min_index = list1.index(list1_min , i)
        if list1[i] != list1[min_index]:
            #  Swapping the minimum at each iteration
            list1[i] , list1[min_index] = list1[min_index] , list1[i]
    print(list1)   

list1 = []
n = int(input('Enter the size of the array'))
for i in range(0,n):
     print('Number at index',i)
     f = int(input())
     list1.append(f)

SelectionSort(list1)  
        