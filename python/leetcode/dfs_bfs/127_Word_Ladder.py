def is_diff_one(str1, str2):
    diff_sum = 0
    for i in xrange(len(str1)):
        if str1[i] != str2[i]:
            diff_sum+=1
            if diff_sum >= 2:
                return False

    return True

def find_diff_one_indexes(begin_word, word_list, exclude_indexs):
    result = []
    for i in xrange(len(word_list)):
        if exclude_indexs[i] != True:
            if is_diff_one(begin_word, word_list[i]):
                result.append(i)
    return result

def find_diff_one_words(begin_word, word_list):
    result = []
    for word in word_list:
        if is_diff_one(begin_word, word):
            result.append(word)
    return result


def find_shortest(begin_word, end_word_index, word_list, exclude_indexs, cache):
    one_indexes = find_diff_one_indexes(begin_word, word_list, exclude_indexs)
    if len(one_indexes) == 0:
        cache[(begin_word, word_list[end_word_index])] = -1
        return 0
    if end_word_index in one_indexes:
        return 1
    shortest_path_count = len(word_list) + 1
    for cur_i in one_indexes:
        cur_exclude_indexs = exclude_indexs[:]
        cur_exclude_indexs[cur_i] = True
        cur_key = (word_list[cur_i],word_list[end_word_index])
        if cur_key in cache:
            cur_result = 1+cache[cur_key]
        else:
            cur_result = 1+find_shortest(word_list[cur_i], end_word_index, word_list, cur_exclude_indexs, cache)
        if cur_result > 1 and shortest_path_count > cur_result:
            shortest_path_count = cur_result
    if shortest_path_count == len(word_list) + 1:
        cache[(begin_word, word_list[end_word_index])] = 0
    else:
        cache[(begin_word, word_list[end_word_index])] = shortest_path_count
    return cache[(begin_word, word_list[end_word_index])]




class Solution(object):
    # time limit
    def ladderLength_dp_top_down(self, begin_word, end_word, word_list):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        cache = {}
        exclude_indexs = [False] * len(word_list)
        if end_word not in word_list:
            return 0
        end_index = word_list.index(end_word)
        result = find_shortest(begin_word, end_index, word_list, exclude_indexs, cache)
        if result > 0:
            result += 1
        return result

    def ladderLength(self, begin_word, end_word, word_list):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if end_word not in word_list:
            return 0
        begin_set, end_set = [begin_word], [end_word]
        visited = {}
        # visited[end_word] = True
        the_len = 1
        while len(begin_set) > 0 and len(end_set) > 0:
            # (begin_set, end_set).p()
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            temp_words = []
            for word in begin_set:
                # word.p()
                adj_words = find_diff_one_words(word, word_list)
                # adj_words.p()
                for adj_word in adj_words:
                    # (adj_word,end_set,the_len + 1).p()
                    if adj_word in end_set:
                        return the_len + 1
                    if visited.get(adj_word, False) == False:
                        temp_words.append(adj_word)
                        visited[adj_word] = True
            begin_set = temp_words
            the_len+=1
        return 0
    
