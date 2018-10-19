class Solution:
    def partitionLabels(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        from collections import Counter
        res = []
        cur_set, start_i = set(), 0
        counter = Counter(s)
        for i, c in enumerate(s):
            counter[c] -= 1
            if counter[c] > 0:
                cur_set.add(c)
            else:
                cur_set.discard(c)
                if len(cur_set) == 0:
                    res += i+1 - start_i,
                    start_i = i + 1
        return res
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        last_pos_dict = {}
        for i,c in enumerate(s):
            last_pos_dict[c] = i
        end_i = -1
        for i,c in enumerate(s):
            last_pos = last_pos_dict[c]
            if i > end_i:
                res += last_pos + 1 - i,
                end_i = last_pos
            else:
                if last_pos > end_i:
                    res[-1] += last_pos - end_i
                    end_i = last_pos
        return res
                    
            
    