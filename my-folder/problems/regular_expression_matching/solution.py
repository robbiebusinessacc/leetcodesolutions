class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = re.findall(p,s)
        return ls[0] == s if ls else False



    