class Solution(object):
    def ladderLength(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: List[List[str]]
        """
        def diff_one(sw, tw):
            m = len(sw)
            count = 0
            for i in range(m):
                if sw[i] != tw[i]:
                    count += 1
                    if count == 2:
                        return False
            return count == 1
        words.append(begin_word)
        n = len(words)
        queue = [(n-1,1)]
        visited = [n] * n
        while queue:
            cur_i, cur_n = queue.pop(0)
            # (cur_i, cur_l).p()
            cur_word = words[cur_i]
            if visited[cur_i] < cur_n: continue
            visited[cur_i] = cur_n
            for i in range(n-1):
                if visited[i] >= cur_n and diff_one(cur_word, words[i]):
                    new_len = cur_n + 1
                    if words[i] == end_word:
                        # new_list.p()
                        return new_len
                    else:
                        queue.append((i, new_len))
        return 0

# the key is generate the new word
class Solution(object):
    def ladderLength(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: List[List[str]]
        """
        wn = len(begin_word)
        a2z = "abcdefghijklmnopqrstuvwxyz"
        def add_next_words(cur_word):
            for i in range(wn):
                for c in a2z:
                    w = cur_word[:i] + c + cur_word[i+1:]
                    # w.p()
                    if w in word_set:
                        word_set.discard(w)
                        queue.append(w)
            # (cur_word, queue).p()
        word_set = set(words) 
  
        layer_count = 0
        queue = [begin_word]
        word_set.discard(begin_word)
        while queue:
            cur_len = len(queue)
            layer_count += 1
            for _ in range(cur_len):
                cur_word = queue.pop(0)
                if cur_word == end_word:
                    return layer_count
                add_next_words(cur_word)
        return 0

    def ladderLength(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: List[List[str]]
        """
        wn = len(begin_word)
        a2z = "abcdefghijklmnopqrstuvwxyz"
        def next_word_set(cur_set):
            new_set = set()
            for cur_word in cur_set:
                for i in range(wn):
                    for c in a2z:
                        w = cur_word[:i] + c + cur_word[i+1:]
                        # w.p()
                        if w in word_set:
                            new_set.add(w)
            return new_set
            # (cur_word, queue).p()
        word_set = set(words) 
        if end_word not in word_set:
            return 0
        layer_count = 1
        front, back = {begin_word}, {end_word}
        word_set.discard(begin_word)
        while front:
            # (front, back, front & back).p()
            if len(front & back) > 0:
                return layer_count
            layer_count += 1

            front = next_word_set(front)

            if len(front) > len(back):
                front, back = back, front
            word_set -= front
        return 0

## review
class Solution(object):
    ## 33mins TLE
    def ladderLength(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        n = len(words)
        words.discard(begin_word)
        if end_word not in words:
            return 0
        all_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        def get_nexts(word):
            res = []
            for i in range(len(word)):
                for c in all_chars:
                    if c == word[i]:
                        continue
                    new_word = word[:i] + c + word[i+1:]
                    # new_word.p()
                    if new_word in words:
                        res += new_word,
            return res
        def dfs(word):
            min_l = n + 1 
            next_words = get_nexts(word)

            for nw in next_words:
                if nw == end_word:
                    return 1
                words.discard(nw)
                min_l = min(min_l, dfs(nw)+1)
                words.add(nw)
            # (word, next_words, min_l).p()
            return min_l
        res = 1 + dfs(begin_word)
        if res > n: return 0
        return res
    def ladderLength(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        # n = len(words)
        # words.discard(begin_word)
        if end_word not in words:
            return 0
        all_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        def get_nexts(word):
            res = []
            for i in range(len(word)):
                for c in all_chars:
                    if c == word[i]:
                        continue
                    new_word = word[:i] + c + word[i+1:]
                    # new_word.p()
                    if new_word in words:
                        res += new_word,
            return res
        def get_nexts_by_list(words):
            res = set()
            for word in words:
                res |= set(get_nexts(word))
            return res
        currents = {begin_word}
        others = {end_word}
        count = 1
        while True:
            words -= currents
            next_words = get_nexts_by_list(currents)
            # (currents, next_words, others).p()
            if len(next_words) == 0: return 0
            if next_words & others:
                return count + 1
            if len(next_words) <= len(others):
                currents = next_words
            else:
                currents = others
                others = next_words
            # (currents, others).p()
            count += 1
        return count


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        l_set = {beginWord}
        r_set = {endWord}
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        all_c = "abcdefghijklmnopqrstuvwxyz"
        def get_next_set(cur_set, word_set):
            res = set()
            for word in cur_set:
                for i in range(len(word)):
                    for c in all_c:
                        if c == word[i]: continue
                        new_w = word[:i] + c + word[i+1:]
                        if new_w in word_set:
                            res.add(new_w)
            return res
        count = 1
        while len(l_set) > 0:
            # print l_set, word_set
            word_set -= l_set
            l_set = get_next_set(l_set, word_set)
            # print l_set
            count += 1
            if l_set & r_set:
                return count
            if len(l_set) > len(r_set):
                l_set, r_set = r_set, l_set
        return 0
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().ladderLength("a","c",["a","b","c"]).must_equal(2)
        Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]).must_equal(5)

        words = ["shanny","shinny","whinny","whiney","shiver","sharer","scarer","scaler","render","fluxes","teases","starks","clinks","messrs","crewed","donner","blurts","bettye","powell","castes","hackee","hackle","heckle","deckle","decile","defile","define","refine","repine","rapine","ravine","raving","roving","chased","roping","coping","coming","homing","pointy","hominy","homily","homely","comely","comedy","comedo","vagues","crocus","spiked","bobbed","dourer","smells","feared","wooden","stings","loafer","pleads","gaiter","meeter","denser","bather","deaves","wetted","pleats","cadger","curbed","grover","hinged","budget","gables","larked","flunks","fibbed","bricks","bowell","yonder","grimes","clewed","triads","legion","lacier","ridden","bogied","camper","damien","spokes","flecks","goosed","snorer","choked","choler","leakey","vagued","flumes","scanty","bugger","tablet","nilled","julies","roomed","ridges","snared","singes","slicks","toiled","verged","shitty","clicks","farmed","stunts","dowsed","brisks","skunks","linens","hammer","naiver","duster","elates","kooked","whacky","mather","loomed","soured","mosses","keeled","drains","drafty","cricks","glower","brayed","jester","mender","burros","arises","barker","father","creaks","prayed","bulges","heaped","called","volley","girted","forded","huffed","bergen","grated","douses","jagger","grovel","lashes","creeds","bonier","snacks","powder","curled","milker","posers","ribbed","tracts","stoked","russel","bummer","cusses","gouged","nailed","lobbed","novels","stands","caches","swanks","jutted","zinged","wigged","lunges","divers","cranny","pinter","guides","tigers","traces","berber","purges","hoaxer","either","bribed","camped","funked","creaky","noises","paused","splits","morrow","faults","ladies","dinged","smoker","calved","deters","kicker","wisher","ballad","filled","fobbed","tucker","steams","rubber","staled","chived","warred","draped","curfew","chafed","washer","tombed","basket","limned","rapped","swills","gashed","loaner","settee","layers","bootee","rioted","prance","sharps","wigner","ranted","hanker","leaden","groped","dalian","robbed","peeled","larder","spoofs","pushed","hallie","maiden","waller","pashas","grains","pinked","lodged","zipper","sneers","bootie","drives","former","deepen","carboy","snouts","fained","wilmer","trance","bugles","chimps","deeper","bolder","cupped","mauser","pagers","proven","teaser","plucky","curved","shoots","barged","mantes","reefer","coater","clotho","wanner","likens","swamis","troyes","breton","fences","pastas","quirky","boiler","canoes","looted","caries","stride","adorns","dwells","hatred","cloths","rotted","spooks","canyon","lances","denied","beefed","diaper","wiener","rifled","leader","ousted","sprays","ridged","mousey","darken","guiled","gasses","suited","drools","bloody","murals","lassie","babied","fitter","lessee","chiles","wrongs","malian","leaves","redder","funnel","broths","gushes","grants","doyens","simmer","locked","spoors","berger","landed","mosley","scorns","whiten","hurled","routed","careen","chorus","chasms","hopped","cadged","kicked","slewed","shrewd","mauled","saucer","jested","shriek","giblet","gnarls","foaled","roughs","copses","sacked","blends","slurps","cashew","grades","cramps","radius","tamped","truths","cleans","creams","manner","crimps","hauled","cheery","shells","asters","scalps","quotas","clears","clover","weeder","homers","pelted","hugged","marked","moaned","steely","jagged","glades","goshes","masked","ringer","eloped","vortex","gender","spotty","harken","hasten","smiths","mulled","specks","smiles","vainer","patted","harden","nicked","dooley","begged","belief","bushel","rivers","sealed","neuter","legged","garter","freaks","server","crimea","tossed","wilted","cheers","slides","cowley","snotty","willed","bowled","tortes","pranks","yelped","slaved","silver","swords","miners","fairer","trills","salted","copsed","crusts","hogged","seemed","revert","gusted","pixies","tamika","franks","crowed","rocked","fisher","sheers","pushes","drifts","scouts","sables","sallie","shiner","coupes","napped","drowse","traced","scenes","brakes","steele","beater","buries","turned","luther","bowers","lofted","blazer","serves","cagney","hansel","talker","warmed","flirts","braced","yukked","milken","forged","dodder","strafe","blurbs","snorts","jetted","picket","pistil","valved","pewter","crawls","strews","railed","clunks","smiled","dealer","cussed","hocked","spited","cowers","strobe","donned","brawls","minxes","philby","gavels","renter","losses","packet","defied","hazier","twines","balled","gaoled","esther","narrow","soused","crispy","souped","corned","cooley","rioter","talley","keaton","rocker","spades","billie","mattel","billet","horton","navels","sander","stoker","winded","wilder","cloyed","blazed","itched","docked","greene","boozed","ticket","temped","capons","bravos","rinded","brandi","massed","sobbed","shapes","yippee","script","lesion","mallet","seabed","medals","series","phases","grower","vertex","dented","tushed","barron","toffee","bushes","mouser","zenger","quaked","marley","surfed","harmed","mormon","flints","shamed","forgot","jailor","boater","sparer","shards","master","pistol","tooted","banned","drover","spices","gobbed","corals","chucks","kitten","whales","nickel","scrape","hosted","hences","morays","stomps","marcel","hummed","wonder","stoves","distil","coffer","quaker","curler","nurses","cabbed","jigger","grails","manges","larger","zipped","rovers","stints","nudges","marlin","exuded","storey","pester","longer","creeps","meaner","wallop","dewier","rivera","drones","valued","bugled","swards","cortes","charts","benson","wreaks","glares","levels","smithy","slater","suites","paired","fetter","rutted","levied","menses","wither","woolly","weeded","planed","censer","tested","pulled","hitter","slicer","tartar","chunky","whirrs","mewled","astern","walden","hilton","cached","geller","dolled","chores","sorter","soothe","reused","clumps","fueled","hurler","helled","packed","ripped","tanned","binder","flames","teased","punker","jerked","cannon","joists","whited","sagged","heaven","hansen","grayer","turfed","cranks","stater","bunted","horsey","shakes","brands","faints","barber","gorged","creamy","mowers","scrams","gashes","knacks","aeries","sticks","altars","hostel","pumped","reeves","litter","hoaxed","mushed","guided","ripper","bought","gelled","ranker","jennie","blares","saloon","bomber","mollie","scoops","coolie","hollis","shrunk","tattle","sensed","gasket","dodoes","mapped","strips","dodges","sailed","talked","sorted","lodges","livest","pastel","ladles","graded","thrice","thales","sagger","mellon","ganged","maroon","fluked","raised","nannie","dearer","lither","triked","dorset","clamps","lonnie","spates","larded","condor","sinker","narced","quaver","atones","farted","elopes","winger","mottle","loaned","smears","joanne","boozes","waster","digger","swoops","smokey","nation","drivel","ceased","miffed","faiths","pisses","frames","fooled","milled","dither","crazed","darryl","mulder","posses","sumter","weasel","pedals","brawny","charge","welted","spanks","sallow","joined","shaker","blocks","mattie","swirls","driver","belles","chomps","blower","roared","ratted","hailed","taunts","steamy","parrot","deafer","chewed","spaces","cuffed","molded","winked","runnel","hollow","fluted","bedded","crepes","stakes","vested","parley","burton","loiter","massey","carnap","closed","bailed","milder","heists","morale","putter","snyder","damion","conned","little","pooped","ticced","cocked","halves","wishes","francs","goblet","carlin","pecked","julius","raster","shocks","dawned","loosen","swears","buried","peters","treats","noshed","hedges","trumps","rabies","ronnie","forces","ticked","bodies","proved","dadoes","halved","warner","divest","thumbs","fettle","ponies","testis","ranked","clouts","slates","tauted","stools","dodged","chancy","trawls","things","sorrow","levies","glides","battle","sauced","doomed","seller","strove","ballet","bumper","gooses","foiled","plowed","glints","chanel","petals","darted","seared","trunks","hatter","yokels","vanned","tweedy","rubles","crones","nettie","roofed","dusted","dicker","fakers","rusted","bedder","darrin","bigger","baylor","crocks","niches","tented","cashed","splats","quoted","soloed","tessie","stiles","bearer","hissed","soiled","adored","bowery","snakes","wagers","rafter","crests","plaids","cordon","listed","lawson","scared","brazos","horded","greens","marred","mushes","hooper","halter","ration","calked","erodes","plumed","mummer","pinged","curios","slated","ranter","pillow","frills","whaled","bathos","madden","totted","reamed","bellow","golfer","seaman","barred","merger","hipped","silken","hastes","strays","slinks","hooted","convex","singed","leased","bummed","leaner","molted","naught","caters","tidied","forges","sealer","gulled","plumps","racket","fitted","rafted","drapes","nasser","tamara","winced","juliet","ledger","bettie","howell","reeved","spiced","thebes","apices","dorsey","welled","feeler","warded","reader","folded","lepers","cranky","bosses","ledges","player","yellow","lunged","mattes","confer","malign","shared","brandy","filmed","rhinos","pulsed","rouses","stones","mixers","cooped","joiner","papped","liston","capote","salvos","wicker","ciders","hoofed","wefted","locket","picker","nougat","limpid","hooter","jailer","peaces","mashes","custer","wallis","purees","trends","irater","honied","wavers","tanner","change","hinges","tatted","cookie","catnap","carton","crimed","betted","veined","surges","rumped","merlin","convey","placid","harped","dianna","hookey","nobles","carted","elided","whined","glover","bleats","stales","husker","hearer","tartan","weaker","skewer","lumbar","temper","gigged","gawked","mayors","pigged","gather","valves","mitten","largos","boreas","judges","cozens","censor","frilly","dumbed","downer","jogger","scolds","danced","floras","funded","lumped","dashes","azores","quites","chunks","washed","duller","bilges","cruels","brooks","fishes","smoked","leaped","hotter","trials","heaves","rouges","kissed","sleety","manses","spites","starts","banded","clings","titted","vetoed","mister","mildew","wailed","sheets","peeked","passer","felted","broken","lieges","ruffed","bracts","buster","muffed","lanker","breaks","coffey","sighed","charms","balded","kisser","booths","leaven","cheeps","billed","lauder","bumped","career","stocks","airier","limped","jeanie","roamed","carves","lilted","router","bonnie","denver","briggs","steeps","nerves","oinked","bucked","hooves","dancer","burris","parked","swells","collie","perked","cooler","fopped","wedder","malted","sabers","lidded","conner","rogues","fought","dapper","purled","crowds","barnes","bonner","globed","goners","yankee","probes","trains","sayers","jersey","valley","vatted","tauter","dulled","mucked","jotted","border","genres","banked","filter","hitler","dipper","dollie","sieves","joliet","tilted","checks","sports","soughs","ported","causes","gelded","mooter","grills","parred","tipped","placer","slayer","glided","basked","rinses","tamper","bunged","nabbed","climbs","faeces","hanson","brainy","wicket","crowns","calmed","tarred","spires","deanne","gravel","messes","snides","tugged","denier","moslem","erased","mutter","blahed","hunker","fasten","garbed","cracks","braked","rasped","ravens","mutton","tester","tories","pinker","titled","arisen","softer","woolen","disses","likest","dicier","nagged","lipton","plumbs","manged","faulty","sacred","whiter","erases","padres","haired","captor","metals","cardin","yowled","trusts","revels","boxers","toured","spouts","sodded","judged","holley","figged","pricey","lapses","harper","beaned","sewers","caused","willie","farmer","pissed","bevies","bolled","bugler","votive","person","linton","senses","supped","mashed","pincer","wetter","tangos","sticky","lodger","loader","daunts","peaked","moused","sleeps","lasted","tasked","awards","lovely","gushed","spurts","canter","mantis","coaled","groans","dannie","oopses","sneaky","vogues","mobile","plumes","chides","theses","marcia","parser","flexed","stayed","fouler","tusked","quartz","daubed","clancy","rouged","flaked","norton","dunner","corded","shelly","hester","fucker","polled","rodger","yeager","zinced","livens","browne","gonged","pubbed","sapped","thrive","placed","jensen","moises","scopes","stumpy","stocky","heller","levers","morals","wheres","gasped","jobber","leaved","champs","rosier","pallet","shooed","parses","bender","closet","pureed","routes","verges","bulled","foster","rummer","molten","condos","better","cotter","lassos","grafts","vendor","thrace","codded","tinker","bullet","beaker","garden","spiels","popper","skills","plated","farrow","flexes","esters","brains","handel","puller","dickey","creeks","ballot","singer","sicker","spayed","spoils","rubier","missed","framed","bonnet","molder","mugger","waived","taster","robles","tracks","nearer","lister","horsed","drakes","lopped","lubber","busied","button","eluded","ceases","sought","realer","lasers","pollen","crisps","binned","darrel","crafty","gleams","lonely","gordon","harley","damian","whiles","wilton","lesser","mallow","kenyon","wimped","scened","risked","hunter","rooter","ramses","inches","goaded","ferber","freaky","nerved","spoken","lovers","letter","marrow","bulbed","braver","sloped","breads","cannes","bassos","orated","clever","darren","bredes","gouger","servos","trites","troths","flunky","jammed","bugged","watter","motive","humped","writer","pestle","rilled","packer","foists","croats","floury","napier","floors","scotty","sevens","harrow","welter","quacks","daybed","lorded","pulses","pokier","fatten","midges","joints","snoopy","looter","monies","canted","riffed","misses","bunker","piston","yessed","earner","hawked","wedged","brewer","nested","graver","hoaxes","slaves","pricks","magpie","bernie","rapier","roster","poohed","corner","trysts","rogers","whirls","bathed","teasel","opener","minced","sister","dreamy","worker","rinked","panted","triton","mervin","snowed","leafed","thinks","lesson","millet","larson","lagged","likely","stormy","fortes","hordes","wovens","kinked","mettle","seated","shirts","solver","giants","jilted","leaded","mendez","lowers","bidder","greats","pepped","flours","versus","canton","weller","cowper","tapped","dueled","mussed","rubies","bonged","steals","formed","smalls","sculls","docket","ouster","gunned","thumps","curred","withes","putted","buttes","bloats","parsed","galley","preses","tagged","hanger","planes","chords","shafts","carson","posits","zinger","solves","tensed","tastes","rinsed","kenned","bitten","leslie","chanty","candor","daises","baggie","wedded","paints","moored","haloed","hornet","lifted","fender","guiles","swifts","flicks","lancer","spares","pellet","passed","finked","joanna","bidden","swamps","lapped","leered","served","shirrs","choker","limper","marker","nudged","triter","thanks","peered","bruins","loaves","fabled","lathes","pipers","hooped","orates","burned","swines","sprats","warder","colder","crazes","reined","prized","majors","darrow","waifed","rooked","rickey","patter","shrive","gropes","gassed","throve","region","weaken","hettie","walton","galled","convoy","wesson","exudes","tinted","clanks","blinks","slacks","stilts","franny","socket","wished","kidded","knotty","turves","cashes","geared","sunned","glowed","sadden","harlem","testes","sweets","becket","blazes","batter","fellow","clovis","copier","shaped","husked","gimlet","rooney","taints","sashes","bossed","cootie","franck","probed","bagged","smocks","batten","spared","chills","relics","meyers","grader","tromps","dimmer","pasted","pepper","capped","played","junket","easier","palmed","pander","vaguer","bulged","dissed","borges","raises","wallow","jigged","bogged","burped","neater","rammed","fibers","castor","skirts","cancer","tilled","spored","dander","denims","budges","trucks","sowers","yapped","cadges","wrists","hacker","graved","vipers","noshes","minted","lessor","cassia","wrecks","hidden","brando","honeys","chilli","ragged","breded","punier","stacey","sisses","jocked","croaks","dinned","walker","heston","flares","coined","cannot","chocks","leases","wander","balder","warmer","bawled","donnie","damson","header","chilly","models","simper","watery","milked","poises","combed","toilet","gallop","sonnet","loosed","yawned","splays","pauses","bother","graphs","shrews","scones","manuel","milers","hotels","bennie","flores","spells","grimed","tenses","staged","puffer","posies","motion","fudged","fainer","tatter","seraph","nansen","months","muppet","tamera","shaman","falser","becker","lisbon","clefts","weeper","mendel","girder","takers","torsos","forked","dances","stated","yelled","scants","frothy","rolled","yodels","listen","craned","brooms","suffer","easter","shills","craves","bleeps","belled","dished","bordon","zither","jacket","lammer","kirked","shaved","atoned","frumpy","nosier","vender","graced","clingy","chants","wrests","cursed","prunes","tarter","stripe","coffee","veiled","tweeds","shrine","spines","kegged","melvin","gasser","market","marten","peeped","sanger","somber","spider","netted","radium","slings","scarfs","mended","creels","shaves","payers","bunked","movers","beings","conked","cozies","benton","codger","prints","gusset","longed","burner","jambed","mullet","fogged","scores","carbon","sleeks","helped","waxier","gilded","harlot","winces","tenser","lowell","ramsey","kennan","booted","beaver","rested","shouts","hickey","looped","swings","wonted","dilled","defers","lolled","pupped","cruets","solved","romper","defter","chokes","kithed","garnet","bookie","stared","stares","latter","lazies","fanned","wagged","dunces","corked","cloned","prided","baxter","pusses","boomed","masses","warren","weaves","delves","handed","merton","lusher","hepper","gibber","sender","parsec","snares","masher","seamed","sweats","welles","gagged","curter","mother","beeped","vealed","shoved","slaver","hacked","gutted","ranged","bashed","closer","storks","meshed","cortex","copper","severn","gripes","carlos","scares","crates","boiled","ginned","mouses","raided","greyed","verier","slopes","fenced","sniper","priced","flawed","buffed","spacey","favors","platen","miller","walled","cutter","skated","holier","beamed","waiter","drowns","clomps","quarks","bested","frisks","purged","scalds","marian","flower","howled","plover","bikers","trails","hagged","smirks","sitter","carmen","lanced","plants","nobler","yakked","thesis","lassen","margin","wagner","sifter","houses","screws","booker","dormer","meters","padded","loaded","cartel","sutton","willis","chatty","dunked","dreamt","dalton","fables","coveys","muller","shanty","adders","tailor","helper","liters","butted","maiman","hollie","gallon","xavier","shrank","mickey","rather","powers","keened","doused","kisses","flanks","dotted","phased","dumped","linger","kramer","spaced","soften","strife","rowers","hovers","crimes","crooks","carrel","braces","lander","shrove","skulks","banker","itches","dropsy","misted","pulped","cloche","fawned","states","teared","beeper","raider","groves","livery","aerier","keenan","severe","sabres","bogies","coated","harlow","tanked","mellow","cozier","shanks","spooky","blamed","tricks","sleets","punted","jumped","caxton","warped","halley","frisky","shines","skater","lumber","truces","sliced","gibbet","narked","chives","graves","gummed","holler","glazes","nieves","hushed","nought","prated","chored","cloudy","kidder","huston","straws","twined","gifted","rodney","haloes","france","wirier","mercia","rubbed","coaxed","sumner","snipes","nipper","leiden","madman","margie","footed","firmed","budded","froths","senior","hoover","tailed","glider","straps","stalks","billow","racked","javier","zoomed","shades","whores","braids","roused","sudden","dogies","fencer","snaked","flings","traded","gunner","snider","staten","levees","lathed","sailor","waited","muster","clothe","lulled","cargos","revved","sooths","flamed","borers","feller","bladed","oliver","collin","wusses","murder","parted","jailed","frayed","doored","cheeks","misled","belted","winter","merges","shaven","fudges","tabbed","forget","sloths","cachet","mealed","sassed","salter","haunts","ranger","rivets","deeded","reaped","damped","crated","youths","whacks","tamers","misery","seeped","eerier","tiller","busses","gloved","hushes","cronus","pruned","casket","direst","guilds","motley","spools","fevers","snores","greece","elides","waists","rattle","trader","juster","rashes","stoney","pipped","solder","sinner","prides","rugged","steers","gnarly","titter","cities","walter","stolen","steaks","hawker","weaned","jobbed","jacked","pikers","hipper","spoilt","beeves","craved","gotten","balked","sherry","looney","crisis","callie","swiped","fished","rooted","bopped","bowler","escher","chumps","jerrod","lefter","snooty","fillet","scales","comets","lisped","decked","clowns","horned","robber","bottle","reeled","crapes","banter","martel","dowels","brandt","sweeps","heeled","tabled","manors","danger","dionne","prayer","decker","millie","boated","damned","horses","globes","failed","lammed","nigher","joyner","sobers","chided","tipper","parcel","flakes","fugger","elated","hinder","hopper","crafts","wipers","badder","jessie","matted","wafted","pealed","cheats","elites","torres","bushed","sneaks","tidies","brings","stalls","payees","zonked","danker","poshes","smelts","stoops","warden","chicks","ramsay","budged","firmer","glazed","heated","slices","hovels","belied","shifts","pauper","tinges","weston","casted","titles","droves","roomer","modals","seamen","wearer","blonde","berlin","libbed","tensor","hokier","lambed","graped","headed","copped","eroses","fagged","filler","keener","stages","civets","spills","tithed","sullen","sucked","briton","whaler","hooded","tittle","bucket","furled","darned","planet","clucks","batted","dagger","brides","severs","pathos","grainy","relied","carpel","makers","lancet","slowed","messed","ravels","faster","gabbed","chance","grayed","santos","spends","chinos","saints","swirly","dories","wilson","milton","clangs","manual","nodded","signer","stript","etched","vaster","wastes","stored","minces","purred","marvin","pinned","skulls","heaved","wadded","fowled","hashed","mullen","relief","hatted","primed","chaffs","canned","lackey","showed","shandy","chases","maggie","deafen","bussed","differ","worked","marted","ducked","socked","fussed","greyer","herder","trusty","follow","samson","babies","whorls","stanks","manson","cranes","murrow","shrink","genius","holder","lenses","yucked","termed","ruined","junker","belies","joshed","cooled","basted","greeks","fuller","healer","carver","havens","drunks","sucker","lotion","glared","healed","pocked","rifles","weaved","canoed","punter","hinton","settle","boobed","hinted","scored","harder","status","sloven","hayden","golfed","scoots","bloods","slaked","jugged","louses","cassie","shaded","rushed","pitied","barked","honked","rasher","forced","shaver","vowels","holden","pelvis","blades","chests","preyer","floods","deanna","cation","mapper","falter","dabbed","mocker","nestle","shucks","heeded","ticker","binges","summer","slumps","lusted","scampi","crofts","gorges","pardon","torses","smokes","lashed","bailey","jabbed","calmer","preset","forbes","hasted","wormed","winged","minors","banner","grazed","hewers","kernel","jolted","sniped","clunky","ratios","blinds","ganges","misers","spikes","riders","hallow","grumpy","barren","summed","infers","places","jarred","killer","plaint","goofed","subbed","prudes","sipped","kookie","whines","droopy","palled","cherry","proves","mobbed","spaded","cheese","pluses","bathes","motels","spewed","soaked","howler","puffed","malled","shrike","slided","fulled","pouted","shames","lessen","ringed","teemed","grands","linked","wooten","feuded","deaden","scents","flutes","salton"]
        Solution().ladderLength("charge","comedo",words).must_equal(42)


