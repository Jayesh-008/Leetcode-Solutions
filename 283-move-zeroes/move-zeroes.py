class Solution(object):
    def moveZeroes(self, nums):
        a = []
        b = []
        for i in nums:
            if i in nums:
                if i == 0:
                    a.append(i)
                else:
                    b.append(i)
        nums[:] = b+a
        
          

        
        