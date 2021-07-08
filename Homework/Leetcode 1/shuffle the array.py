class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        tmpli = []
        for i in range(0,n):
            tmpli.append(nums[i])
            tmpli.append(nums[i+n])
        return tmpli