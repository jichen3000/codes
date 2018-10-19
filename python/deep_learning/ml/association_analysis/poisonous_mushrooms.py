from apriori import *

def get_only_dataset_from_file(filename, split_format="\t", type_func=float):
    with open(filename) as datafile:
        words = [line.strip().split(split_format) for line in datafile]
    dataset = [ [type_func(cell) for cell in row] for row in words]
    return dataset


if __name__ == '__main__':
    from minitest import *

    with test_case("poisonous_mushrooms"):
        dataset = get_only_dataset_from_file("mushroom.dataset",
            split_format=" ", type_func=str)
        dataset[0].p()
        with test("some"):
            frequents, support_dict = apriori(dataset, support_ratio_threshold = 0.5)
            # frequents.size().pp()
            # frequents.pp()
            # support_dict.size().pp()
            [item for item in frequents[1] if item.intersection('2')].p()
            [item for item in frequents[3] if item.intersection('2')].p()
            # filter(lambda item: item.intersection(2), frequents[1]).pp()
            pass