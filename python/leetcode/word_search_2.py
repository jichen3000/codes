# https://leetcode.com/problems/word-search-ii/

from trie import Trie

def check_in_board_range(point, range_point):
    i, j = point
    m, n = range_point
    return 0 <= i and i < m and 0 <= j and j < n


def find_neighbors(point, board):
    i, j = point
    m, n = len(board), len(board[0])
    neighbor_points = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    neighbor_points = filter(lambda p: check_in_board_range(p, (m,n)), 
            neighbor_points)
    return [(p, board[p[0]][p[1]]) for p in neighbor_points]

def filter_by_prefix(word_points, neighbors, trie):
    result = []
    for word_point in word_points:
        for neighbor in neighbors:
            cur_prefix = word_point[1] + neighbor[1]
            # word_point.p()
            # neighbor.p()
            # cur_prefix.p()
            if trie.starts_with(cur_prefix):
                is_word = trie.search(cur_prefix)
                cur_path = word_point[0] + [neighbor[0]]
                found_word_point = (cur_path, 
                        cur_prefix, is_word)
                result.append(found_word_point)
    return result

def update_acc_hash(acc_hash, word_points):
    for word_point in word_points:
        cur_pos = word_point[0][-1]
        cur_list = acc_hash.get(cur_pos,[])
        cur_list.append(word_point)
        acc_hash[cur_pos] = cur_list
    return acc_hash

def filter_words(acc_hash):
    return [cur_word_point for key in acc_hash 
            for cur_word_point in  acc_hash[key] if cur_word_point[2]]

def search_in_board(words, board):
    trie = Trie.create(words+words[::-1])
    acc_hash = {}
    handled_paths = []
    pos_list = [(i,j) for i in range(len(board)) for j in range(len(board[0]))]
    while len(pos_list) > 0:
        i,j = pos_list.pop(0)
        cur_char = board[i][j]
        # ((0,0),'o',[])
        cur_word_point = ([(i,j)], cur_char)
        # [((1,0),'e'),((0,1),'a')]
        neighbors = find_neighbors((i,j),board)
        cur_words = acc_hash.get((i,j), [])
        # remove all the paths which have been handled
        cur_words = filter(lambda x: x[0] not in handled_paths, cur_words)
        filtered_prefixs = filter_by_prefix(
                cur_words+[cur_word_point], neighbors, trie)
        # [((0,1),'oa',[(0,0)])]
        update_acc_hash(acc_hash, filtered_prefixs)
        # add all the paths which have been handled
        map(lambda x: handled_paths.append(x[0]), cur_words)
        # add some position for new path
        for cur_word_point in filtered_prefixs:
            cur_pos = cur_word_point[0][-1]
            if cur_pos not in pos_list:
                pos_list.append(cur_pos)


    # return acc_hash
    word_points = filter_words(acc_hash)
    return map(lambda x: (x[1], x[0]), word_points)

if __name__ == '__main__':
    from minitest import *

    board = [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
            ]

    words = ["oath","pea","eat","rain"]

    with test(check_in_board_range):
        check_in_board_range((0,0), (3,2)).must_true()
        check_in_board_range((3,0), (3,2)).must_false()
        pass  

    with test(find_neighbors):
        find_neighbors((0,0), board).must_equal(
                [((1, 0), 'e'), ((0, 1), 'a')])

    with test(filter_by_prefix):
        trie = Trie.create(words)
        cur_word_point = ([(0,0)], "o")
        neighbors = [((1, 0), 'e'), ((0, 1), 'a')]
        filter_by_prefix([cur_word_point], 
                neighbors,trie).must_equal(
                [([(0, 0), (0, 1)], 'oa', False)])

    with test(update_acc_hash):
        acc_hash = {}
        filtered_prefixs = [([(0, 0), (0, 1)], 'oa', False)]
        update_acc_hash(acc_hash, filtered_prefixs).must_equal(
                {(0, 1): [([(0, 0), (0, 1)], 'oa', False)]})
        acc_hash.must_equal(
                {(0, 1): [([(0, 0), (0, 1)], 'oa', False)]})
    with test(search_in_board):
        search_in_board(words, board).pp()
