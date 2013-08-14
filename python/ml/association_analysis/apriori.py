
# createC1
def create_candidate_ones(dataset):
    candidate_ones = set(item  for transaction in dataset for item in transaction)
    # type frozenset can be used as the key in a dictionary;
    return [frozenset([item]) for item in candidate_ones]

# scanD
def scan_dataset(dataset, candidate_ones, support_ratio_threshold):
    item_count_float = float(len(dataset))
    def computer_ratio(candidate):
        trues = [candidate.issubset(transaction) for transaction in dataset]
        return trues.count(True) / item_count_float

    support_dict = {candidate:computer_ratio(candidate) 
        for candidate in candidate_ones}
    frequents = [key for key, value in support_dict.items() 
        if value >= support_ratio_threshold]
    return frequents, support_dict


# aprioriGen
def create_candidate_ns(cur_frequents, item_number):
    candidate_ns = []
    len_cur_frequents = len(cur_frequents)
    for i in range(len_cur_frequents):
        for j in range(i+1, len_cur_frequents):
            L1 = list(cur_frequents[i])[:item_number-2]; L2 = list(cur_frequents[j])[:item_number-2]
            L1.sort(); L2.sort()
            # why need them to equal?
            # see the P255, Figure 11.3
            if L1==L2:
                candidate_ns.append(cur_frequents[i] | cur_frequents[j])
    return candidate_ns

def apriori(dataset, support_ratio_threshold = 0.5):
    candidate_ones = create_candidate_ones(dataset)
    frequent_1s, support_dict = scan_dataset(dataset, candidate_ones, support_ratio_threshold)
    frequents = [frequent_1s]
    item_number=2
    while (len(frequents[item_number-2]) > 0):
        candidate_ns = create_candidate_ns(
            frequents[item_number-2], item_number)
        frequent_ns, support_n_dict = scan_dataset(
            dataset, candidate_ns, support_ratio_threshold)
        # why do not filter the [], using len(frequent_ns) > 0
        support_dict.update(support_n_dict)
        frequents.append(frequent_ns)
        item_number += 1
    return frequents, support_dict

# generateRules
def generate_rules(frequents, support_dict, confidence_threshold=0.7):
    rule_list = []
    for i in range(1, len(frequents)):
        for frequent_item in frequents[i]:
            element_set = [frozenset([item]) for item in frequent_item]
            if (i > 1):
                rule_list.extend(rules_from_consequences(frequent_item, 
                    element_set, support_dict, confidence_threshold))
            else:
                rule_list.extend(rules_according_confidence(frequent_item, 
                    element_set, support_dict, confidence_threshold))
    return rule_list

def rules_according_confidence(frequent_item, element_set, 
        support_dict, confidence_threshold):
    def create_rule(consequence):
        confidence = support_dict[frequent_item]/ \
                support_dict[frequent_item-consequence]
        return frequent_item-consequence, consequence, confidence
    new_rule_list = map(create_rule, element_set)
    new_rule_list = filter(lambda rule: rule[2] > confidence_threshold,
        new_rule_list)
    return new_rule_list

def rules_from_consequences(frequent_item, element_set, 
        support_dict, confidence_threshold):
    m = len(element_set[0])
    new_rule_list = []
    if (len(frequent_item) > (m + 1)):
        candidate_ns = create_candidate_ns(element_set, m + 1)
        new_rule_list.extend(rules_according_confidence(frequent_item, 
                candidate_ns, support_dict, confidence_threshold))
        new_consequences = [rule[1] for rule in new_rule_list]
        if (len(new_consequences) > 1):
            new_rule_list.extend(rules_from_consequences(frequent_item, 
                    new_consequences, support_dict, confidence_threshold))
    return new_rule_list



if __name__ == '__main__':
    from minitest import *

    with test_case("apriori"):
        dataset = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
        dataset = map(set,dataset)
        with test("scan_dataset"):
            candidate_ones = create_candidate_ones(dataset)
            candidate_ones.must_equal(
                [frozenset([1]), frozenset([2]), frozenset([3]), frozenset([4]), frozenset([5])])
            frequent_1s,support_ones_dict=scan_dataset(dataset, candidate_ones, 0.5)
            frequent_1s.must_equal(
                [frozenset([5]), frozenset([2]), frozenset([3]), frozenset([1])])
            support_ones_dict.must_equal(
                {frozenset([4]): 0.25,
                 frozenset([5]): 0.75,
                 frozenset([2]): 0.75,
                 frozenset([3]): 0.75,
                 frozenset([1]): 0.5})
            pass

        with test("apriori"):
            frequents, support_dict = apriori(dataset, support_ratio_threshold = 0.5)
            frequents.must_equal(
                [[frozenset([5]), frozenset([2]), frozenset([3]), frozenset([1])],
                 [frozenset([3, 5]), frozenset([2, 3]), frozenset([2, 5]), frozenset([1, 3])],
                 [frozenset([2, 3, 5])],
                 []])
            support_dict.must_equal(
                {frozenset([5]): 0.75,
                 frozenset([3]): 0.75,
                 frozenset([2, 3, 5]): 0.5,
                 frozenset([1, 2]): 0.25,
                 frozenset([1, 5]): 0.25,
                 frozenset([3, 5]): 0.5,
                 frozenset([4]): 0.25,
                 frozenset([2, 3]): 0.5,
                 frozenset([2, 5]): 0.75,
                 frozenset([1]): 0.5,
                 frozenset([1, 3]): 0.5,
                 frozenset([2]): 0.75})

        with test("generate_rules"):
            rules= generate_rules(frequents, 
                support_dict, confidence_threshold=0.7)
            rules.must_equal(
                [(frozenset([5]), frozenset([2]), 1.0),
                 (frozenset([2]), frozenset([5]), 1.0),
                 (frozenset([1]), frozenset([3]), 1.0)])
            pass
