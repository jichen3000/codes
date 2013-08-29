from collections import Counter

class TreeNode(object):
    def __init__(self, name, count, parent):
        self.name = name
        self.count = count
        self.node_link = None
        self.parent = parent
        self.children = {}

    def inc(self, count=1):
        self.count += count

    def disp(self, index=1):
        info = '  '*index + self.name+' '+ str(self.count)+"\n"
        for child in self.children.values():
            info += child.disp(index+1)
        return info
    __repr__ = disp


# def createTree(dataset, support_threshold=1):
#     def init_header_table():
#         items = [item for sublist in dataset for item in sublist]
#         header_table = dict(Counter(items))
#         header_table = {key: [value, None] for key, value in header_table.items() if value >= support_threshold}
#         return header_table
#     header_table = init_header_table()
#     # header_table.p()
#     if len(header_table) == 0: 
#         return None, None
#     retTree = TreeNode('Null Set', 1, None)
#     # dataset.pp()
#     for tranSet, count in dataset.items():
#         localD = {}
#         for item in tranSet:
#             if item in header_table.keys():
#                 localD[item] = header_table[item][0]
#         if len(localD) > 0:
#             orderedItems = [v[0] for v in sorted(localD.items(),
#                                      key=lambda p: p[1], reverse=True)]
#             # orderedItems.p()
#             updateTree(orderedItems, retTree, \
#                                header_table, count)
#     return retTree, header_table

def createTree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0: return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    retTree = TreeNode('Null Set', 1, None)
    for tranSet, count in dataSet.items():
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(),
                                 key=lambda  p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, \
                           headerTable, count)
    return retTree, headerTable


'''
first: 
    items = ['z', 'x', 'y', 's', 't']

tree:
    root -> 'z', 1
header_table:

'''
def updateTree(items, inTree, header_table, count):
    # items.p()
    # count.p()
    # header_table.p()
    # inTree.p()
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = TreeNode(items[0], count, inTree)
        if header_table[items[0]][1] == None:
            header_table[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(header_table[items[0]][1],
                                inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]],
                                   header_table, count)

def updateHeader(nodeToTest, targetNode):
    # nodeToTest.p()
    # targetNode.p()
    while (nodeToTest.node_link != None):
        nodeToTest = nodeToTest.node_link
    nodeToTest.node_link = targetNode

def createInitSet(dataset):
    return {frozenset(trans):1 for trans in dataset}

def ascendTree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)

def findPrefixPath(basePat, treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.node_link
    return condPats        

def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(),
                              key=lambda p: p[1])]
    # bigL.p()
    for basePat in bigL:
        # basePat.p()
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        # condPattBases.p()
        myCondTree, myHead = createTree(condPattBases, minSup)
        # newFreqSet.p()
        # if myCondTree:
        #     myCondTree.p()
        if myHead != None:
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)

if __name__ == '__main__':
    from minitest import *
    simple_dataset = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    simple_dataset = createInitSet(simple_dataset)
    # simple_dataset.p()
    with test("createTree"):
        myFPtree, myHeaderTab = createTree(simple_dataset, 3)
        # myFPtree.pp()
        myFPtree.__repr__().must_equal("  Null Set 1\n    x 1\n      s 1\n        r 1\n    z 5\n      x 3\n        y 3\n          s 2\n            t 2\n          r 1\n            t 1\n      r 1\n")
        # myHeaderTab.pp()
        # simple_dataset.pp()
        pass

    with test("findPrefixPath"):
        findPrefixPath('x', myHeaderTab['x'][1]).must_equal(
            {frozenset(['z']): 3})
        findPrefixPath('z', myHeaderTab['z'][1]).must_equal(
            {})
        findPrefixPath('r', myHeaderTab['r'][1]).must_equal(
            {frozenset(['x', 's']): 1, frozenset(['z']): 1, frozenset(['y', 'x', 'z']): 1})

    with test("mineTree"):
        freqItems = []
        mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems)
        freqItems.must_equal(
            [set(['y']),
             set(['x', 'y']),
             set(['y', 'z']),
             set(['x', 'y', 'z']),
             set(['s']),
             set(['s', 'x']),
             set(['t']),
             set(['t', 'y']),
             set(['t', 'x']),
             set(['t', 'x', 'y']),
             set(['t', 'z']),
             set(['t', 'y', 'z']),
             set(['t', 'x', 'z']),
             set(['t', 'x', 'y', 'z']),
             set(['r']),
             set(['x']),
             set(['x', 'z']),
             set(['z'])])
        # myFPtree.p()

    with test("kosarak"):
        ko_dataset = [line.split() for line in open('kosarak.dataset').readlines()]
        ko_dataset = createInitSet(ko_dataset)
        koFPtree, koHeaderTab = createTree(ko_dataset, 100000)
        koFreqList = []
        mineTree(koFPtree, koHeaderTab, 100000, set([]), koFreqList)
        koFreqList.p()
        pass



