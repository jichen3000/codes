#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINES 5000
#define len(x)  (sizeof(x) / sizeof(x[0]))
// char *lineptr[4];

// int readlines(char *lineptr[], int nlines); 
// void writelines(char *lineptr[], int nlines);

void my_qsort(void *lineptr[], int left, int right, 
    int (*comp)(void *, void *));

int numcmp(char *, char *);

void writelines(char const *lineptr[], int nlines){
    while (nlines-- > 0)
        printf("%s\n", *lineptr++);
}

int main(int argc, char const *argv[]){
    int nlines;
    int is_numeric = 0;

    // is_numeric = 0;
    // char const *lineptr[] = { "Illegal month", "Jan", "Feb", "Mar" };
    // nlines = 4;
    // my_qsort((void**) lineptr, 0, nlines-1,
    //     (is_numeric ? (int (*)(void*, void*))numcmp : 
    //         (int (*)(void*, void*))strcmp)  );
    // writelines(lineptr, nlines);

    is_numeric = 1;
    char const *lineptr[] = { "3", "2", "5", "100" };
    // *lineptr = &{ "3", "2", "5", "100" };
    nlines = 4;
    my_qsort((void**) lineptr, 0, nlines-1,
        (is_numeric ? (int (*)(void*, void*))numcmp : 
            (int (*)(void*, void*))strcmp)  );
    writelines(lineptr, nlines);
    return 0;
}

void swap(void *v[],  int i, int j){
    void *temp;
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}

// comp is a pointer to a function, *comp is the function
void my_qsort(void *arr[], int left, int right, 
        int (*comp)(void *, void *)){
    int i, last;
    
    if (left >= right){
        return;
    }
    swap(arr, left, (left + right)/2);
    last = left;
    for (i = left+1; i <= right; ++i){
        if ((*comp)(arr[i], arr[left]) < 0){
            swap(arr, ++last, i);
        }
    }
    swap(arr, left, last);
    my_qsort(arr, left, last-1, comp);
    my_qsort(arr, last+1, right, comp);

}

int numcmp(char *s1, char *s2){
    double v1, v2;
    v1 = atof(s1);
    v2 = atof(s2);
    if (v1 < v2)
        return -1;
    else if (v1 > v2)
        return 1;
    else
        return 0;
}