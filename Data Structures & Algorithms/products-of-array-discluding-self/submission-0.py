class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resArr=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            resArr[i]=prefix
            prefix*=nums[i]
        
        postfix=1

        for i in range(len(nums)-1, -1,-1):
            resArr[i]*=postfix
            postfix*=nums[i]

        return resArr