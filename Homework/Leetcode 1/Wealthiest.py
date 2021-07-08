class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = -100
        for i in accounts:
            tmp = 0
            for j in i:
                tmp += j
            if maxx < tmp:
                maxx = tmp
        return maxx