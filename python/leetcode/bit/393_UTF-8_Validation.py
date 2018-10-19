class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        pre = 0
        def get_1_count(num):
            if num < 128:
                return 0
            elif 128 <= num < 128 + 64:
                return 1
            elif 128 + 64 <= num < 128 + 64 + 32:
                return 2
            elif 128 + 64 + 32 <= num < 128 + 64 + 32 + 16:
                return 3
            elif 128 + 64 + 32 + 16 <= num < 128 + 64 + 32 + 16 + 8:
                return 4
            else:
                return 5
        for v in data:
            count = get_1_count(v)
            # print(v, count, pre)
            if count > 4:
                return False
            elif count >= 2:
                if pre > 0:
                    return False
                pre = count - 1
            elif count == 1:
                if pre <= 0:
                    return False
                pre -= 1
            else:
                if pre > 0:
                    return False
        return pre == 0
        
    
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        pre = 0
        count = 0
        for c in data:
            if count == 0:
                if bin(c>>3) == '0b11110':
                    count = 3
                elif bin(c>>4) == '0b1110':
                    count = 2
                elif bin(c>>5) == '0b110':
                    count = 1
                elif bin(c>>7) != '0b0':
                    return False
            else:
                if bin(c>>6) == '0b10':
                    count -= 1
                else:
                    return False
            # print(bin(c),count)
        return count == 0
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().validUtf8([237]).must_equal(False)
