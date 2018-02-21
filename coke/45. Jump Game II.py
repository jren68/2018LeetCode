class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        step = 0
        back_pointer = 0 
        front_pointer = back_pointer
        n = len(nums)
        for i in range(len(nums)):
            if i > back_pointer:
                back_pointer = front_pointer
                step += 1
                
            front_pointer = max([front_pointer, nums[i] + i])
            if front_pointer >= n - 1:
                return step + 1
        return -1