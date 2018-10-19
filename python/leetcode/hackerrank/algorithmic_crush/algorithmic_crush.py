import fileinput
import time

class RangeHelper(object):
    '''
    methods for range like (start, end, value) (1, 3, 100)
    '''
    @staticmethod
    def cmp(r_one, r_two):
        if r_one[1] < r_two[0]:
            return "<"
        elif r_one[0] > r_two[1]:
            return ">"
        else:
            return "over"

    @staticmethod
    def split(r_one, r_two):
        ''' r_one and r_two is "over" '''

        # one  ----
        # two  =======        
        # one  -
        # two  =====        
        if r_one[0] == r_two[0] and r_one[1] < r_two[1]:
            # print(1)
            return {"m" : (r_one[0],   r_one[1],   r_one[2]+r_two[2]),
                    "r" : (r_one[1]+1, r_two[1],   r_two[2])}
        # one  -------
        # two  ====        
        # one  -------
        # two  =
        elif r_one[0] == r_two[0] and r_one[1] > r_two[1]:
            # print(2)
            return {"m" : (r_one[0],   r_two[1],   r_one[2]+r_two[2]),
                    "r": (r_two[1]+1, r_one[1],   r_one[2])}
        # one  ----
        # two    ====        
        # one  ----
        # two     ====        
        #     not include:
        #     one  ----   -       
        #     two     =   ====        
        elif r_one[0] < r_two[0] and r_one[1] >= r_two[0] and r_one[1] < r_two[1]:
            # print(3)
            return {"l" : (r_one[0],   r_two[0]-1, r_one[2]),
                    "m" : (r_two[0],   r_one[1],   r_one[2]+r_two[2]),
                    "r" : (r_one[1]+1, r_two[1],   r_two[2]) }
        # one    ----
        # two  ====        
        # one     ----
        # two  ====        
        #     not include:
        #     one  ----      -
        #     two  =      ====        
        elif r_one[0] > r_two[0] and r_one[0] <= r_two[1] and r_one[1] > r_two[1]:
            # print(4)
            return {"l" : (r_two[0],   r_one[0]-1, r_two[2]),
                    "m" : (r_one[0],   r_two[1],   r_one[2]+r_two[2]),
                    "r" : (r_two[1]+1, r_one[1],   r_one[2]) }
        # one  --------
        # two    ====        
        # one  -----
        # two    = 
        elif r_one[0] < r_two[0] and r_one[1] > r_two[1]:
            # print(5)
            return {"l": (r_one[0],   r_two[0]-1, r_one[2]),
                    "m" : (r_two[0],   r_two[1],   r_one[2]+r_two[2]),
                    "r": (r_two[1]+1, r_one[1],   r_one[2]) }
        # one    ----
        # two  ========
        # one    -
        # two  =====
        elif r_one[0] > r_two[0] and r_one[1] < r_two[1]:
            # print(6)
            return {"l" : (r_two[0],   r_one[0]-1, r_two[2]),
                    "m" : (r_one[0],   r_one[1],   r_one[2]+r_two[2]),
                    "r" : (r_one[1]+1, r_two[1],   r_two[2]) }
        # one    ----
        # two  ======        
        # one       -
        # two  ======        
        elif r_one[0] > r_two[0] and r_one[1] == r_two[1]:
            # print(7)
            return {"l" : (r_two[0],   r_one[0]-1, r_two[2]),
                    "m" : (r_one[0],   r_one[1],   r_one[2]+r_two[2]) }
        # one  ------
        # two    ====        
        # one  ------
        # two       =        
        elif r_one[0] < r_two[0] and r_one[1] == r_two[1]:
            # print(8)
            return {"l": (r_one[0],   r_two[0]-1, r_one[2]),
                    "m" : (r_two[0],   r_one[1],   r_one[2]+r_two[2]) }
        # one  ----
        # two  ====        
        # one  -
        # two  =
        elif r_one[0] == r_two[0] and r_one[1] == r_two[1]:
            # print(9)
            return {"m" : (r_one[0],   r_one[1],   r_one[2]+r_two[2]) }
        else:
            raise Exception("Not support this situation {}, {}".format(
                r_one, r_two))


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, 
                self.data)

