class Solution(object):
    def sortArrayByParity(self, nums):
        a = []
        b = []
        for i in nums:
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)
        a.sort()
        b.sort()
        return a+b
        