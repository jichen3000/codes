class Solution(object):
    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def gen_line(w_list):
            n = len(w_list)
            if n == 1:
                return w_list[0] + " " * (max_width-len(w_list[0]))
            space_num = max_width - sum(map(len, w_list))
            left, remain = divmod(space_num, n-1)
            res = ""
            for i in range(n-1):
                res += w_list[i] + " " * left
                if i < remain: res += " "
            res += w_list[-1]
            return res
        
        res = []
        w_list, count = [], 0
        for w in words:
            if len(w) + count <= max_width:
                w_list += w,
                count += len(w) + 1
            else:
                res += gen_line(w_list),
                w_list = [w]
                count = len(w) + 1
        last_line = " ".join(w_list)
        res += last_line + " " * (max_width-len(last_line)),
        return res
        
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],
                16).must_equal(["This    is    an","example  of text","justification.  "])