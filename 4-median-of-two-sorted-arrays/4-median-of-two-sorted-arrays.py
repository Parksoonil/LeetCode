class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        result = 0.0
        while nums1 or nums2:
            if nums1:
                nums.append(nums1.pop())
            if nums2:
                nums.append(nums2.pop())
        nums.sort()
        if len(nums) % 2 == 1:
            result = nums[len(nums)//2]
        else:
            result = (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
        return result