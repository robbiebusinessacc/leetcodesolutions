class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        return[A for(A,B)in Counter(arr).items()if B==1][k-1]if len([A for(A,B)in Counter(arr).items()if B==1])>=k else''
        
