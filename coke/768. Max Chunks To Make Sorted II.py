class Solution:
    def maxChunksToSorted(self, A):
        """
        :type arr: List[int]
        :rtype: int
        """
        check = {}
        B = [x for x in A]
        B = sorted(B)
        for i in range(len(B)):
            if B[i] not in check:
                check[B[i]] = i
        total = 0
        pt = 0
        end = 0
        duplicate_time = 0
        
        cur_num = None
        cur_dup = 0
        
        while pt < len(A):
            if pt == check[A[pt]]:
                cur_num = A[pt]
                cur_dup = 1
                total += 1
                pt += 1
            elif pt == check[A[pt]] + cur_dup:
                cur_dup += 1
                total += 1    
                pt += 1
            else:
                end = check[A[pt]]
                cur_num = A[pt]
                cur_dep = 1
                pt += 1
                while pt <= end:
                    if check[A[pt]] > end:
                        end = check[A[pt]]
                        cur_num  = A[pt]
                        cur_dup = 0
                        pt += 1
                    elif A[pt] == cur_num:
                        end += 1
                        cur_dup += 1
                        pt += 1
                    else:
                        pt += 1
                total += 1
        return total
  