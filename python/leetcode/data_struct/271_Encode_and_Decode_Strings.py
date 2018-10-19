class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += "{}#{}".format(len(s),s)
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        # print(s)
        res = []
        i = 0
        while i < len(s):
            index = s[i:].index("#") + i
            # print(i, index, s[i:index])
            size = int(s[i:index])
            # size.p()
            if size > 0:
                res += s[index+1:index+1+size],
            else:
                res += "",
            # print(res)
            i = index + 1 + size
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Codec):
        c = Codec()
        # s = ["",""]
        # c.decode(c.encode(s)).must_equal(s)
        s = ["C#","&","~Xp|F","R4QBf9g=_"]
        c.decode(c.encode(s)).must_equal(s)
