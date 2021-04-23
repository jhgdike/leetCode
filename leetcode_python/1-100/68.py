class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        n = len(words)
        tmp = [words[0]]
        cnt = 0
        sum_ = len(words[0])
        for i in range(1, n):
            # if not sum_:
            #     tmp.append()
            if sum_ + len(words[i]) < maxWidth:
                sum_ += len(words[i])+1
                cnt += 1
                tmp.append(words[i])
            else:
                if cnt == 0:
                    s = tmp[0] + " " * (maxWidth-sum_)
                else:
                    s = tmp[0]
                    per_empty = (maxWidth-sum_) // cnt + 1
                    empty_mode = (maxWidth-sum_) % cnt
                    for j in range(cnt):
                        empty_cnt = (per_empty+1) if j < empty_mode else per_empty
                        s += " " * empty_cnt + tmp[j+1]
                ans.append(s)
                tmp = [words[i]]
                cnt = 0
                sum_ = len(words[i])
        s = " ".join(tmp)
        ans.append(s+" " * (maxWidth-len(s)))
        return ans


s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
