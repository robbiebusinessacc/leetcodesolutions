class Solution:
    def destCity(self,paths):
        A,B=map(set,zip(*paths));return list(B - A)[0]