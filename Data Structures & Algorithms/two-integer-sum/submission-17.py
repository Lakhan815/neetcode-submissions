class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = list()
        for i,j in enumerate(nums):
            diff = target-j
            if((diff in nums) and (nums.index(diff)!=i)):
                return sorted([i,nums.index(diff)])
