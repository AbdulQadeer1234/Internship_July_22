class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for i in nums:
            for j in range(len(res)):
                res.append(res[j] + [i])
        return res
            