class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = []
        b = []
        c = []
        i = 0
        j = 0
        while i < m:
            a.append(nums1[i])
            i += 1
        while j < n:
            b.append(nums2[j])
            j += 1
        c = a+b
        c.sort()
        nums1[:] = c
        


        
        