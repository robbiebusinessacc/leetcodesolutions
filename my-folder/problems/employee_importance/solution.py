"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(i):
            return A[i][0] + sum(dfs(j) for j in A[i][1])
        A = {}
        for e in employees:
            A[e.id] = [e.importance, e.subordinates]
        
        return dfs(id)