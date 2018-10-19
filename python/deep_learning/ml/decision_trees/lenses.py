# from chapter 3 in Mahcine Learning in Action.

import common as tree_decision

if __name__ == '__main__':
    import minitest

    with open('lenses.txt','r') as data_file:
        dataset = [line.strip().split('\t') for line in data_file]
    labels=['age', 'prescript', 'astigmatic', 'tearRate']
    dataset.pp()
    # tree = tree_decision.create_tree(dataset, labels)
    # tree.pp()
    # it just overfitting. So you can prune the tree, 
    # remove some branch which just has one or two node.
    {'tearRate': 
        {'normal': 
            {'astigmatic': 
                {'no': 
                    {'age': 
                        {'pre': 'soft',
                         'presbyopic': 
                            {'prescript': 
                                {'hyper': 'soft',
                                 'myope': 'no lenses'}
                            },
                         'young': 'soft'}
                    },
                'yes': 
                    {'prescript': 
                        {'hyper': 
                            {'age': 
                                {'pre': 'no lenses',
                                 'presbyopic': 'no lenses',
                                 'young': 'hard'}
                            },
                         'myope': 'hard'}
                    }
                }
            },
        'reduced': 'no lenses'}
    }
