class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i,j in enumerate(nums):
                product = 1
                for x,y in enumerate(nums):
                        if not (x==i):
                                product *= y
                res.append(product)
        return res
