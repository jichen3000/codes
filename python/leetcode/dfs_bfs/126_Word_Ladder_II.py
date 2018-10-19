class Solution(object):
    def findLadders(self, begin_word, end_word, words):
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
        queue = [(n-1,[begin_word])]
        visited = [n] * n
        results = []
        min_path = None
        while queue:
            cur_i, cur_l = queue.pop(0)
            # (cur_i, cur_l).p()
            cur_word = cur_l[-1]
            cur_n = len(cur_l)
            if min_path and cur_n >= min_path:
                break
            if visited[cur_i] < cur_n: continue
            visited[cur_i] = cur_n
            for i in range(n-1):
                if visited[i] >= cur_n and diff_one(cur_word, words[i]):
                    new_list = cur_l[:] + [words[i]]
                    if words[i] == end_word:
                        # new_list.p()
                        results += new_list,
                        if min_path == None:
                            min_path = len(new_list)
                    else:
                        queue.append((i, new_list))
        return results


    def findLadders(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: List[List[str]]
        """
        diff_mem = {}
        def get_diff_ones(cur_i):
            w = words[cur_i]
            if w in diff_mem:
                return diff_mem[w]
            results = set()
            for j in range(m):
                key = (j, w[:j] + w[j+1:])
                for i in mem[key]:
                    results.add(i)
            results.discard(cur_i)
            diff_mem[w] = results
            return results

        words.append(begin_word)
        n = len(words)

        from collections import defaultdict
        mem = defaultdict(set)
        m = len(begin_word)
        for i in range(n):
            w = words[i]
            if i != n-1 and w == begin_word:
                continue
            for j in range(m):
                key = (j, w[:j] + w[j+1:])
                mem[key].add(i)
        queue = [(n-1,[begin_word])]
        visited = [n] * n
        results = []
        min_path = None
        # mem.p()
        while queue:
            cur_i, cur_l = queue.pop(0)
            # (cur_i, cur_l).p()
            cur_word = cur_l[-1]
            cur_n = len(cur_l)
            if min_path and cur_n >= min_path:
                break
            if visited[cur_i] < cur_n: continue
            visited[cur_i] = cur_n
            # for i in range(n-1):
            #     if visited[cur_i] >= cur_n and diff_one(cur_word, words[i]):
            # (cur_word, get_diff_ones(cur_word)).p()
            for i in get_diff_ones(cur_i):
                # (i, get_diff_ones(cur_i)).p()
                # i.p()
                if visited[i] >= cur_n:
                    new_list = cur_l[:] + [words[i]]
                    if words[i] == end_word:
                        # new_list.p()
                        results += new_list,
                        if min_path == None:
                            min_path = len(new_list)
                    else:
                        queue.append((i, new_list))
        return results


    def findLadders(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(words)
        wn = len(begin_word)
        a2z = "abcdefghijklmnopqrstuvwxyz"
        mem = {}
        def get_next_words(cur_word):
            if cur_word in mem:
                return mem[cur_word]
            new_set = set()
            for i in range(wn):
                for c in a2z:
                    w = cur_word[:i] + c + cur_word[i+1:]
                    # w.p()
                    if w in word_set:
                        new_set.add(w)
            mem[cur_word] = new_set
            return new_set
        loop_list = [[begin_word]]
        word_set.discard(begin_word)
        results = []
        while loop_list:
            next_loop_list = []
            loop_word_set = set()
            for cur_l in loop_list:
                cur_word = cur_l[-1]
                next_words = get_next_words(cur_word)
                for w in next_words:
                    if w == end_word:
                        results += cur_l + [w],
                    next_loop_list += cur_l + [w],
                loop_word_set |= next_words
            if results:
                return results
            word_set -= loop_word_set
            loop_list = next_loop_list

        return results   
    def findLadders(self, begin_word, end_word, words):
        """
        :type begin_word: str
        :type end_word: str
        :type words: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(words)
        if end_word not in word_set:
            return []
        wn = len(begin_word)
        a2z = "abcdefghijklmnopqrstuvwxyz"
        mem = {}
        def get_next_words(cur_word):
            if cur_word in mem:
                return mem[cur_word]
            new_set = set()
            for i in range(wn):
                for c in a2z:
                    w = cur_word[:i] + c + cur_word[i+1:]
                    # w.p()
                    if w in word_set:
                        new_set.add(w)
            mem[cur_word] = new_set
            return new_set
        front_loop_list = [[begin_word]]
        back_loop_list = [[end_word]]
        from collections import defaultdict
        front_dict, back_dict = defaultdict(list), defaultdict(list)
        front_dict[begin_word] += front_loop_list[0],
        back_dict[end_word] += back_loop_list[0],
        # word_set.discard(begin_word)
        # word_set.discard(end_word)
        results = []
        while front_loop_list and back_loop_list:
            # (front_loop_list, back_loop_list).p()
            if len(front_loop_list) <= len(back_loop_list):
                cur_loop_list = front_loop_list
            else:
                cur_loop_list = back_loop_list

            next_loop_list = []
            loop_word_dict = defaultdict(list)
            for cur_l in cur_loop_list:
                cur_word = cur_l[-1]
                word_set.discard(cur_word)
                next_words = get_next_words(cur_word)
                # (cur_word,next_words).p()
                for w in next_words:
                    next_loop_list += cur_l + [w],
                    loop_word_dict[w] += next_loop_list[-1],

            if len(front_loop_list) <= len(back_loop_list):
                front_loop_list = next_loop_list
                front_dict = loop_word_dict
            else:
                back_loop_list = next_loop_list
                back_dict = loop_word_dict

            # next_loop_list.p()
            # cur_set.p()
            # (front_loop_list, back_loop_list).p()
            inter_set = set(front_dict.keys()) & set(back_dict.keys())
            if len( inter_set ) > 0:
                # inter_set.p()
                # (front_loop_list, back_loop_list).p()
                for w in inter_set:
                    front_lists = front_dict[w]
                    back_lists = back_dict[w]
                    # (front_lists,back_lists).p()
                    for fl in front_lists:
                        for bl in back_lists:
                            results += fl[:-1] + list(reversed(bl)),
                break
            # word_set -= cur_set


        return results        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findLadders("hit","cog", ["hot","dot","dog","lot","log","cog"]).must_equal(
                [
                    ["hit","hot","dot","dog","cog"],
                    ["hit","hot","lot","log","cog"]
        ])
        Solution().findLadders("red","tax", ["ted","tex","red","tax","tad","den","rex","pee"]).must_equal(
                [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]])

