# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# Custom Judge:
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]

# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
      duplicate=2
      k=duplicate
      for left in range(k,len(nums)):
        #print(left)
        print("k",k)
        print("left",left)
        print("duplicate",duplicate)
        if nums[left]!=nums[k-duplicate] :
          nums[k]=nums[left] 
          print(k)
          k+=1
      print(nums)
      print(k)
      return k

obj=Solution()
nums=[1,1,2,3,3,3]
obj.removeDuplicates(nums)




# arr=[1,1,1,2,2,3]
# a=0
# for i in range(len(arr)-1):
#   k=arr[i+1]
#   if arr[i]==k:
#     print("_")
#     print("A",a)
#   else:
#     print(arr[i])
    
# print(a)'''