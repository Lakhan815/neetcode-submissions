class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l = 0
        # r = len(nums)-1
        # mini=nums[0]
        # while(l<=r):
        #     mid = (l+r)//2
        #     if(nums[l]<nums[mid]):
        #         l=mid+1
        #         mini=nums[l]
        #     elif(nums[mid]<nums[r]):
        #         r=mid-1
        #         mini=nums[r]
        return min(nums)

        