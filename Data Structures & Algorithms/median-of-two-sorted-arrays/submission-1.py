class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        m = len(nums1)
        n = len(nums2)
        half = (m+n+1)//2
        left = 0
        right = m
        while left <= right:
            cut1 = (right + left) // 2
            cut2= half - cut1
            L1 = nums1[cut1-1] if cut1>0 else float('-inf')
            R1 = nums1[cut1] if cut1 < m else float('inf')
            L2 = nums2[cut2 - 1] if cut2> 0 else float('-inf')
            R2 = nums2[cut2] if cut2 < n else float('inf')
            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 == 1:
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                right = cut1 - 1
            else:
                left = cut1 + 1
        return 0