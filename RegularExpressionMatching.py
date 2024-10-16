class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p or p == ".*":
            return True
        elif len(p) == 1 and len(s) == 1:
            return p == "."
        elif len(s) >= 1:
            if len(p) <= 1:
                return False
            elif p[1] == "*":
                s_index = 0
                while s_index < len(s) and (s[s_index] == p[0] or p[0] == "."):
                    s_index += 1
                for i in range(0, s_index + 1):
                    if self.isMatch(s[i:], p[2:]):
                        return True
            else:
                if s[0] == p[0] or p[0] == ".":
                    return self.isMatch(s[1:], p[1:])
                return False
        elif len(s) == 0:
            if len(p) < 2:
                return False
            else:
                if p[1] != "*":
                    return False
                else:
                    return self.isMatch(s, p[2:])

sol = Solution()
print(sol.isMatch("aaaaa", "a*a*a*a*a*b"))