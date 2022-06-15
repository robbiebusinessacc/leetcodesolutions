class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        counter = 0
        for char in s:
            if char == '(':counter += 1
            if counter > 1:result += char
            if char ==')':counter -= 1       
        return result