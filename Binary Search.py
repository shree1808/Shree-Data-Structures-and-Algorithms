
def BinarySearch(new_list , key):
    min = 0
    max = len(new_list) - 1
    middle_element = (min + max) // 2
    Found = False
    while min<=max and not Found:
            middle_element = (min + max) // 2   
            if  key == new_list[middle_element] :
                Found = True
            elif key > new_list[middle_element]: # Searching on the Right Sub-list.
                min  = middle_element + 1
            else:                                # Searching on the Left Sub-list. 
                max = middle_element - 1

    if Found == True:
         print('Object Found')
    else:
        print('Object Not Found')

new_list = []
# User defined list
n = int(input('Enter the Array Size'))
for i in range (0 , n):
     print('Number at Index',i,)
     item = int(input())
     new_list.append(item)

new_list.sort()
print(new_list)
key = int(input('Enter the key'))

BinarySearch(new_list ,key)