class RangeBST(object):
    def __init__(self,root_data=None):
        if root_data:
            self.root = Node(root_data)
        else:
            self.root = None
        self.max_value = 0

    def _reset_max_value(self,cur_value):
        # (self.max_value, cur_value).p()
        if self.max_value < cur_value:
            self.max_value = cur_value

    def add(self, node_data):
        if self.root == None:
            self.root = Node(node_data)
            # node_data.p()
            self._reset_max_value(node_data[2])
            return self.max_value
        acc = [(self.root, node_data)]
        while len(acc) > 0:
            cur_node, cur_data = acc.pop()
            cmp_result = RangeHelper.cmp(cur_data, cur_node.data)
            if cmp_result == "over":
                split_hash = RangeHelper.split(cur_data, cur_node.data)
                if "m" in split_hash:
                    cur_node.data = split_hash["m"]
                    self._reset_max_value(cur_node.data[2])
                if "l" in split_hash:
                    if cur_node.left:
                        acc.append((cur_node.left, split_hash["l"]))
                    else:
                        cur_node.left = Node(split_hash["l"])
                        self._reset_max_value(cur_node.left.data[2])
                if "r" in split_hash:
                    if cur_node.right:
                        acc.append((cur_node.right, split_hash["r"]))
                    else:
                        cur_node.right = Node(split_hash["r"])
                        self._reset_max_value(cur_node.right.data[2])
            elif cmp_result == ">":
                if cur_node.right:
                    acc.append((cur_node.right, cur_data))
                else:
                    cur_node.right = Node(cur_data)
                    self._reset_max_value(cur_data[2])
            else:
                if cur_node.left:
                    acc.append((cur_node.left, cur_data))
                else:
                    cur_node.left = Node(cur_data)
                    self._reset_max_value(cur_data[2])
        return self.max_value
    def pre_order_list(self):
        result = []
        acc = [self.root]
        while len(acc) > 0:
            cur_node = acc.pop()
            result.append(cur_node)
            if cur_node.right: acc.append(cur_node.right)
            if cur_node.left: acc.append(cur_node.left)
        return result



def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0))
        return ret
    return wrap

@timing
def main1(files=None):
    n_list = None
    n_max = 0
    for line in fileinput.input(files=files):
        if fileinput.lineno() == 1:
            n, m = map(int, line.split(" "))
            n_list = [0 for i in range(n)]
        else:
            start_index, end_index, value =  map(int,line.split(" "))
            for i in range(start_index-1, end_index):
                n_list[i] += value
                if n_list[i] > n_max: n_max = n_list[i]
    print(n_max)
    return n_max

@timing
def main(files=None):
    tree = RangeBST()
    input_count = 0
    for line in fileinput.input(files=files):
        if fileinput.lineno() == 1:
            n, input_count = map(int, line.split(" "))
            input_count = float(input_count)
            input_count.p()
        else:
            cur_range = map(int,line.split(" "))
            tree.add(cur_range)
            if fileinput.lineno() % 1000 == 0:
                print("finish {}".format(fileinput.lineno()/input_count))

    print(tree.max_value)
    return tree.max_value

if __name__ == '__main__':
    from minitest import *

    with test(main):
        main("test.txt").p()
        # main("test3.txt").must_equal(8628)
        # main("test4.txt").must_equal(7542539201)
        # main1("test4.txt").must_equal(7542539201)
        # main1("test.txt").must_equal(7542539201)

