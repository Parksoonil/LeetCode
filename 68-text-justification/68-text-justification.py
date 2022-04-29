class Solution:
    def fullJustify(self, words: List[str], maxwidth: int) -> List[str]:
        lines = []
        width = 0
        line = []
        
        for word in words:
            if (len(word) + width + len(line)) <= maxwidth:
                width += len(word)
                line.append(word)
                continue
            if len(line) == 1:
                lines.append(
                    "{0: <{width}}".format(" ".join(line), width = maxwidth))
            else:
                space, extra = divmod(maxwidth - width, len(line) - 1)
                i = 0
                
                while extra > 0:
                    line[i] += " "
                    extra -= 1
                    i += 1
                lines.append((" " * space).join(line))
                
            line = [word]
            width = len(word)
            
        lines.append(
            "{0: <{width}}".format(" ".join(line), width = maxwidth))
        
        return lines