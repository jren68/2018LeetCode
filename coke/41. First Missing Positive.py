class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            self.fix(nums, i)           
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
 
    def fix(self, nums, i):
        if nums[i] < 0 or nums[i] >= len(nums) or nums[i] == i + 1 : #cannot fix or already good
            return True # 
        val = nums[i]
        nums[val-1], nums[i] = nums[i], nums[val-1]
        if nums[i] != i + 1 and nums[i] != nums[val-1]:
            self.fix(nums, i)
        