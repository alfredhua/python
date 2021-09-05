
class Solution(object):
     """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
     def twoSum(self,nums,target):
         result =[]
         for i in nums:
            for j in nums[1:]:
                print("-----i:{0}------j:{1}".format(i,j))
                if (i + j) == target:
                    result.append(nums.index(i)) 
                    result.append(nums.index(j)) 
                    return result 

class object():
    pass

print(Solution().twoSum(nums=[3,3],target=6))

