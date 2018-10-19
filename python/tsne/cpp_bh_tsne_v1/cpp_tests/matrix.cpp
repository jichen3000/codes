#include <cstdio>
#include <stdlib.h>

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

void print_matrix(double* matrix, int row_count, int* col_counts){
    for (int r = 0; r < row_count; r++) {
        for(int i = col_counts[r]; i < col_counts[r + 1]; i++) {
            printf("%f\t",matrix[i]);
        }
        printf("\n");
    }
}

void print_array(double* the_array, int count) {
    for (int r = 0; r < count; r++) {
        printf("%f\t",the_array[r]);
    }
    printf("\n");
}

double* gen_matrix(int row_count, int col_count){
    double* matrix = (double*) malloc(row_count * col_count * sizeof(double));
    int row_index = 0;
    for (int r = 0; r < row_count; r++) {
        for (int c = 0; c < col_count; c++) {
            matrix[row_index+c] = row_index*1.0+c;
        }
        row_index += col_count;
    }
    // print_matrix(matrix, row_count, col_count);
    return matrix;
}

double* gen_matrix2(int row_count, int col_count){
    double* matrix = (double*) malloc(row_count * col_count * sizeof(double));
    int row_index = 0;
    for (int r = 0; r < row_count; r++) {
        for (int c = 0; c < col_count; c++) {
            matrix[row_index+c] = r*1.0;
        }
        row_index += col_count;
    }
    return matrix;
}

void matrix_sample(){
    const int row_count = 3;
    const int col_count = 4;
    double* matrix = (double*) malloc(row_count * col_count * sizeof(double));
    int row_index = 0;
    for (int r = 0; r < row_count; r++) {
        for (int c = 0; c < col_count; c++) {
            matrix[row_index+c] = r*10.0+c;
        }
        row_index += col_count;
    }
    print_matrix(matrix, row_count, col_count);
    free(matrix);
}

int main(){
    // matrix_sample();
    const int row_count = 6;
    const int col_count = 5;
    double* matrix = gen_matrix2(row_count, col_count);
    print_matrix(matrix, row_count, col_count);
    free(matrix);

    printf("\nmatrix2:\n");
    double* matrix2 = gen_matrix(row_count, col_count);
    int* col_counts = (int*) calloc(row_count+1, sizeof(int));
    col_counts[0] = 0;
    for (size_t i = 0; i < row_count; i++) {
        col_counts[i+1] = col_counts[i] + col_count;
    }
    print_matrix(matrix2, row_count, col_counts);
    print_array(matrix2, row_count * col_count);
    free(col_counts);
    free(matrix2);

    printf("ok");

}
