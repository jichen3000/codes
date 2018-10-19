#include <math.h>
#include <float.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "vptree.h"
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;



void print_matrix(double* matrix, int row_count, int col_count){
    int row_index = 0;
    for (int r = 0; r < row_count; r++) {
        for (int c = 0; c < col_count; c++) {
            // matrix[row_index+c] = r*10.0+c;
            printf("%f\t",matrix[row_index+c]);
        }
        printf("\n");
        row_index += col_count;
    }
}


double* gen_matrix(int row_count, int col_count){
    double* matrix = (double*) malloc(row_count * col_count * sizeof(double));
    int row_index = 0;
    for (int r = 0; r < row_count; r++) {
        for (int c = 0; c < col_count; c++) {
            matrix[row_index+c] = r*1.0;
            // if (c==0) {
            //     matrix[row_index+c] = r*1.0;
            // } else {
            //     matrix[row_index+c] = row_index*1.0+c;
            // }
        }
        row_index += col_count;
    }
    // print_matrix(matrix, row_count, col_count);
    return matrix;
}

template< class T >
void pv(std::vector<T> the_array){
    for (size_t i = 0; i < the_array.size(); i++) {
        std::cout << i << " : " << the_array[i]<< std::endl;
    }
    std::cout <<"vector finished!"<< std::endl;
}

// void pd(std::vector<DataPoint> the_array){
//     std::cout << "data: ";
//     for (size_t i = 0; i < the_array.size(); i++) {
//         std::cout << the_array[i].index()<<", ";
//     }
//     std::cout << std::endl;
// }

int main(){
    int N = 10;
    int D = 5;
    int K = 4;
    int rand_seed = 2;
    double* X = gen_matrix(N,D);
    // Build ball tree on data set
    VpTree<DataPoint, euclidean_distance>* tree = new VpTree<DataPoint, euclidean_distance>();
    vector<DataPoint> obj_X(N, DataPoint(D, -1, X));
    std::srand((unsigned int) rand_seed);
    for(int n = 0; n < N; n++) obj_X[n] = DataPoint(D, n, X + n * D);
    std::random_shuffle(obj_X.begin(), obj_X.end());
    pd(obj_X);
    cout << "size:" << obj_X.size() << endl;
    // cout << "1:" << obj_X[1] << endl;
    tree->create(obj_X);

    vector<DataPoint> indices;
    vector<double> distances;
    for(int n = 0; n < N; n++) {

        // Find nearest neighbors
        indices.clear();
        distances.clear();
        tree->search(obj_X[n], K + 1, &indices, &distances);
        std::cout << n << std::endl;
        pv(indices);
        pv(distances);
    }
    free(X);
    delete tree;
}
