#  Selection Sort in Descending order
def SelectionSort(list1):
    # Finding the maximum
    for i in range(len(list1)):
        max_num = list1[i]
        for j in range(i+1 , len(list1)):
            if max_num < list1[j]:
                max_num = list1[j]

    # Finding the Index of the Max
        max_index = list1.index(max_num , i)
    # Swapping the max_num at each iteration
        if list1[i] != list1[max_index] :
            list1[i] , list1[max_index] = list1[max_index] , list1[i]
    print(list1)

list1 = []
n = int(input('Enter the size of the array'))
for i in range(0,n):
     print('Number at index',i)
     f = int(input())
     list1.append(f)

SelectionSort(list1)  
        