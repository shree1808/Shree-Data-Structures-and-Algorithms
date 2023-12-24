# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution  
        low = 0 # The first idnex of the list
        high = len(nums) - 1 # the last index of the list

        while low<=high: # considering every list item
            mid = (low + high)//2 # Index of the Middle element
            if nums[mid] == target:
                return mid
            elif target < nums[mid]: # Left Sublist 
                high = mid - 1
            else:                    #  Right Sublist
                low = mid + 1
        return -1
    

