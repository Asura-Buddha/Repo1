class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pr = 1
        sm = 0
        n = str(n)
        for i in n:
            pr *= int(i)
            sm += int(i)
        return pr - sm