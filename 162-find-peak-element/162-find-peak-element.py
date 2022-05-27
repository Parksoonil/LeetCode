class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n, m = 0, len(nums) - 1
        
        while n <= m:
            mid = n + (m - n) // 2
            if (mid - 1 < 0 or nums[mid] > nums[mid - 1]) and (mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]):
                return mid
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                m = mid - 1
            elif mid + 1 < len(nums) or nums[mid] < nums[mid + 1]:
                n = mid + 1
        
        return n