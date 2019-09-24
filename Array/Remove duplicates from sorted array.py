
** Given a sorted array nums, remove the duplicates in-place such that 
    each element appear only once and return the new length.**



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort()
        nums.clear()
        nums.extend(a)
        return len(nums)
    
    
# Time O(n), Space O(1)   
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
          return slow + 1
