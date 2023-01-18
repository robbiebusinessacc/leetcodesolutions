class Solution:
    def maxSubarraySumCircular(self, A):
        S = sum(A)
        ans1, cur = A[0], A[0]
        for x in A[1:]:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)
        ans2, cur = A[0], A[0]
        for x in A[1:]:
            cur = x + min(cur, 0)
            ans2 = min(ans2, cur)                    
        return max(ans1, S - ans2) if ans1 > 0 else ans1