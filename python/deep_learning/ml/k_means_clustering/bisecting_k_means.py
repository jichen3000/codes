from k_means import *

from numpy import *

def matrix_row_to_list(a_matrix, row_index):
    return a_matrix[row_index, :].tolist()[0]

def first_points(data_matrix, k):
    # n = shape(data_matrix)[1]
    # centroids = mat(zeros((k,n)))
    # for j in range(n):
    #     minJ = min(data_matrix[:,j])
    #     rangeJ = float(max(data_matrix[:,j]) - minJ)
    #     centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    centroids = data_matrix[:,:k]
    return centroids


# 
def biKmeans(data_matrix, k, cal_distance_func=distEclud):
    m = shape(data_matrix)[0]
    cluster_assignment_matrix = mat(zeros((m,2)))
    centroid0 = mean(data_matrix, axis=0).tolist()[0]
    centroids =[centroid0]
    for j in range(m):
        cluster_assignment_matrix[j,1] = cal_distance_func(
            mat(centroid0), data_matrix[j,:])
    while (len(centroids) < k):
        lowest_distance_sum = inf
        for i in range(len(centroids)):
            points_in_current_cluster =data_matrix[nonzero(
                cluster_assignment_matrix[:,0].A==i)[0],:] 
            split_centroids, split_assignments = \
                kMeans(points_in_current_cluster, 2 , 
                    cal_distance_func, first_points)
            split_distance_sum = sum(split_assignments[:,1])
            not_split_distance_sum = sum(
                cluster_assignment_matrix[nonzero(cluster_assignment_matrix[:,0].A!=i)[0],1])
            # print "split_distance_sum, and notSplit: ", \
                # split_distance_sum,not_split_distance_sum
            if (split_distance_sum + \
                    not_split_distance_sum) < lowest_distance_sum:
                best_split_centroid = i
                best_new_centroids = split_centroids
                best_assignments = split_assignments.copy()
                lowest_distance_sum = split_distance_sum + \
                    not_split_distance_sum
        best_assignments[nonzero(best_assignments[:,0].A == 1)[0],0] = \
            len(centroids)
        best_assignments[nonzero(best_assignments[:,0].A == 0)[0],0] = \
            best_split_centroid
        # print 'the best_split_centroid is: ',best_split_centroid
        # print 'the len of best_assignments is: ', len(best_assignments)
        centroids[best_split_centroid] = matrix_row_to_list(best_new_centroids,0)
        # best_new_centroids[0,:].tolist()[0].pp()
        centroids.append(matrix_row_to_list(best_new_centroids,1))
        cluster_assignment_matrix[nonzero(cluster_assignment_matrix[:,0].A == \
                             best_split_centroid)[0],:]= best_assignments
    return mat(centroids), cluster_assignment_matrix

if __name__ == '__main__':
    from minitest import *

    with test_case("bisecting_k_means"):

        data_matrix = mat(get_only_dataset_from_file('test_set2.dataset'))

        with test("biKmeans"):
            centroids, assignments=biKmeans(data_matrix,3)
            sum(assignments[:,1]).must_equal(69.29242050002955)
            assignments.p()
            draw_matrix(data_matrix, show=False)
            draw_matrix(centroids,color='bo')
            pass


