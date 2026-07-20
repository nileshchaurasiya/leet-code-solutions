# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# Solutions
class Solution:
  def moveZeroes(self, arr: list[int]) -> None:
    start=0
    for next in range(len(arr)):
      if arr[next]!=0:
        arr[start],arr[next]=arr[next],arr[start]
        start+=1
    return(arr)
obj=Solution()
arr=[0, 1, 0, 3, 12]
print(obj.moveZeroes(arr))