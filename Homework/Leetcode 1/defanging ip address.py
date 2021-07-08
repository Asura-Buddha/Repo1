class Solution:
    def defangIPaddr(self, address: str) -> str:
        string1 = ""
        string = address
        for i in string:
            if i != ".":
                string1 += i
            else:
                string1 += "[.]"
        return string1