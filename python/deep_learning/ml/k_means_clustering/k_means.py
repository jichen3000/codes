from numpy import *
from operator import itemgetter

def draw_matrix(data_matrix, x_column=0, y_column=1, show=True, color='ro'):
    import matplotlib.pyplot as plt
    # dataset.p()
    xs = data_matrix[:, x_column]
    ys = data_matrix[:, y_column]
    plt.plot(xs, ys,color)
    if show:
        plt.show()
    return plt


def get_only_dataset_from_file(filename):
    with open(filename) as datafile:
        words = [line.strip().split('\t') for line in datafile]
    dataset = [ [float(cell) for cell in row] for row in words]
    return dataset

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(data_matrix, k):
    n = shape(data_matrix)[1]
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(data_matrix[:,j])
        rangeJ = float(max(data_matrix[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    return centroids

def kMeans(data_matrix, k, 
        cal_distance_func=distEclud, 
        create_centers_func=randCent):
    m = shape(data_matrix)[0]
    cluster_assignment_matrix = mat(zeros((m,2)))
    centroids = create_centers_func(data_matrix, k)
    changed_flag = True
    while changed_flag:
        changed_flag = False
        for i in range(m):
            min_distance = inf
            min_index = -1
            for j in range(k):
                distJI = cal_distance_func(centroids[j,:],data_matrix[i,:])
                if distJI < min_distance:
                    min_distance = distJI
                    min_index = j
            if cluster_assignment_matrix[i,0] != min_index: 
                changed_flag = True
            cluster_assignment_matrix[i,:] = \
                    min_index,min_distance
        # print centroids
        for cent in range(k):
            rows_in_current_cluster = data_matrix[nonzero(
                cluster_assignment_matrix[:,0].A==cent)[0]]
            centroids[cent,:] = mean(rows_in_current_cluster, axis=0)
    # cluster_assignment_matrix.p()
    return centroids, cluster_assignment_matrix

def sum_distances(centroids, points):
    def get_min_distance(point):
        return min([distEclud(point, centroid) for centroid in centroids])
    return sum(map(get_min_distance ,points))

if __name__ == '__main__':
    from minitest import *

    with test_case("k_means"):

        with test("randCent"):
            data_matrix = mat(get_only_dataset_from_file('test_set.dataset'))
            # data_matrix.p()
            # draw_matrix(data_matrix, show=False)
            rand_centroids = randCent(data_matrix, 2)
            # draw_matrix(rand_centroids,color='bo')
            pass

        with test("kMeans"):
            centroids, clustAssing = kMeans(data_matrix,4)
            # centroids.pp()
            # for i in range(10)
            draw_matrix(data_matrix, show=False)
            draw_matrix(centroids,color='bo')
            pass

        with test("sum_distances"):
            sample_centroids = mat([
                [0,0],
                [1,1]])
            sample_points = mat([
                [2,2],
                [-1,-1],
                [-2, -2]])
            sum_distances(sample_centroids, sample_points).must_equal(
                5.6568542494923806)
            pass


