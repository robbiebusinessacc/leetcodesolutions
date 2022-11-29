class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet=' abcdefghijklmnopqrstuvwxyz'
        newKey=' '
        for i in key:
            if i not in newKey:newKey+=i
        return (''.join(alphabet[newKey.index(i)]for i in message))