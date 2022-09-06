class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[[1]]
        for i in range(numRows-1):
            s=a[-1]
            z=[1]
            for i in range(len(s)-1):
                z.append(s[i]+s[i+1])
            z.append(1)
            a.append(z)
        return a