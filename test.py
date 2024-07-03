from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        spaces = []
        row = 0
        count = maxWidth
        lines.append([])
        for word in words:
            if count - len(word) < 0:
                spaces.append(count + 1)
                count = maxWidth
                lines.append([])
                row += 1
            lines[row].append(word + ' ')
            count -= len(word) + 1
        spaces.append(count + 1)
 
        for i in range(len(lines)):
            if len(lines[i]) > 1:
                for j in range(spaces[i]):
                    lines[i][j%(len(lines[i])-1)] += ' '
            else:
                for j in range(spaces[i]):
                    lines[i][0] += ' '
            lines[i] = ''.join(lines[i])[0:maxWidth]

        return lines

sol = Solution()
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))    