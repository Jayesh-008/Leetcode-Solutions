class Solution(object):
    def runningSum(self, nums):
        a = []
        n = len(nums)
        for i in range(0,n):
            a.append(nums[i])
            nums[i] = sum(a)
        return nums
            


        