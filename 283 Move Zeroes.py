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
    j=0
    for i in range(len(arr)):
      print(arr[i])
      if arr[i]!=0:
        print("new",arr[i])
        arr[j]=arr[i]
        j+=1
    for i in range(j,len(arr)):
        print("hiih")
        arr[i]=0
    return(arr)
obj=Solution()
arr=[0,1,1,0,3,12]
print(obj.moveZeroes(arr))


