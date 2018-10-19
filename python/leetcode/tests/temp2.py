class Solution:
    def rotateString(self, sa, sb):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        from collections import defaultdict
        if len(sa) != len(sb):
            return False
        mema = defaultdict(list)
        memb = defaultdict(list)
        n = len(sa)
        for i, c in enumerate(sa):
            mema[c].append(i)
        for i, c in enumerate(sb):
            memb[c].append(i)
        if len(mema) != len(memb):
            return False
        n.p()
        mema.pp()
        memb.pp()
        diff = None
        for k in mema.keys():
            la = mema[k]
            lb = memb[k]
            if len(la) != len(lb):
                return False
            for i in range(len(la)):
                if diff == None:
                    diff = (la[i] - lb[i]) % n
                else:
                    if diff != (la[i] - lb[i]) % n:
                        return False
        return True
    def rotateString(self, sa, sb):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(sa) != len(sb):
            return False
        n = len(sa)                    
        for delta in range(1, n):
            for i in range(n):
                if sa[i] != sb[(i - delta) % n]:
                    break
            else:
                return True
        return False
        
if __name__ == '__main__':
    from minitest import *

    with test("some"):
        Solution().rotateString("clrwmpkwru","wmpkwruclr").must_equal(True)
