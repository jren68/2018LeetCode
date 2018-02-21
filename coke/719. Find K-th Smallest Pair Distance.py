class Solution:
    def smallestDistancePair(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        A = sorted(A)
        left = min([(A[i] - A[i-1]) for i in range(1, len(A))])
        right = A[-1] - A[0]
        target = k
        while right > left + 1:
            mid = int((left + right)/2)
            if self.findSmallerThanVal(A,mid) < target:
                left = mid
            else:
                right = mid
        
        if self.findSmallerThanVal(A,left) >= target:
            return left
        else:
            return right
                   
        return 0
    def findSmallerThanVal(self, A, val):
        # find how many pairs in A, a sorted array, has diff larger than val
        left = 0
        total = 0
        for i in range(1, len(A)):
            while left < i and A[i] - A[left] > val:
                left += 1
            total += i - left
        return total
            
            
        