from collections import Counter

def is_all_same(the_list):
    if len(the_list)==0:
        return False
    else:
        return all(x==the_list[0] for x in the_list)
    
def isValid(s):
    # Complete this function
    counter = Counter(list(s))
    counter.p()
    values = counter.values()
    if is_all_same(values):
        return "YES"
    else:
        value_counter = Counter(values)
        value_counter.p()
        if len(value_counter) == 2 \
                and any(i==1 for i in value_counter.values()):
            return "YES"
    return "NO"

if __name__ == '__main__':
    from minitest import *

    with test(isValid):
        isValid("hfchdkkbfifgbgebfaahijchgeeeiagkadjfcbekbdaifchkjfejckbiiihegacfbchdihkgbkbddgaefhkdgccjejjaajgijdkd").must_equal(
                "YES")
        isValid("aabbcd").must_equal("NO")
        isValid("ibfdgaeadiaefgbhbdghhhbgdfgeiccbie"+
                "hhfcggchgghadhdhagfbahhddgghbdehidbi"+
                "baeaagaeeigffcebfbaieggabcfbiiedcabf"+
                "ihchdfabifahcbhagccbdfifhghcadfiadee"+
                "aheeddddiecaicbgigccageicehfdhdgafad"+
                "dhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd").must_equal(
                "YES")

