class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return''.join([t for i,t in sorted(list(zip(indices,s)))])