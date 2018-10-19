class Solution:
    def customSortString(self, s, t):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s_dict = {c:i for i, c in enumerate(s)}
        others = []
        new_t = []
        for i, c in enumerate(t):
            if c not in s_dict:
                others += (i, c),
            else:
                new_t += c,
        new_t.sort(key=lambda x: s_dict[x])
        for i,c in others:
            new_t.insert(i, c)
        return "".join(new_t)
    
    
            
        
    def customSortString(self, s, t):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        from collections import Counter
        
        s_set = set(s)
        others = [(i,c) for i, c in enumerate(t) if c not in s_set]
        # print(others)
        counter = Counter(t)
        j, res = 0, ""
        for i in range(len(t)):
            if others and i == others[0][0]:
                _, c = others.pop(0)
                # print(c)
                res += c
            else:
                res += s[j]
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    j += 1
        return res        