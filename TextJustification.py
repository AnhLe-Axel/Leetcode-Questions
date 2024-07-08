from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        width = 0
        cur_line = []

        for word in words:
            if width + len(word) <= maxWidth:
                cur_line.append(word)
                width += len(word) + 1
            else:
                space = maxWidth - width + len(cur_line)
                added = 0
                index = 0

                while added < space:
                    if index >= len(cur_line) - 1:
                        index = 0
                    cur_line[index] += " "
                    added += 1
                    index += 1
                
                res.append("".join(cur_line))
                width = len(word) + 1
                cur_line = []
                cur_line.append(word)
        
        for i in range(len(cur_line) - 1):
            cur_line[i] += " "
        cur_line[-1] += " " * (maxWidth - width + len(cur_line))
        res.append("".join(cur_line))

        return res

sol = Solution()
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))