class Solution:
    def average(self,salary):
        return sum(sorted(salary)[1:-1])/(len(salary)-2)