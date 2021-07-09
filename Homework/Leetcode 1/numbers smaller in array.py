class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            tmp = i
            cnt = 0
            for j in nums:
                if j < tmp:
                    cnt += 1
            ret.append(cnt)
        return ret