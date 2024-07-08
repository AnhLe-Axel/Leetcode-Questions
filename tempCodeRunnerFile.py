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
                
                res.append(cur_line)
                width = len(word) + 1
                cur_line = []
                cur_line.append(word)
        
        for word in range(len(cur_line) - 1):
            word += " "
        cur_line[-1] += " " * (maxWidth - width + len(cur_line))
        res.append(cur_line)

        return res