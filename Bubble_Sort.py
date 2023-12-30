#  Bubble sort in Ascending Order
def BubbleSort(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i +1]:
                nums[i] , nums[i+1] = nums[i+1] , nums[i]
    
    print(nums)

nums = []
n = int(input('Size of the Array'))
for num in range(n):
    size = int(input())
    nums.append(size)

BubbleSort(nums)
