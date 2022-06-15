class Solution:
	def nearestValidPoint(self,x,y,points):
		ans=min([[a,b]for(a,b)in points if a==x or b==y],key=lambda t:abs(t[0]-x)+abs(t[1]-y),default=None);return points.index(ans)if ans else-1