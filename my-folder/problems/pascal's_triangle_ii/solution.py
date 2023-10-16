class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [math.comb(rowIndex,i) for i in range(rowIndex+1)]
        '''
        currentRow=[1]
        for i_1 in range(rowIndex):
            newRow=[]
            for i_2 in range(len(currentRow)-1):
                newRow.append(currentRow[i_2]+currentRow[i_2+1])
            currentRow=[1]+newRow+[1]
        return currentRow'''