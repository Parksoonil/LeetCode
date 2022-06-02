class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        idxs = sorted(range(len(nums)), key=lambda i: nums[i])  # n ≤ 2*10^4 → O(nlogn): sorting, binary search, etc might be used
        nums = [nums[idx] for idx in idxs]
        i_s, i_e = 0, 1  # two pointers
        while i_e < len(nums):
            if (diff := nums[i_e] - nums[i_s]) <= t:  # diff is always positive
                if abs(idxs[i_s] - idxs[i_e]) <= k:
                    return True
                i_e += 1   # diff should be bigger
            else:
                i_s += 1  # diff should be smaller
                i_e = i_s + 1  # back to the beginning
        return False