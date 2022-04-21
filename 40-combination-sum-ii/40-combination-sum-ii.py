class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ret)
        return ret
    def dfs(self, nums, target, index, path, ret):
        
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            
            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], ret)