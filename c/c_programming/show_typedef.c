#include <stdio.h>
#include <stdlib.h>

typedef int Length;
typedef char const *String;

typedef struct tnode *Treeptr;
typedef struct tnode {
    char *word;
    int count;
    Treeptr left;
    Treeptr right; 
} Treenode;

int main(int argc, char const *argv[])
{
    Length i = 10;
    String str = "colin";
    printf("Length type: %d\n", i);
    printf("String type: %s\n", str);
    str = (String) malloc(100);
    free((void *) str);

    printf("tnode size %ld\n", sizeof(tnode));
    return 0;
}