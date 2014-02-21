#include <stdio.h>

struct list_head{
    struct list_head *next, *prev;
};

struct fox{
    int id;
    struct list_head *list;
};

#define container_of(ptr, type, member) ({  \
    const typeof( ((type *) 0) ->member ) *__mptr = (ptr);  \
    (type *)( (char *)__mptr - offsetof(type, member) ); \
})

#define hlist_entry(ptr, type, member) container_of(ptr,type,member)

/**
 * list_entry - get the struct for this entry
 * @ptr:    the &struct list_head pointer.
 * @type:   the type of the struct this is embedded in.
 * @member: the name of the list_struct within the struct.
 */
#define list_entry(ptr, type, member) \
    container_of(ptr, type, member)


int main(int argc, char const *argv[])
{
    printf("%s\n", "ok");
    return 0;
}
