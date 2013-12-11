#include <stdio.h>

#define len(arr) (sizeof(arr)/sizeof(arr[0])) 

struct point {
    int x;
    int y;
};

struct rect {
    struct point top_point;
    struct point bottom_point;
};

struct point make_point(int x, int y)
{
    struct point temp;
    temp.x = x;
    temp.y = y;
    return temp;
}

struct rect make_rect(struct point top, struct point bottom)
{
    struct rect result = {top, bottom};
    return result;
}

void add_one_rect(struct rect *source)
{
    (*source).top_point.x += 100;
    // implied parenthesization is ++(source->bottom_point.y).
    // notice '*' is always the lowest precedence.
    ++source->bottom_point.y;
}

struct key {
    char const *word;
    int count;
};

struct key_list {
    char const *word;
    int count;
    struct key_list *next;
};


int find_key(struct key const *key_pointer, char const *str)
{
    // printf("str %s\n", str);
    int index = 0;
    while(key_pointer->word != str){
        // printf("key word %s\n", key_pointer->word);
        key_pointer++;
        index++;
    }
    return index;
}

int test_struct_array(void)
{
    struct key key_arr[] = {
        "auto", 0,
        "case", 0,
        "break", 0
    };
    char const *words[] = {"auto","break","auto","auto"};
    // printf("%ld\n", sizeof(key_arr[0]));
    // printf("%ld\n", sizeof(key_arr));
    // printf("%ld\n", len(key_arr));
    // printf("%ld\n", len(words));
    // printf("%s\n", words[1]);

    for (int i = 0; i < len(words); ++i){
        int found_index = find_key(key_arr, words[i]);
        key_arr[found_index].count++;
    }
    int found_index1 = find_key(key_arr, words[0]);
    printf("key word: %s, count: %d\n", 
        key_arr[found_index1].word, key_arr[found_index1].count);
}

int test_simple(void)
{
    struct point pt1 = {1,3};
    printf("pt1: %d,%d\n", pt1.x, pt1.y);

    struct point pt2 = {1,2};
    printf("pt2: %d,%d\n", pt2.x, pt2.y);

    struct point pt3 = make_point(4,5);
    printf("pt3: %d,%d\n", pt3.x, pt3.y);

    struct rect rt1 = {pt1, pt2};
    printf("rt1: %d,%d\n", rt1.top_point.x, rt1.bottom_point.y);
    struct rect rt2 = make_rect(make_point(4,5), make_point(6,7));
    printf("rt2: %d,%d\n", rt2.top_point.x, rt2.bottom_point.y);
    add_one_rect(&rt2);
    printf("rt2: %d,%d\n", rt2.top_point.x, rt2.bottom_point.y);
}

int main(int argc, char const *argv[])
{
    // test_simple();
    test_struct_array();
    return 0;
}
