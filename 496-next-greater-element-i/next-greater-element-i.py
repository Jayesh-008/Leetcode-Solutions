class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}

        # Build next greater element map for nums2
        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            nge[stack.pop()] = -1

        # Build result for nums1
        return [nge[num] for num in nums1]
        