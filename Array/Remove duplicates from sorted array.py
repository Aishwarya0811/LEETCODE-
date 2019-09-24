
** Given a sorted array nums, remove the duplicates in-place such that 
    each element appear only once and return the new length.**



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort()
        nums.clear()
        nums.extend(a)
        return len(nums)
