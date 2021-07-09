class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmpli = [0]*len(indices)
        for i in range(len(s)):
           tmpli[indices[i]] = s[i]
        tmp = ""
        for i in tmpli:
            tmp += i
        return tmp