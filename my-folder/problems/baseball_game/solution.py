class Solution:
    def calPoints(self, ops: List[str]) -> int:
        z=[]
        for op in ops:
            print(z)
            if op=='D':
                z.append(z[-1]*2)
            elif op=='C':
                z=z[:-1]
            elif '+'in op:
                z.append(z[-1]+z[-2])
            else:
                z.append(int(op))
        return sum(z)