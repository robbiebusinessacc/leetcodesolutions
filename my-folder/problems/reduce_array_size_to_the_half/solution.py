class Solution:
    def minSetSize(self, arr: List[int]):
        min_len=len(arr)//2
        l=[]
        k=0
        for i,j in dict(sorted(dict(Counter(arr)).items(), key=lambda item: item[1],reverse=True)).items():
            l.append(i)
            k+=j
            if len(arr)-k<=min_len:
                return len(l)
