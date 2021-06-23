class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        List = [0,0]
        for i in range(0,len(nums)-1):
            num1 = nums[i]
            for j in range(i+1,len(nums)):
                 if num1 + nums[j] == target:
                        List[0] = i
                        List[1] = j
        return(List)