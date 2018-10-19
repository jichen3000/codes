from collections import Counter
class Node:
    def __init__(self, code='', freq=0, data=None):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
        self.code = code
    def __repr__(self):
        data_str = self.data
        if self.data: 
            data_str = "'{}'".format(self.data)
        return "{}(code='{}', freq={}, data={})".format(
                self.__class__, self.code, self.freq, data_str)

    def depth_first_list(self):
        acc = [self]
        result = []
        count = 100
        index = 0
        while len(acc) > 0 and index < count:
            cur_node = acc.pop()
            result.append(cur_node)
            if cur_node.right: acc.append(cur_node.right)
            if cur_node.left: acc.append(cur_node.left)
            index += 1
        return result

            

# Enter your code here. Read input from STDIN. Print output to STDOUT
def walk_nodes(the_node, the_char):
    if the_char == "0":
        return the_node.left
    else:
        return the_node.right
    
def encode_huff(root, line):
    result = []
    node_list = root.depth_first_list()
    leaf_list = filter(lambda x: x.data, node_list)
    leaf_dict = dict([(leaf.data,leaf.code) for leaf in leaf_list])
    # return leaf_dict
    return "".join([leaf_dict[char] for char in line])

    
def decodeHuff(root , s):
    result = []
    cur_node = root
    # import ipdb; ipdb.set_trace()
    for char_01 in s:
        cur_node = walk_nodes(cur_node, char_01)
        if not cur_node:
            raise Exception("not suport this string {}".format(s))
        if cur_node.data:
            result.append(cur_node.data)
            cur_node = root
    return "".join(result)
    
def generate_huff_tree(line):
    char_list = Counter(line).most_common()
    freq = len(line)
    if freq == 1:
        return Node('1', freq, line[0])
    root = Node('', freq, None)
    cur_node = root
    for char, freq in char_list[:-2]:
        cur_node.right = Node(cur_node.code+"1", freq, char)
        cur_node.left = Node(cur_node.code+"0", cur_node.freq-freq, None)
        cur_node = cur_node.left
    char, freq = char_list[-2]
    cur_node.right = Node(cur_node.code+"1", freq, char)
    char, freq = char_list[-1]
    cur_node.left = Node(cur_node.code+"0", freq, char)
    return root


line = raw_input()
# line = "ACABADDDD"
# line = "ACABA"
root = generate_huff_tree(line)

s = encode_huff(root, line)
# print(root.depth_first_list())

print(decodeHuff(root , s))

# print(root)