class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        count=0
        for l in alphabet:
            if l in sentence:
                count+=1
        return count==26
        