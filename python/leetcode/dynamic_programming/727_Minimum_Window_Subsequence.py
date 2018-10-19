import bisect
class Solution(object):
    # tle #42mins
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        sn = len(S)
        tn = len(T)
        (sn,tn).p()
        if tn > sn: return ""
        positions = {}
        for c in T:
            positions[c] = []
        for i in range(sn):
            c = S[i]
            if c in positions:
                positions[c] += i,
        if tn == 1:
            if positions[T[0]] :
                return T[0]
            else:
                ""
        groups = []
        for start in positions[T[0]]:
            for end in positions[T[-1]]:
                if start <= end and end - start + 1 >= tn:
                    groups += [start, end, start],
        def group_cmp(g1, g2):
            l1 = g1[1] - g1[0]
            l2 = g2[1] - g2[0]
            if l1 == l2:
                return cmp(g1[0], g2[0])
            else:
                return cmp(l1,l2)
        groups.sort(cmp = group_cmp)
        groups.size().p()
        for group in groups:
            for i in range(1, tn-1):
                for ci in positions[T[i]]:
                    if ci > group[0] and ci < group[1]:
                        group[0] = ci
                        break
                else:
                    break
            else:
                return S[group[2]: group[1]+1]
        return ""
       
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        sn = len(S)
        tn = len(T)
        if tn > sn: return ""
        dp = {}
        def dfs(ts, ss):
            if (ts,ss) in dp:
                return dp[(ts,ss)]
            # (ss,ts).p()
            for i in range(ts, tn):
                min_len = sn + 1
                cur_result = ""
                for j in range(ss, sn):
                    if T[i] == S[j]:
                        if i+1 == tn:
                            if ss > 0:
                                dp[(ts,ss)] = S[ss:j+1]
                                return S[ss:j+1]
                            else:
                                dp[(ts,ss)] = S[j]
                                return S[j]
                        elif j+1 == sn:
                            pass
                        else:
                            r = dfs(i+1, j+1)
                            if r:
                                if ss > 0:
                                    result = S[ss:j+1] + r
                                else:
                                    result = S[j] + r
                                if len(result) < min_len:
                                    # result.p()
                                    cur_result = result
                                    min_len = len(result)

                dp[(ts,ss)] = cur_result
                return cur_result
            dp[(ts,ss)] = ""
            return ""
        return dfs(0,0)                
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        sn = len(S)
        tn = len(T)
        if tn > sn: return ""
        dp = [[None] * sn for _ in range(tn)]
        first_j = 0
        for i in range(tn):
            found = False
            for j in range(first_j, sn):
                if T[i] == S[j]:
                    if i == 0:
                        dp[i][j] = (j,j)
                    else:
                        dp[i][j] = (dp[i-1][j-1][0], j)
                    if not found:
                        first_j = j + 1
                    found = True
                else:
                    dp[i][j] = dp[i][j-1] if j > 0 else None
            if not found:
                return ""
        
        min_l = sn + 1
        result = ""
        for item in dp[-1]:
            if item:
                start, end = item
                # (start, end).p()
                if end-start+1 < min_l:
                    result = S[start: end+1]
                    min_l = end-start+1
        return result
    
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        sn = len(S)
        tn = len(T)
        if tn > sn: return ""
        dp = [None] * sn
        first_j = 0
        min_l = sn + 1
        result = ""
        if tn == 1:
            if T in S:
                return T
            else:
                return ""
        for i in range(tn):
            found = False
            for j in range(first_j, sn):
                if T[i] == S[j]:
                    if i == 0:
                        dp[j] = j
                    else:
                        dp[j] = pre_dp[j-1]
                        if i == tn - 1:
                            if j - dp[j] + 1 < min_l:
                                min_l = j - dp[j] + 1
                                result = S[dp[j]: j+1]
                    if not found:
                        first_j = j + 1
                    found = True
                else:
                    dp[j] = dp[j-1] if j > 0 else None
            if not found:
                return ""
            pre_dp = dp[:]
        
        return result



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().minWindow("ss","u").must_equal("")
        Solution().minWindow("abbcdebdde","bde").must_equal("bcde")
        Solution().minWindow("abccdebdde","bde").must_equal("bdde")
        Solution().minWindow("zmcmjm","mm").must_equal("mcm")
        Solution().minWindow("zmccquq","mq").must_equal("mccq")
        S = "dlnizvdvourutyysrupkgnjfppstcriscwfbfxggepvrzqxyuniktgbpcujntijkrcbvtkupwwmsylrxwhmvxbxebrwqqyllyzhkspiywlgngbcvpdughbnidjovegnyqyhfnnqxwvgaxpgyokcgmxuloirvgwqluiffxtqtojqzmjejbwpxbeejzdhnyrliorpmjopuef"
        T = "vfvyzhpnme"
        Solution().minWindow(S,T).must_equal("vourutyysrupkgnjfppstcriscwfbfxggepvrzqxyuniktgbpcujntijkrcbvtkupwwmsylrxwhmvxbxebrwqqyllyzhkspiywlgngbcvpdughbnidjovegnyqyhfnnqxwvgaxpgyokcgmxuloirvgwqluiffxtqtojqzmje")
        S = "cnktshvvjnnwftckuerryorwnpirtxjgvzxyfxmnwtcrwdycwdndcguzzvziachknezyxsefcxdjnmncuzgeosxrswnkfsoioezgwwnhkfpruwvleohnhgdcrhljvuxovajjpznmemjefmzxcfycskqwiqybpjzqdnqgvqaaxfhobugozbccxlvzwyedqcdilzrqaxqalggwjoyzexdtxadjbtryuxzhplvihxewahnldiuvvfajnmtiwbrkumvepnwvufxhbwkravnbwhjtgigngxohbtuakxhftttyluatnasevhpxcgiqertakkldcojqyvqwtbowliufswqfzmtcgoaejgnwtwobrskkzbmsspcpveqrhfertkeitdomceozpdrfeemfgggzwfywvlovkpsxwhmgfhlqjlkmpraerxlnmkhjciziivtrvbduapionqlmgbgbrmpavvsfvmbgtczxitctsuqskkmfcsrmvbgoygkawcxxccpzefzddtajwnlwjvfvhegwyforoymslmynhexdvftlhvstybaboduqcjwcrbmtonvdfvjthyaukrddvvypdxbavtavdzlzejyayevkneupnafnvmdekmloeowmrppvlzpdtoszxqbsbugmjjcorsvmbcydzmzegoypqkfsjutadgdthbfgxnrnqacmagdmmhqcoxdvsocmwdopvyfsthczdyzxnrpdysagsuvecbpodjsvgfyohcotnabrnbbtgfmvlkxfietcpwiwlwloxskwfesezaozkdmwqmccqstctvrmijxsndduiqphtkbqnhmimfmfigkwanhglnvegxpswsplscnumykeyeeguvybhjqsalaajpxuucglrsxuccuussnlgmovkwpclajxwqpekpsklhhnmcdpdtrtmlyxhwzebvesjjgirfpvwyscwgkesahngjahacftxxoyevubhxlcsrpyxjwyyzdgsavkfkmoxrhjzvnquutgncyedgcmkhlomkdjjhnhbiefgnnyiqbhzkwfefgnzdyuhnecwgeqimempikgswvhnfewstpuvxwewgdlmeeicqqifmsxjjclwjsjctkeveuqfryqyuvahtxybgdufvdtaefnvnrooiofmesjypuegncrtvqhxussokaraopboqnngqebuueolxulrmwfdihjplfmiottohagheohyhsndmaldbupcqiflsklhhhubmpybgzggmsjhrhydjzgbyeljdzxlkzzdjqfngetkvkystbcetaxmycdsygtwvjvieehtetvtelxhldbcjnuawdoepicnitdymznrykpmpiexquobsaqylguwbdnulupzuchkxfpxrtjmecuckcigucggzieergyxhfmuiaaudnebsjpcrekmibkxylejpcmcmyivavsnbzoairaiafvikymdndjbqzkbdpzbenzhtnloqqkwtsvchejngxravpfwmcppdkoxsxcxwwursdcpqxrcbbtkammzpalutgkhlfegafzfusbtfzfdlpeyljiaqqddwtopkjmpllfacqwckirhwiqudfomcbhhroftcgrlekzmxxhhhinqwayyjbanmekzagyghkhzkmokhoojotfnznamekmhqptnkkqzcalhuiqsnpedcmowfjkyfhqjpsuowwrpdgxqcvyeuvijckhkoxeslqzexovcliqkkewdlzxveurjycsjrpubfxjcutvmniqnzdakwbdrwxxnmpzityozccozzmrunjgzryylaqpfuqxaqmrzpwjcfgscupkavzrocuizmmmffgzselluxhrgzizokacdsoaovdbeovbezzvrdsscofwkbiasytokpylwxmroekjyodhlulubkkjuxtcatmcjknpjeeuuysrmtfjvduqyifvpcjkcqoobdpdtcvsgtkjfghaelzpqytixemppcqrkfhwdilbkurywafiwbqeywcqyniypdxgcyfhkmmnnycaonwgsqwwswkkjkkofyjxiihaeswxjlglcmzghxdjvkhadjxatyqcsvtmvyrbjadlnvwsrmadgqnmkxmkoqfiydubdzxspyygmjiaorkfcxlsktcqtwojngoxfzjjdnupbfvagukavprsseanygyhywtixtxqochiiizchyusfwzktfwgcuvfjgcwqvwgsdwkodtpphxxddtdzionwqttvrsocpkhpgljvhdzgfmfgirszfpignwnkrxuccmqcljpdlgaxnfiaeeadrkqxegfedbpnjnpyobactbjoqfppkhiicohesrhjunplsmipuhxfsaumeqcrukxhfoacvobqavodstisklsxjwqtfbhycmleycdomvakdkbduzwksmgfjcdansworblcpvnzzfgzpmelictpyuqchonlduzfltlbskpfqrisshtaambszqqergfeefkvkiogrgwknepimwoqoxbdjdyisxeocdjocqqqcxemiuzzburlxzogsjcylrpgsmqgwzyynvxjxglfyerlfmzogaznhkkspcsomvvixpukzifbflzkcdfmeaxvwuhxszzmdxujtgqpphnmsuhjzszvsnvsykuokzwauiytajvohmmmwbyikmzwpcyodaxdonkeczgcmedfkoafpnclvhspddcpycrtlvqihxvtefrwmmkbpujccauhdsnlidiekgnxgwiwbimrdbwxqdosqoczluwzpaiunibzrewyopculgbhzjxqzdqgrfkrhslxvdvxypxaxjphqcoujfkalcfjopujlgowbsoctvqxdlkoceyngwtauwxcivwezgorjnkwacuyvyhlndztnxkqwflmqyoxnhtbzfzsoglazflewfqzixlvzmmrmihuexgehifhsbrvqeafdmjixgrzqsxppnvlcrmzxoufkfihwxkpimwwcdlldvdifigzfqhknxqmbaqdriyoztlniywvgjvcoaprfgwlwvwmddsxtlzvxhhmqhktlpmfdtiqnzbpqaclxtddwhpqdnkswoldhgcldcuaxvtieygsjmjgokfmmyfxvzryvluovavzhobgwrmkceqayvkwsvxtksqqxgfgadazgfmhgdsxjqakcuapfqggoumfoqugazlvnupwneheathmofbsqqilrbyvcnejjvknktenkmwvzocyrxwifjhrtkkvvyhloqnjyqmiaarrunwpxlttzvgvbicbktedyxdzwdooghxapvydbxiwmgvykfoylyxvxajpjemwvgygdeddwlzzdvyfnhqezhyqrsxcgvrrgworoynclzyjqpqovlpnjvqcluhjuoubsowraehpjmlpdnxeeanoikvynzejzijyupwxclupdpvbeqjkamfppjbirtztttajigqpqcqzprpwnclczpqoqvtpejibqdurjmhlvfongstxjyinkpbvlxplufjefpirxivjusjbexhulhvzhmsvorlnsulffysovkljqsdkrgpakozcdoneswhgwmdkzfwanjegxzcxlsnwzqvwqdoezufibpmgeuilgnakundeskyiddhskgdkryhnjxcmujlytukhypquofveiwqwaylrlgqyhmyrnckvdlekbguphwuajchmqwialethmfpkswaqfbdxporwqjluaemxabukwamajjrcoapuzpnnbleapcaqonxnbhfbbdoffbhuimrawgdusrkvpbpbmrwmsprxfqjerovruewjixyfdxfsyseolnztyusbtzfnlcfygpwwogystbtrddqcrhoiqvmrdzglohzhsmwlvfqwtrdvspfvofxaynenoaivxxcpuzeswdzqjxknwdrrlronqkfaepmqltdeiizhkxkqeohexggdrfegsiwjzipextyrybgttgghfbgfhjnvzwkpipguuevqwwjyyjculvkxjeiwhuowbeofmsysbsemjlrnejuonsofjlueexsgsupmrepknjtvrgbczzdvphfnsavcikhdlrycasxhfjaktukleqkaqybljrypkajbrhofpqsqtzuphixogloroidliepvzwnufaacsrzedslnbnauermotqhmstthfavourpvxrtwejmhdtlyhghtcdtkjemumbijzwbuervgqnhdmmknfkgcefnnjajsrqnwqjligdgwshgudwtswrdnfzrvqpvcjanvfbkaoykyzvjugwcdmyxzjxoynuuewvjqrvapfcbulcaplshpgvjithcvvklszenadnkejwkwzmzuyqmedjhgaongcowisexptzhpxbbqkslbccgufgkivrvgnbrqbeznbbxuybpvsbsicppjankfeiporftbmuhrsrrpfnqnresowwhffzffgguvkeddbozcphysxxdefilnmttunvllswisylirrlhszrbkcxefsvchwotxiwhbpzhydkmggcqjuwftskjyluvptnxegkzauezmvmtstzhphddittnsbrpsnedfhkaeapxwfyylthmguzrwezispcqnsoqyxjflkerbepjuisfriqqccvzjgaddrushpywnhirkbrcdvlhnasatsptfhrwymunnkhljvnopauzsxwxgywrzpndnvbizxzrblgngiztotethumpgkyrgtsqpzhvsbrjwbmmfzrdwlromamktqwjmikultfcpxjhilhcfzvqzkqpsjmqlmkcmpeuihxcgairnzcxctxvpljdptusylasvgzovqlpnpgqzvwszcxfgbdexyjafozrgssyqgzqpesprxdfzwtzgzbygohfpwrnpsbixqoqazakwkfphooqjdwgbgznqcgseshaijaymuiibybkfgtefiudqsnmkakykisyghdkqlsbzvjvygkoqfjojttetujtwmjweajqanfxkrgatclvsiqgdvxhabgaosnppauctcyokyiduvolewrrejwcfwwfpsrojylqqmghgyqvfvhffyxmcxrukmdgkbjtvyuddlidchdxfypteagwbwpurzhuaunainneqzvrbesvnynvfdcqvkrlkoedzcckkhdujfosntmnywzriwzaabkwhrifaofxzzxusscxzmyilpopaxrrrhctlhsecabzyasbaiqhwbhmmejvvutshybsfaqlxcvefangxbquzdlioobhfocjpitdvbzhtpgtdbhdgnpgfrfpafawwwziysbdbmzkwvulqbljqlaanshfblfgmrghropzawtxeprrqaoyegljjyekfapaqhpeoymjdpagxszetwaewbcycwmxmcriayniyzlwsnziifaysianuoygbqhubeqfjymafzeoxmawxtdxxbaobmfqdvdpkjgzhtdclfbrfwdrzstyhbukqjenudyqjgsgthgzpipizpaowcfiiafwflgltxzpijoytocluvqlmufbqxndgrtvkaktxlzllefzhnizdesmbmqzjsefwofwajcdawkqegghrhkxnzvfpskthktbyzzcbotfdvvbwdpiuskxuqujakrmnxafgrahwcfpoesbtlnuzoktzvezsxkwnxxnqlstaagjpobbdzzdzlfktgwdddemucejffgqpbisvdexpcegijmwrbtxhrimincyamurnfnhpoaupiokjhrgsrtbdlmmwypsvpzdyltkzbaknxcwbabnebrwpfaldigxptxneyiolkinegfkebeakontlolhytbdobtzguyjvzahultyysxuilxffoowovcnncwfvqvxvxjjkadsrgdivzeyfvbtygjehfirilrivkgqkagayotmyjniwhxpmvfnvkazfophffofalopxdvfuyozfzbswynuqhcnnnjnuonrojcrjbdpebvgueyvmcrmmmkrmiiyumpavhyiktejbucgolihtltpogtgcvrryuttigbcegnssfvrnnudyuheyserppzvzncfgurdzhezbadbpnniclevsszmhjnkvqrtuvuhawjsdjluodcwzvcitfcydtaxljjzttuwyufgumtvfohsqwhqlucrnlmkdnvrjmuufscnopcbaadtunhpmfhrezvbzgrgavpgzecdrampabbzwzutfjaxekccifvwbzposkmowhrggdbplpwxqdkanxltrxwakafvsmkldmistnlbtiphwhqbrkgrehxmkuartsnjklndncrobiefwxkerbyddpcymrjpbbikvtjgjnpdviljxywncccbyajkvhtnvybaetrqggdhvuhjqwwmnogvyctofzvavdnhwyrooevdwxiehztywcpaktimvvimrwqiiuiahjedvhcfmqvseugksfwququwvsjewjjxxehmgnnmunfhuvvtnlpeicojfqlxiqccqplzpbspruapavyxehvvhhtldjdvldgqwhxugrzhpibpyvhdkqkqorworgwdnzjqnfjcjqeciezzlvhygzwwllkuvsmahxfxvysqmjeltlqriibyqqsxojypvaeeobpzmuptccqcprpomxmtzjgrmnsnhqwwxhfxfcdqskjleisfgoqjoedmisahrdlgkmmbvrgljepgunaqctazghpmacembrbiepypyevwpfsodklhtpuohpwdiulbsbrsajzxdbevswppaulfewmshvvjmkffvmhtdimfjymjsuycjrwcgzbnsdmftvzraelvhjjqbbzduyzygqnfdfoyhzfltogrihfjnjpilwmdscecjolzkkhxjzxnvpjeamzknfinzzwniwqxqicqpxndlrprudfylbdxrqxqrgttyeijosqwewcuiwszzthhvcakhqhdauftuhjlrnkplynewxokycgttfkhhjorgxurnqgkxgzsinawnxszeifbpkrgbccnhnrrgzemtrbgzqduxpihcspgxjxppstwxzpymvnzowceagwdkvdwuhclqdpvufolmuhsmhwyvjxgpbxhiiayyatnujbcxmutxigryedxbwzpsjlwuvwxyiramufhutzhiblaosvskxgnhusjdhgkhcgahzutilyddnhqgpjvfjbvmselkbnfkhmodcrexrxbhgehbdustdnlgyicgdvcncmatiwcindbhhhutuayeoaqyhohztiftlhzkwjqdfiwxiltbhwjrrywcyeqgyhexeabwthtazeqzxzfjpfxgxnfyblmfgydtlitudiehnjhqbarsmijrcxkinycdkxmrsupwitonxvsirbhzuynolbbuzsfpgxnzsndmxjvqkvllcufrdkzjdgrdoyqqjxsgxsulfbbpwhggeerbsrrlzhtecjkrvllfwhzgrnhmtwvfiyzcuwcerbiuuidrgbaudrfklwhaalnvguiheitidwgjrbntdoyeuawzegcobnbetzjlzczgstoakfwwulruryadzsaoqqacmtbgrirledcnqicsmirincktndneimctlkaddlbflsrhiunnpoercwsburefswuhmrqigzaibdzyxnxvncyonlfvwhnyxwfjmordshdcqgysbqpqezevtigexnrihwygbuokniycnfloaltnkslhoakqrdkrxsdfcleyfftoitmpprkwsctkyxfphqlrbramofjzaxoiylmttaaoizgoqkxtpervzaevsulmfhnjlttctxfluwhriwcvrdkktfxsplojdrfpwxxvslxkcjoerowlcdvaozxexumcxovvbkozaeibkqlvpdhdruscqjzecyuevjvntmasjuxivkirytoynzghicbwckthidofsethngqnujwznvulhqycbuptzhydqqpbuygazggzznxjebfbuhsqzbjbhcfizzflptlagdbywrkjnfbsfjivfptvxdvcwehmkvmqiiqwsjvsdjitfixcabixbmvuxdmnjfdkqrqeymvwpdjvtlworalfxdtspmiihqdbhsuywnpkbxipdpjgrageuxfzrnksjfuogoelguesqhzoxuxmtlylknsgeazkkmzxguanriktzajslmaihdnpxauhijbufkgbyxnovexglzpzdyxmjjxrmbofyhnwbsmcrodkfamdvwzxnjamizveiaopjswwgvtnsgkbjjlpgvsuzgclajsxypscbrzdrkkcanziqggmncalhiqjakhlkfydplkojqiletisbctfzcphibuctjavyuqqrmcbfjbtenzqckmonfpgqtujahwjyulwxymaflvlkcaihphxltizzeictzjjursggitwedoniejfltmuttsgbyxfniysjkenvuasmoelrhumytjlhvgckgquhzwadoqvxajhjaqwurpprsjgqxhyrxnamifichrjirtzbxwnadvqqzoviryzvseqppehtlbumdmfcpdmcszhxjvluevhvjmsqwczrbfwcabhrsgjbquxufbyxjhbjzzpmsvpwskwhbqudjvcaxqikgynalewmlvbzugsfbwaiwkbpvszkgdjvakzzlsglevvscbmpkfsqemtqjrilkjrqxkjvsnrjcfiigyymgiosobwfkqkmayrrslfjuomhjjkvxpeuesctafwrrhfnupzxhlnzkuqghswcmpehttqngiqndfnwbifdzayvvfombqoozuhmbpqpvkbkdlmmqrmtdxhggysjrcsmlgplakaofzpmbcqiebdaspocflrrslsihrfpsvmloqnqlxbiisfdpmazoscutrjnwmjlsdjzzhidtyscwjfflxtttnyhnxbdjxetlpyvxpzlphxnpesmshypxuxhsfifzkrlzvmblucrdxkpgtnesqxiqrbrgdpezjzzgkrvklgybtyllgtzwqnqpdzqtdcljyjrpbcapqpnkfkqplqpovmksouksntnpohikxlruuoqtoykdsjsadhvnbtchatstrverslajctxshlfqywvivsndbjiswjafwmbesdnazzsackrixiivlxzksbiljhjgbhzqhxxeyxvyjqhmyskqxoezpmclxvuewdjicsqbhpjsslhtsexjxpzfieskjpweilnmcfoxxmnortmjqgbiiuaqvzxcijvxloibamkwvumhkblbqxcgajlkjchtxywpfdwgxqumyawafepcjbaduiiodzjitrqquqfwhnibzgitnlchftaatojaqaqknciaddyanvouqigxqrrsiskljdheqtimwzmdbweccdkibyzhayshykyrfbnbiylpeozcjhostzxcdgmwcfhrfxlcvomkuztsoeanzwrrwpilttxlemxcxgrgibglvwybjuualvnlnpmhpydfmnbhpgnpisuxpykznsexcfctncsiwdokdndartxguvfgxzaepdrzkwgzxglxpaccblvfobtnhbzfyuwofyvuhudwcjcxtgeguztutsnentivkbbovrogoqtxlhcqsaljhzddbtsjleizzuqsgkhhzlvbyhssaxhvlurxbtzbquzuzrqysvgoknchhzfwkvetulawwbzqjkenkufoyviahmoubajzopkewonxenmzpjrzunfislubrvwwhmjrkmuuqafkbzbhwobsnevqeoglgpatmvrpnzqdyabxmfjiyimqitpxnejdgwbgmdktrxnmtlvzasbrjwlealyvsntxhqounrbfdzkamcbygtpttgrnrjdtozapwarmxrvpmmqfeixdgyscieurckdagvolfjrzcjquwlzqhchzyykjwrqjtbngbjlacpbkevqobcieqmuovjgqbomotarpvikdchonhvqltnjgwiqifwxvkdmmmgaozzokxbtzmaadbuvmdpeaphvoqebijsqebbcbzltkjzvthhukobdtxoggyjmzwneeiibsjvzsnevcdevdfxinjanwq"
        T = "ereswethisxakuwzddblzcgpmkbzwnzdiayqlollxctiseifmnpdhacvotczgajpcklgsnylkseejouzhafykbwlnpppwmocybfg"
        Solution().minWindow(S,T).must_equal('eazkkmzxguanriktzajslmaihdnpxauhijbufkgbyxnovexglzpzdyxmjjxrmbofyhnwbsmcrodkfamdvwzxnjamizveiaopjswwgvtnsgkbjjlpgvsuzgclajsxypscbrzdrkkcanziqggmncalhiqjakhlkfydplkojqiletisbctfzcphibuctjavyuqqrmcbfjbtenzqckmonfpgqtujahwjyulwxymaflvlkcaihphxltizzeictzjjursggitwedoniejfltmuttsgbyxfniysjkenvuasmoelrhumytjlhvgckgquhzwadoqvxajhjaqwurpprsjgqxhyrxnamifichrjirtzbxwnadvqqzoviryzvseqppehtlbumdmfcpdmcszhxjvluevhvjmsqwczrbfwcabhrsgjbquxufbyxjhbjzzpmsvpwskwhbqudjvcaxqikgynalewmlvbzugsfbwaiwkbpvszkgdjvakzzlsglevvscbmpkfsqemtqjrilkjrqxkjvsnrjcfiigyymgiosobwfkqkmayrrslfjuomhjjkvxpeuesctafwrrhfnupzxhlnzkuqghswcmpehttqngiqndfnwbifdzayvvfombqoozuhmbpqpvkbkdlmmqrmtdxhggysjrcsmlgplakaofzpmbcqiebdaspocflrrslsihrfpsvmloqnqlxbiisfdpmazoscutrjnwmjlsdjzzhidtyscwjfflxtttnyhnxbdjxetlpyvxpzlphxnpesmshypxuxhsfifzkrlzvmblucrdxkpgtnesqxiqrbrgdpezjzzgkrvklgybtyllgtzwqnqpdzqtdcljyjrpbcapqpnkfkqplqpovmksouksntnpohikxlruuoqtoykdsjsadhvnbtchatstrverslajctxshlfqywvivsndbjiswjafwmbesdnazzsackrixiivlxzksbiljhjgbhzqhxxeyxvyjqhmyskqxoezpmclxvuewdjicsqbhpjsslhtsexjxpzfieskjpweilnmcfoxxmnortmjqgbiiuaqvzxcijvxloibamkwvumhkblbqxcgajlkjchtxywpfdwgxqumyawafepcjbaduiiodzjitrqquqfwhnibzgitnlchftaatojaqaqknciaddyanvouqigxqrrsiskljdheqtimwzmdbweccdkibyzhayshykyrfbnbiylpeozcjhostzxcdgmwcfhrfxlcvomkuztsoeanzwrrwpilttxlemxcxgrgibglvwybjuualvnlnpmhpydfmnbhpgnpisuxpykznsexcfctncsiwdokdndartxguvfgxzaepdrzkwgzxglxpaccblvfobtnhbzfyuwofyvuhudwcjcxtgeguztutsnentivkbbovrogoqtxlhcqsaljhzddbtsjleizzuqsgkhhzlvbyhssaxhvlurxbtzbquzuzrqysvgoknchhzfwkvetulawwbzqjkenkufoyviahmoubajzopkewonxenmzpjrzunfislubrvwwhmjrkmuuqafkbzbhwobsnevqeoglgpatmvrpnzqdyabxmfjiyimqitpxnejdgwbgmdktrxnmtlvzasbrjwlealyvsntxhqounrbfdzkamcbygtpttgrnrjdtozapwarmxrvpmmqfeixdgyscieurckdagvolfjrzcjquwlzqhchzyykjwrqjtbngbjlacpbkevqobcieqmuovjgqbomotarpvikdchonhvqltnjgwiqifwxvkdmmmg')
        # S = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdd"
        # T = "aabbcdd"
        # Solution().minWindow(S,T).must_equal("")
        