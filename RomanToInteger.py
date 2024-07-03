class Solution:
    def romanToInt(self, s: str) -> int:
        romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        integers = [1, 5, 10, 50, 100, 500, 1000]
        sum = 0
        for i in range(len(s)):
            char = s[i]
            if char in ['I', 'X', 'C'] and i + 1 < len(s) and romans.index(s[i+1]) > romans.index(char):
                    sum -= integers[romans.index(char)]
            else:
                sum += integers[romans.index(char)]
        return sum
