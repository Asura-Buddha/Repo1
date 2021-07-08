class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(0,len(nums)):
            tmp = nums[i]
            for j in range(i+1,len(nums)):
                if tmp == nums[j]:
                    cnt += 1
        return cnt