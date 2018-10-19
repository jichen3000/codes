from collections import defaultdict
def is_p(word):
    n = len(word)
    for i in range(int(n/2)):
        if word[i] != word[n-1-i]:
            return False
    return True

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        n.p()
        if n <= 1: return []
        results = []
        for i in range(n-1):
            for j in range(i+1,n):
                if is_p(words[i]+words[j]):
                    results += [i,j],
                if is_p(words[j]+words[i]):
                    results += [j,i],
        return results
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        # n.p()
        if n <= 1: return []
        results = []
        starts, ends = defaultdict(list), defaultdict(list)
        for i in range(n):
            if words[i]:
                starts[words[i][0]] += i,
                ends[words[i][-1]] += i,
            else:
                for j in range(n):
                    if i != j and is_p(words[j]):
                        results += [i,j],
                        results += [j,i],
        # (starts,ends).p()
        for k, sl in starts.items():
            for si in sl:
                for ei in ends[k]:
                    if si != ei and is_p(words[si]+words[ei]):
                        results += [si, ei],
        return results

# review
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        new_words = [(w,i) for i, w in enumerate(words)]
        new_words.sort(key=lambda x: len(x[0]))
        word_dict = {}
        res = []
        def check(w):
            n = len(w)
            for i in range(n/2):
                if w[i] != w[n-1-i]:
                    return False
            return True
        for w, i in new_words:
            # (w,i).p()
            rw = w[::-1]
            if "" in word_dict and check(w):
                j = word_dict[""]
                res += [i,j],
                res += [j,i],
            if rw in word_dict:
                j = word_dict[rw]
                res += [j,i],
                res += [i,j],
            for k in range(len(w)-1):
                if w[:k+1][::-1] in word_dict and check(w[k+1:]):
                    res += [i, word_dict[w[:k+1][::-1]]],
                if rw[:k+1] in word_dict and check(rw[k+1:]):
                    res += [word_dict[rw[:k+1]], i],
            word_dict[w] = i
        return res

    ## best one
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mem = {}
        n = len(words)
        # n.p()
        # if n <= 1: return []
        results = []
        for i in range(n):
            mem[words[i][::-1]] = i
        for i in range(n):
            wn = len(words[i])
            for j in range(wn+1):
                left, right = words[i][:j], words[i][j:]
                (left, right).p()
                if left in mem and is_p(right) and mem[left] != i and wn >= j:
                    (i,mem[left]).p()
                    results += [i,mem[left]],
                if right in mem and is_p(left) and mem[right] != i and wn > wn - j:
                    (mem[right],i).p()
                    results += [mem[right],i],
        return results

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_p(w):
            wn = len(w)
            # print(w, wn)
            for i in range(wn//2):
                if w[i] != w[wn-1-i]:
                    return False
            return True
        res = [set()]
        if not words: return res
        n = len(words)
        wd = {words[i][::-1]:i for i in range(n)}
        
        for i in range(n):
            w = words[i]
            wn = len(w)
            for j in range(wn+1):
                if w[:j] in wd and wd[w[:j]] != i and is_p(w[j:]):
                    res[0].add((i, wd[w[:j]]))
            for j in range(1,wn+1):
                if w[j:] in wd and wd[w[j:]] != i and is_p(w[:j]):
                    res[0].add((wd[w[j:]],i ))
        return list(res[0])
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_p(w):
            wn = len(w)
            # print(w, wn)
            for i in range(wn//2):
                if w[i] != w[wn-1-i]:
                    return False
            return True
        res = []
        if not words: return res
        n = len(words)
        wd = {words[i][::-1]:i for i in range(n)}
        
        for i in range(n):
            w = words[i]
            wn = len(w)
            for j in range(wn+1):
                if w[:j] in wd and wd[w[:j]] != i and is_p(w[j:]):
                    res += [i, wd[w[:j]]],
            for j in range(1,wn+1):
                if w[j:] in wd and wd[w[j:]] != i and is_p(w[:j]):
                    res += [wd[w[j:]],i ],
        return res


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        words = ["abcd", "dcba", "lls", "s", "sssll"]
        Solution().palindromePairs(words).must_equal(
                [[0, 1], [1, 0], [3, 2], [2, 4]])
        # words = ["bfdijce","gce","bhgchdcejfcgjfiece","dcebhjhjfgcjdfjg","ejgbjebi","fffgigehhabhfhdge","fajahcagah","ja","ghedcicbg","ccifjedjig","gihbhhebhheecgeifcii","gdjfajdhgibgdb","hcjjdi","jhfjecjigjdhbga","dejbejddhje","ecgfijhcja","ghejidhebg","hfehjfhhfjdjeeahjad","bbajfihihbacdefh","cdeeebaab","cdagiaffffjbjcaia","ab","ejaieca","hcfiecbfcjjhhdj","aehjicd","ieciciiehidbfaaifcj","dca","cjachjbgbefffci","i","j","ejbggahbhii","gjdcjfbhefdgd","ecaed","jbbbjffjgib","biiejcgbcahijgbibiaa","aeahieeceggchd","djicdd","cbj","ggfbeifejd","jgjhehhe","fdgib","ddgabdicbibj","ejbcdfiacicegiibeje","bfdcd","hhjajfgefgefa","cecgbebfchia","jchdbcbh","jcegc","dejfjjcbcdiadaaaei","bjbhfa","ibjba","iddhgdjgjgeid","ifiigfijhad","ahihjcfh","degiedaj","fjfhhiddacjdij","ecjhgc","beebfahffgjaabjafi","fcbdijfjgifjgbijdfc","fc","jgbjajjae","edcgjcigdeecbdhif","fhbhjcbajfddifci","ch","jahggfgdjidhihcafcji","effbcdfbfjdegacdhgc","acjajjbeaeedjbcfihd","bag","ffjdidbghbfdeh","eice","h","aeffjeagfigicadg","hgbejbgcecejfeg","hh","bbadbcbiaechiid","dicajhebdhcgfhgbafa","ehig","eaeddiebehiabf","beijag","gaabbe","gfiehgehe","hffcdfdhcfiia","efbfhe","fdg","hddeaaeacadbhf","dd","hcaicbbjaechebfj","aibjjfdhgchjjhhabe","bjgicf","aij","icaajcfdad","f","fgieaifhghgchhcbjad","gbfjgaabffdeafgejef","bebhbdgjbchbheegba","ceefea","eadjbjfacjeaihefbc","eghihceecbgiehihe","icadjeefhiead","jjibgdb","efedigddjfdea","c","d","hhcjhbdggcbdif","ejhga","fejfbccaeac","ehjbeje","dehd","caddigbdaabdffaie","bjjgjiehaffaachfh","ehhaicejafgddcfihee","jefii","gbijjebhdehi","bfdbcajjfdfh","ca","jbbfibdadiefah","bbefdfcghcaaiijb","ib","ce","bbfdb","cbbcbjebjbjhcfd","ecjge","gjdegighaagbhjc","afdcgdggbi","hdgah","gahdgc","jfbgeaebbd","cefbhfcabagjhjhgeabd","jdaacjjdbc","efacbghiheihedfi","fbffgdcajadjh","aib","ihdcfibgegedeaaa","gehbcj","hjfajbbdc","ihafhfddfhbfgc","fhecfcjd","adefabbggidhgcjf","dedfejiddhcgabfcbihc","hbibhhghhajg","iabjgjihiiiebeig","iegajfg","aaj","gfdhaahdbcbfgja","jd","ifeibdfegjcafdiee","dhjih","afbfdf","gjighgaebb","cbdfjddjfb","aa","gbcajjeajjcfg","gcd","gefddc","fcbiehbiaddcbgfccbid","ifjbgdc","hhgdebcf","iabe","bihj","ifajbhjjhbcd","diabbjjh","bgjhihhgba","jfjcfgbchdfhhggcg","ahdbehfhhccfeefcicf","dghf","dacagebbcieggjjbfi","hejjgdhjbeggedbbgj","a","gghibdbhf","cadfh","fhfbgdegfhccf","hcihffaibjedbjcef","ghhibbgdhgibbfj","jaegfhahhe","fjacga","cjfacjichhhcbhfhbj","gdaejffeiiigfiaci","cdfejfjf","ddf","fhfeifgi","ghghiedhejdhicfhgiaj","abajg","daajgijcdh","bfaiabeaahifjjfdf","ccfhjiegdaj","bhbeegihbifefiia","fb","cjffbhfbgjjfadih","dhefhfaajejee","deijihhhjjibfea","jbgij","agfdidigfeada","daecfjiaacigcjjcb","bgdiied","cjadgiie","ghbhfci","jdbfhhhach","ifiegeaad","eajhiechdhjfhdecfjhe","jhbd","gje","edeggghabeefcaa","aeebiaheefjbigge","bfdhjacgjdficad","fiafgifgajciafiib","aiejhc","gh","eidfbdfcffci","hbdbbcaghejgchiegjf","cdffefdhbfgh","hbjiahfgiiejfcfbg","fdfccabdbggbifhjhjga","dhggbecfhdhcbfddafe","ihee","ciaadifia","gd","hac","dhgaegbichdafdiehe","agdfefdjdbcg","fe","hgdhef","cfgccibbfbcjicg","jj","gdh","decghhbfdcaaiafecaf","jibccbadhdfabjehfi","gaibdjdgjdifcadce","hdcbeegf","ebdaj","fgcdh","hgfabihbhibcdccgd","dhehjgicjhhibfghacig","dgfiagb","jhadfjfafagaggfg","eegg","bjaaeig","chfi","fbb","djcieficibgiiabjdbdc","gdcjijfajgbcb","digh","gbhjcfafhjgchgabjfe","jhggiggjd","eeccgibhheheaaajfadd","bcdcggagb","gbbdbjgi","jchahjcaahbad","bjefigc","ggfhee","ejb","ficidccfgffehdi","iadghjbahjeeja","ighibfegabfegfjafab","dfaeejga","bffbbja","hebbgeigchdb","cfdi","dhha","fjfhfjcabe","gfcca","adeffi","fidgieaijfjcjhgfc","igibid","jjhechdbabegjabdjfc","ai","dgc","aehhchefa","beihbjaahe","ebiagd","bfcafajjahbid","baiijjfgjibafacg","hhajgicga","deadad","efcahgh","aiciffj","hhjchdfeiabfjiiie","agihihabbc","ccacdghah","eifhbbidjbceaegc","hfadbaediajcfbb","jjjjcgeaacffgg","dceiidhcigcbgc","biabjchfi","chgjbhigebba","ciggdgfigbjjjdeccgba","cehe","caidbdi","fjeecdebhidchfeggja","hfbbccad","bbbaggbegaihc","cdahjdjeifccjijdiabj","jcjj","jagf","afagefhgiahebich","fjgejbbdbgab","aih","bgjabhffeafj","fgcghbcheg","ebacdfbchhiaffjgeh","ehhejdbdgg","hafgeiahaffgicafjffi","bbhajadcdeihbggfi","fbdbg","edbiaihc","ed","gcdeefbhidc","gijcigefcecgffjfie","hjg","jahfaghjjbafaebcccf","ahjhafidhbic","gecihhgbhgeeaga","feagfagcef","fhahccbfddhfcaidaa","hajchgjeb","ajhbhfjdfgfdebbgaa","jiedjcgbgifafi","hiaje","cafbaibebabjdadcc","icicefadeecaiceiiaf","jeejjedbfh","ajjdi","diafeaahaeb","heedafafabhcg","hfgdbchbigddjaffg","adahedgichjhhhghg","eajjafcdadbbhfeii","cfachcdbhbcd","fabiigh","gegdbcfghcc","igafadcghfcgbhfccdf","cdbbgbgfggjjedci","ehghd","hgadfefdeeh","ccbeibahfc","jfeag","dihhjehhab","geigahebghifjihdgcfd","fefhbciachhjafj","egdcjbdhgja","fbdfae","cgbdeffbacchjfeig","jgic","caefggbjjdbbjcjfbagb","ddaadegchiejjjbf","ad","dabhgddjgahaach","eddaad","hjbfa","hccejcgcbebfffdhibe","gjababagaaa","ghbjfadjjejaga","cgcdcfadhgdeff","bfihdibecfjehaef","jhijchdaeahdjdfgeac","jb","ejfihbbebihhed","jecgdefeheiebfeabb","aibchhafgcbefdah","dcgefai","fcafbgbfh","gjdaef","eciidjhcbgachbdfjha","dddbccahjdafacjeaib","eifcchejafiijagca","gg","jihahehccafjfdg","dhfia","geghggbdfdgficdhccij","bajjefgdcedjdededd","gdghcgb","bf","gjaeidd","bagc","b","ahaeecafgaafgiif","hfgjbgjicigbciggh","jcfhdgaddbhhgfiebgfi","fejbgcddja","gebjehgdbfhcfidcidhh","ggcaafdbbaiefd","hfaggjab","begicebfhiceicajcfj","iefhaahfajdfchfhecee","icj","cegijjjjfehded","eeadcidaecejchabicbe","ajhhdcachhi","gifibbgaabghj","cajdcfeaefaegdag","bdeedaejj","edjd","ibciabjdefabdgbjgjhi","dhbd","bbijjcjdjjggg","feifjbj","fbdhhahfd","dg","bgeihfafeccibeccjii","gfcecgfebcbgh","jeeefihhaeccf","dgghcbiffdfafjdihai","begae","jbhjbigiceagaigad","acgfbbibihfagih","adgbgjdafcf","gadcjajadeafcabbcg","hfbdfhbcjbdd","hfejjjjbgahcheejef","eihjdcfhbgbcdgdedca","dfg","idfffagdeaee","aejgdiidhbgjaj","cchdbfdaeaaid","igjjaegfe","gedggj","jhbibhehbefddieff","ieaec","ejjifcbdjcjfejcg","djggigibjc","aie"]
        # Solution().palindromePairs(words).must_equal(
        #         [[0, 1], [1, 0], [3, 2], [2, 4]])
        # Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]).must_equal( [[3, 2], [0, 1], [1, 0], [2, 4]])
        # Solution().palindromePairs(["abcd","dcba","lls","s","sssll",""]).must_equal([[3, 5], [5, 3], [3, 2], [0, 1], [1, 0], [2, 4]])
        # Solution().palindromePairs(["ab","ba","abc","cba"]).must_equal([[0,1],[1,0],[2,1],[2,3],[3, 2], [0, 3]])
        # Solution().palindromePairs(["a","b","c","ab","ac","aa"]).must_equal([[3, 0], [1, 3], [4, 0], [2, 4], [5, 0], [0, 5]])
        # Solution().palindromePairs(["a",""]).must_equal([[0,1],[1,0]])
