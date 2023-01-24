class Solution:
    def frequencySort(self, s: str) -> str:
        z={}
        for i in set(s):
            z[i]=s.count(i)
        sorted_dict = sorted(z.items(), key=lambda x:x[1], reverse=True)
        a=""
        for key,value in sorted_dict:
            a+=(key*value)
        return a
                