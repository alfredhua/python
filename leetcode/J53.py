class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxNum=nums[0]
        for i in range(len(nums)):
            num = 0
            for j in range(i,len(nums)):
                num = num+ nums[j]
                maxNum =max(num,maxNum)
        
        return maxNum