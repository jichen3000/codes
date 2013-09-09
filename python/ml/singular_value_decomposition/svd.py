from numpy import *

def load_example_data():
    return[[1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [1, 1, 1, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1]]

def choose_features(sigma, threshold=0.95):
    sum_value = sum(sigma)
    feature_index = 0
    cal_sum = 0
    for value in sigma:
        cal_sum += value
        feature_index += 1
        if cal_sum >= threshold * sum_value:
            break
    return feature_index

if __name__ == '__main__':
    from minitest import *

    with test("svd"):
        dataset = load_example_data()
        u, sigma, vt = linalg.svd(dataset)
        u.p()
        sigma.p()
        vt.p()
        choose_features(sigma, 0.99).p()