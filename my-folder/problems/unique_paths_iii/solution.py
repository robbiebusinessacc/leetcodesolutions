H=range
E=len
class Solution:
	ans=0
	def findPathNum(C,i,j,grid,curLen,pLen):
		D=pLen;B=curLen;A=grid
		if A[i][j]==2:
			if D-1==B:C.ans+=1
			return
		elif A[i][j]==-1:return
		B+=1;A[i][j]=-1
		if i-1>=0:C.findPathNum(i-1,j,A,B,D)
		if j-1>=0:C.findPathNum(i,j-1,A,B,D)
		if i+1<E(A):C.findPathNum(i+1,j,A,B,D)
		if j+1<E(A[0]):C.findPathNum(i,j+1,A,B,D)
		A[i][j]=0
	def uniquePathsIII(F,grid):
		A=grid;G=0;B=0,0
		for C in H(E(A)):
			for D in H(E(A[0])):
				if A[C][D]!=-1:
					G+=1
					if A[C][D]==1:B=C,D
		F.findPathNum(B[0],B[1],A,0,G);return F.ans