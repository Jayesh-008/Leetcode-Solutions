class Solution(object):
    def findDifference(self, nums1, nums2):
        a,b,c = [],[],[]
        for i in nums1:
            if i not in nums2:
                a.append(i)
        a = set(a);a = list(a);c.append(a)
        for j in nums2:
            if j not in nums1:
                b.append(j)
        b = set(b);b = list(b);c.append(b)
        return c
        
        
        
        