class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        def searchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        left, right = searchLeft(nums, target), searchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
                