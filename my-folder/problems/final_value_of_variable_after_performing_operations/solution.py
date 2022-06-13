class Solution:
    def finalValueAfterOperations(self,o):
        return str(o).count('--')*-1+str(o).count('++')
    
        