class Solution(object):
    def longestPalindrome(self, string):
        maxLength = 1
     
        start = 0
        length = len(string)
     
        low = 0
        high = 0
     
        # One by one consider every character as center point of 
        # even and length palindromes
        for i in xrange(1, length):
            # Find the longest even length palindrome with center
        # points as i-1 and i.
            low = i - 1
            high = i
            while low >= 0 and high < length and string[low] == string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1
     
            # Find the longest odd length palindrome with center 
            # point as i
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and string[low] == string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1
     
        # print "Longest palindrome substring is:",
        # print string[start:start + maxLength]
     
        return string[start:start + maxLength] 
               
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        cur_palindrome = []
        longest = []
        for i in xrange(len(s)):
            print("cur_palindrome",cur_palindrome)
            if len(cur_palindrome) == 0:
                if i>=1 and s[i] == s[i-1]:
                    cur_palindrome.append(s[i-1])
                    cur_palindrome.append(s[i])
                elif i>=2 and s[i] == s[i-2]:
                    cur_palindrome.append(s[i-2])
                    cur_palindrome.append(s[i-1])
                    cur_palindrome.append(s[i])
            else:
                #if len(cur_palindrome) % 2 == 0:
                #    syn_pre_i = i-len(cur_palindrome)
                #else:
                syn_pre_i = i-len(cur_palindrome)-1
                print(i, s[i])
                if syn_pre_i >= 0: print("syn_pre_i",syn_pre_i,s[syn_pre_i])
                if s[i] == s[i-1] and len(cur_palindrome)==cur_palindrome.count(s[i-1]):
                    cur_palindrome.append(s[i])
                    if syn_pre_i >= 0 and s[i] == s[syn_pre_i]:
                        cur_palindrome.insert(0, s[i])
                elif syn_pre_i >= 0 and s[i] == s[syn_pre_i]:
                    cur_palindrome.insert(0, s[i])
                    cur_palindrome.append(s[i])
                # means cur_palindrome end
                else:                        
                    if len(cur_palindrome) >= len(longest):
                        longest = cur_palindrome
                    cur_palindrome = []
                    print("clear cur_palindrome",cur_palindrome)
                    if i>=1 and s[i] == s[i-1]:
                        cur_palindrome.append(s[i-1])
                        cur_palindrome.append(s[i])
                    elif i>=2 and s[i] == s[i-2]:
                        cur_palindrome.append(s[i-2])
                        cur_palindrome.append(s[i-1])
                        cur_palindrome.append(s[i])
                    # if s[i] in cur_palindrome:

        if len(cur_palindrome) > len(longest):
            longest = cur_palindrome
        if len(s)>0 and len(longest) == 0:
            longest.append(s[0])
        return "".join(longest)
    

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().longestPalindrome("abbbba").must_equal("abbbba")
        # Solution().longestPalindrome("abbbbba").must_equal("abbbbba")
        # Solution().longestPalindrome("dddaaabbbbbaaaddd").must_equal("dddaaabbbbbaaaddd")
        # Solution().longestPalindrome("aaxyaazaaaazaayxaa").must_equal("aaxyaazaaaazaayxaa")
        Solution().longestPalindrome("abababa").must_equal("abababa")
        # Solution().longestPalindrome(   "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa").must_equal(
        #                                 "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")


