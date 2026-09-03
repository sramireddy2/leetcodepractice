class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1index = {}
        for i, n in enumerate(nums1):
            nums1index[n] = i
        
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                index = nums1index[val]
                res[index] = cur
            if cur in nums1index:
                stack.append(cur)

        return res

        