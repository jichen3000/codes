#include <stdio.h>
#include <stdlib.h>
// #include <stream

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

int main(){
    FILE *the_file;
	if((the_file = fopen("python/tsne/cpp_bh_tsne_v1/cpp_tests/data.dat", "r+b")) == NULL) {
		printf("Error: could not open data file.\n");
		return false;
	}
    int row_count = 5;
    int col_count = 2;
    // double *data;
    double* data = (double*) malloc(row_count * col_count * sizeof(double));
    if(*data == NULL) { printf("Memory allocation failed!\n"); exit(1); }
    fread(data, sizeof(double), row_count * col_count, the_file);
    print_matrix(data, row_count, col_count);

    fclose(the_file);

}
