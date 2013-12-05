#include <stdio.h>

#define max(A, B) ((A) > (B) ? (A) : (B))

// it will undefine the macro max.
#undef max

#ifdef __APPLE__
    #define os "apple"
#endif

int max(int a, int b){
    printf("I am the false max \n");
    return 0;
}


int test_macro(void){
    printf("macro max %d\n", max(2,1));
}

int main(int argc, char const *argv[]){
    test_macro();
    printf("%s\n", os);
    return 0;
}