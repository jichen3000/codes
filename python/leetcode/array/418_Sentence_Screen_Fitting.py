class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        res, k = 0, 0
        ls, n = list(map(len, sentence)), len(sentence)
        all_len = sum(ls) + n
        # all_len.p()
        for i in range(rows):
            j = cols
            while j >= ls[k]:
                if j >= all_len:
                    count = j // all_len
                    res += count
                    j -= count * all_len
                    if j < ls[k]:
                        continue
                    # (n,res,j,k).p()
                j -= ls[k] + 1
                k += 1
                if k == n:
                    k = 0
                    res += 1
        return res
                
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        res, k = 0, 0
        ls, n = list(map(len, sentence)), len(sentence)
        all_len = sum(ls) + n
        # (all_len,ls).p()
        if cols >= all_len:
            count = cols // all_len
            res += count * rows
            cols -= count * all_len
        elif cols == all_len-1:
            res += rows
            cols = 0
        if cols == 0:
            return res
        if cols < max(ls):
            return res
        # (cols,res).p()
        i,count,handled = 0,0,False
        while i < rows:
            j = cols
            while j >= ls[k]:
                j -= ls[k] + 1
                k += 1
                if k == n:
                    k = 0
                    count += 1
            i += 1
            if not handled and k == 0 and count > 0 and j < ls[0]:
                count_row = rows // (i) - 1
                # (i,j,count_row,count).p()
                i += (i) * count_row
                # i.p()
                res += count_row * count
                handled = True
        return res + count

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        word_nums = self.preprocess(sentence, cols)          
        word_count = 0                
        for _ in range(rows):
            word_count += word_nums[word_count % len(sentence)]
        return word_count//len(sentence)
        
    # Preprocessing 
    # according every word start, the number of words.
    def preprocess(self, sentence, cols):
        word_nums = [0] * len(sentence)
        word_ptr, word_sum = 0, 0
        word_len = len(sentence[0])
        for i, word in enumerate(sentence):
            while(word_sum + word_len <= cols):
                word_sum += word_len
                word_ptr += 1
                word_len = len(sentence[word_ptr % len(sentence)]) + 1
            word_nums[i] = word_ptr - i
            word_sum -= (len(word) + 1)
        return word_nums
# ["f","p","a"],8,7
# i, word, wlen, wsum, wptr, word_nums[i]
# 0, f     1     0     0
#          1     1     1
#          2     3     2
#          2     5     3
#          2     7     4     4
# 1, p     2     5
#          2     7     5     4
# 2, a     2     5     6     4

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        n = len(sentence)
        wn = sum(map(len, sentence)) + n - 1
        res = 0
        if cols >= wn:
            cn = (cols+1)//(wn+1)
            cols -= cn * (wn+1)
            res = cn * rows
        if cols < len(sentence[0]): return res
        j = 0
        for i in range(rows):
            cc = cols
            while cc > 0:
                if cc >= len(sentence[j]):
                    cc -= len(sentence[j]) + 1
                    j += 1
                    if j == n:
                        j = 0
                        res += 1
                else:
                    break
        return res

    # according the answer, change to python thinking
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        n = len(sentence)
        # according every word start, the number of words.
        def cal_word_num(i):
            left_space = cols
            word_num = 0
            while left_space > 0:
                left_space -= len(sentence[i]) + 1
                if left_space >= -1: word_num += 1
                i = (i+1) % n
            return word_num
        word_nums = [cal_word_num(i) for i in range(n)]
        word_count = 0
        for i in range(rows):
            word_count += word_nums[word_count % n]
        return word_count // n

    # add cols count first, fastest
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        n = len(sentence)
        wn = sum(map(len, sentence)) + n - 1
        res = 0
        if cols >= wn:
            cn = (cols+1)//(wn+1)
            cols -= cn * (wn+1)
            res = cn * rows
        if cols < len(sentence[0]): return res
        # according every word start, the number of words.
        def cal_word_num(i):
            left_space = cols
            word_num = 0
            while left_space > 0:
                left_space -= len(sentence[i]) + 1
                if left_space >= -1: word_num += 1
                i = (i+1) % n
            return word_num
        word_nums = [cal_word_num(i) for i in range(n)]
        word_count = 0
        for i in range(rows):
            word_count += word_nums[word_count % n]
        return word_count // n + res


if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().wordsTyping(["hello","world"],2,8).must_equal(1)
        Solution().wordsTyping(["f","p","a"],8,7).must_equal(10)
        Solution().wordsTyping(["hello"],10000,1).must_equal(0)
        Solution().wordsTyping(["try","to","be","better"],10000,9001).must_equal(5293333)
        # Solution().wordsTyping(["t"],100,100).must_equal(5000)
        # Solution().wordsTyping(["aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa"],20000,20000).must_equal(363600)
        