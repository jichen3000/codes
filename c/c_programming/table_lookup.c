#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct table_entry{
    struct table_entry *next;
    char *name;
    char *replacement;
};

#define HASH_SIZE 101

// static struct table_entry *hash_table[HASH_SIZE];


unsigned hash(char const *str)
{
    unsigned hash_value;
    for (hash_value = 0; *str != '\0'; str++){
        hash_value = *str + 31 * hash_value;
    }
    // return hash_value % HASH_SIZE;
    return 1;
}

struct table_entry *lookup(struct table_entry *hash_table[], 
    char const *str)
{
    struct table_entry *the_table_entry;

    for (the_table_entry = hash_table[hash(str)]; 
        the_table_entry != NULL && the_table_entry->name!=NULL; 
        the_table_entry = the_table_entry->next){
        if (strcmp(str, the_table_entry->name) == 0){
            // printf("%s\n", "return the_table_entry");
            return the_table_entry;     
        }
    }
    // printf("%s\n", "return null");
    return NULL;           
}

void *checked_malloc(long num_bytes)
{
    void *pointer;
    if ((pointer = malloc(num_bytes)) == NULL){
        /* raise error */
    }
    return pointer;
}

char *checked_strdup(char const *str)
{
    char *result;
    if ((result = strdup(str)) == NULL){
        /* raise error */
    }
    return result;
} 

struct table_entry *install(struct table_entry *hash_table[], 
    char const *name, char const *replacement) 
{
    struct table_entry *the_table_entry;
    unsigned hash_value;

    if ((the_table_entry = lookup(hash_table, name)) == NULL) { 
        the_table_entry = (struct table_entry *) checked_malloc(
            sizeof(*the_table_entry));
        the_table_entry->name = checked_strdup(name);
        hash_value = hash(name);
        the_table_entry->next = hash_table[hash_value];
        hash_table[hash_value] = the_table_entry;
    } else {
        free((void *) the_table_entry->replacement);
    }
    the_table_entry->replacement = checked_strdup(replacement);
    return the_table_entry; 
}

int test_hash_table(void)
{
    struct table_entry *hash_table[HASH_SIZE];
    char const *name = "colin";
    char const *name2 = "mm";
    install(hash_table, name, "chengji");
    install(hash_table, name, "chengji");
    install(hash_table, name2, "ll");
    printf("%s: %s\n", name, lookup(hash_table, name)->replacement);
    printf("%s: %s\n", name2, lookup(hash_table, name2)->replacement);
}

int main(int argc, char const *argv[])
{
    // char str[]="colin";
    // printf("%ld\n", sizeof(unsigned));
    // printf("%ld\n", sizeof(int));
    // printf("%ld\n", sizeof(long));
    // printf("%ld\n", sizeof(float));
    // printf("%ld\n", sizeof(double));
    // printf("%ld\n", sizeof(char));
    // printf("%ld\n", sizeof(table_entry));
    // printf("%ld\n", sizeof(str));

    // printf("hash: %u\n", hash(str));

    test_hash_table();
    return 0;
}