#     with test(RangeBST):
#         tree = RangeBST()
#         tree.add((1,100,1))
#         tree.add((10,80,2))
#         tree.add((80,85,2))
#         tree.add((60,80,3))
#         tree.add((4,80,4))
#         tree.add((30,40,5))
#         tree.add((50,100,6))
#         tree.max_value.p()

    # with test(RangeBST):
    #     tree = RangeBST()
    #     tree.add((29,40,787))
    #     tree.add((9,26,219))
    #     tree.add((21,31,214))
    #     # Node((29, 31, 1001))
    #     tree.max_value.must_equal(1001)
    #     tree.add((8,22,719))
    #     # Node((21, 22, 1152))
    #     tree.max_value.must_equal(1152)
    #     # import ipdb; ipdb.set_trace()
    #     tree.add((15,23,102))
        # # Node((21, 22, 1254))
        # tree.add((11,24,83))
        # Node((21, 22, 1337))
        # tree.max_value.must_equal(1337)
        # tree.add((14,22,321))
        # # Node((21, 22, 1658))
        # tree.max_value.must_equal(1658)
        # tree.add((5,22,300))
        # # Node((21, 22, 1958))
        # tree.max_value.must_equal(1958)
        # tree.add((11,30,832))
        # # Node((21, 22, 2790))
        # tree.max_value.must_equal(2790)
        # tree.add((5,25,29))
        # # Node((21, 22, 2819))
        # tree.max_value.must_equal(2819)
        # tree.add((16,24,577))
        # Node((21, 22, 3396))
        # tree.max_value.must_equal(3396)
        # tree.add((3,10,905))
        # # Node((21, 22, 3396))
        # tree.max_value.must_equal(3396)
        # tree.add((15,22,335))
        # # Node((21, 22, 3731))
        # tree.max_value.must_equal(3731)
        # tree.add((29,35,254))
        # Node((21, 22, 3731))
        # tree.max_value.must_equal(3731)
        # tree.add((9,20,20))
        # # Node((21, 22, 3731))
        # tree.max_value.must_equal(3731)
        # tree.add((33,34,351))
        # # Node((21, 22, 3731))
        # tree.max_value.must_equal(3731)
        # tree.add((30,38,564))
        # Node((21, 22, 3731))
        # tree.pre_order_list().pp()
        # tree.max_value.must_equal(3731)
        # tree.add((11,31,969))
        # # Node((21, 22, 4700))
        # tree.pre_order_list().pp()
        # tree.max_value.must_equal(4700)
        # tree.add((3,32,11))
        # tree.add((29,35,267))
        # tree.add((4,24,531))
        # tree.add((1,38,892))
        # tree.add((12,18,825))
        # tree.add((25,32,99))
        # tree.add((3,39,107))
        # tree.add((12,37,131))
        # tree.add((3,26,640))
        # tree.add((8,39,483))
        # tree.add((8,11,194))
        # tree.add((12,37,502))
    # with test(RangeHelper.split):
    #     # one  ----
    #     # two  =======        
    #     r_one = (10, 20, 1)
    #     r_two = (10, 23, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'m': (10, 20, 3), 'r': (21, 23, 2)})
    #     # one  -
    #     # two  =====        
    #     r_one = (10, 10, 1)
    #     r_two = (10, 23, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'m': (10, 10, 3), 'r': (11, 23, 2)})

    #     # one  -------
    #     # two  ====        
    #     r_one = (10, 23, 1)
    #     r_two = (10, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'m': (10, 20, 3), 'rc': (21, 23, 1)})
    #     # one  -------
    #     # two  =
    #     r_one = (10, 23, 1)
    #     r_two = (10, 10, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'m': (10, 10, 3), 'rc': (11, 23, 1)})

    #     # one  ----
    #     # two    ====        
    #     #     not include:
    #     #     one  ----   -
    #     #     two     =   ====        
    #     r_one = (10, 20, 1)
    #     r_two = (11, 23, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 10, 1), 'm': (11, 20, 3), 'r': (21, 23, 2)})
    #     # one  ----
    #     # two     ====        
    #     r_one = (10, 20, 1)
    #     r_two = (20, 23, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 19, 1), 'm': (20, 20, 3), 'r': (21, 23, 2)})

    #     # one    ----
    #     # two  ====        
    #     #     not include:
    #     #     one  ----      -
    #     #     two  =      ====        
    #     r_one = (11, 23, 1)
    #     r_two = (10, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 10, 2), 'm': (11, 20, 3), 'r': (21, 23, 1)})
    #     # one     ----
    #     # two  ====        
    #     r_one = (20, 23, 1)
    #     r_two = (10, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 19, 2), 'm': (20, 20, 3), 'r': (21, 23, 1)})

    #     # one  --------
    #     # two    ====        
    #     r_one = (10, 23, 1)
    #     r_two = (13, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'lc': (10, 12, 1), 'm': (13, 20, 3), 'rc': (21, 23, 1)})
    #     # one  -----
    #     # two    = 
    #     r_one = (10, 23, 1)
    #     r_two = (13, 13, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'lc': (10, 12, 1), 'm': (13, 13, 3), 'rc': (14, 23, 1)})

    #     # one    ----
    #     # two  ========
    #     r_one = (13, 20, 1)
    #     r_two = (10, 23, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 12, 2), 'm': (13, 20, 3), 'r': (21, 23, 2)})
    #     # one    -
    #     # two  =====
    #     r_one = (13, 13, 1)
    #     r_two = (10, 23, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 12, 2), 'm': (13, 13, 3), 'r': (14, 23, 2)})

    #     # one    ----
    #     # two  ======        
    #     r_one = (13, 20, 1)
    #     r_two = (10, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 12, 2), 'm': (13, 20, 3)})
    #     # one       -
    #     # two  ======        
    #     r_one = (20, 20, 1)
    #     r_two = (10, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'l': (10, 19, 2), 'm': (20, 20, 3)})

    #     # one  ------
    #     # two    ====        
    #     r_one = (10, 20, 1)
    #     r_two = (13, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'lc': (10, 12, 1), 'm': (13, 20, 3)})
    #     # one  ------
    #     # two       =
    #     r_one = (10, 20, 1)
    #     r_two = (20, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'lc': (10, 19, 1), 'm': (20, 20, 3)})

    #     # one  ----
    #     # two  ====        
    #     r_one = (10, 20, 1)
    #     r_two = (10, 20, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'mc': (10, 20, 3)})
    #     # one  -
    #     # two  =
    #     r_one = (10, 10, 1)
    #     r_two = (10, 10, 2)
    #     RangeHelper.split(r_one, r_two).must_equal(
    #             {'mc': (10, 10, 3)})

    # with test(RangeHelper.cmp):
    #     r_one = (10, 20, 1)
    #     r_two = (10, 20, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             "over")
    #     r_one = (10, 20, 1)
    #     r_two = (13, 20, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             "over")
    #     r_one = (13, 20, 1)
    #     r_two = (10, 23, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             "over")
    #     r_one = (13, 13, 1)
    #     r_two = (10, 23, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             "over")
    #     r_one = (1, 10, 1)
    #     r_two = (20, 23, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             "<")
    #     r_one = (1, 1, 1)
    #     r_two = (2, 2, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             "<")
    #     r_one = (11, 20, 1)
    #     r_two = (1, 10, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             ">")
    #     r_one = (2, 2, 1)
    #     r_two = (1, 1, 2)
    #     RangeHelper.cmp(r_one, r_two).must_equal(
    #             ">")

