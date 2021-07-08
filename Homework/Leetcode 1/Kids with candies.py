class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = 0
        for i in candies:
            if i > maxx:
                maxx = i
        tmpli = []
        for i in candies:
            if i + extraCandies >= maxx:
                tmpli.append(True)
            else:
                tmpli.append(False)
        return tmpli