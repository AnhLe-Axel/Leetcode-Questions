class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p or p == ".*":
            return True
        if len(p) == 0:
            return len(s) == 0
        elif len(p) == 1:
            if len(s) == 1:
                if p == ".":
                    return True
            else:
                return False
        elif len(p) > 1:
            if p[1] == "*":
                index = 0
                while index < len(s) and s[index] == p[0]:
                    index += 1
                return self.isMatch(s[index:], p[2:])
            else:
                if s[0] == p[0] or p[0] == ".":
                    return self.isMatch(s[1:], p[1:])
                return False

sol = Solution()
print(sol.isMatch("aa", "a*"))