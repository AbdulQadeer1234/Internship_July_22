class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=bin(x).replace('b','0')
        b=bin(y).replace('b','0')
        count=0
        m=max(len(a),len(b))
        if(len(a)<len(b)):
            for i in range(m-len(a)):
                a='0'+a
        else:
            for i in range(m-len(b)):
                b='0'+b
        for i in range(len(a)):
            if(a[i]!=b[i]):
                count+=1
        return count
        