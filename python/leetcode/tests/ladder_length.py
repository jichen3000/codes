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

