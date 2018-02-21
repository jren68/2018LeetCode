class Solution:
    def trap(self, A):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(A) <= 1: return 0
        
        left = 0
        right = len(A) - 1
        left_height = A[left]
        right_height = A[right]
        
        total = 0
        while left < right:
            if left_height < right_height:
                while left < right and A[left] <= left_height:
                    total += left_height - A[left]
                    left += 1
                left_height = A[left]
            else:
                while left < right and A[right] <= right_height:
                    total += right_height - A[right]
                    right -= 1
                right_height = A[right]
            #print('left=', left, 'right=', right, 'total=', total)
        return total
                
            