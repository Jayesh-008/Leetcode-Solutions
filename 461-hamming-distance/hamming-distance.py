class Solution(object):
    def hammingDistance(self, x, y):

        count=0
        r1=bin(x)[2:]
        r2=bin(y)[2:]
        max_len=max(len(r1),len(r2))
        r1=r1.zfill(max_len)
        r2=r2.zfill(max_len)
        for i in range(len(r1)):
            if r1[i]!=r2[i]:
                count+=1
        return count
        