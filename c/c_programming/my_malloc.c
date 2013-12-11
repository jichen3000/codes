#include <stdio.h>
#include <unistd.h>

// for alignment to long
typedef long Align;

// block Myheader
union header {
    struct {
        // *ptr;
        union header *next;
        unsigned size;
    } s;
    // for alignment
    // x
    Align alignment;
};

typedef union header MyHeader;

// base;
static MyHeader empty_start;
// *freep
static MyHeader *free_start_pointer = NULL;


/* free:  put block ap in free list */
void my_free(void *ap)
{
    MyHeader *bp, *p;
    bp = (MyHeader *)ap - 1; 
    /* point to block Myheader */
    for (p = free_start_pointer; !(bp > p && bp < p->s.next); p = p->s.next){

        if (p >= p->s.next && (bp > p || bp < p->s.next)){    
            /* freed block at start or end of arena */
            break;  
        }
    }
    if (bp + bp->s.size == p->s.next) {
        bp->s.size += p->s.next->s.size;
        bp->s.next = p->s.next->s.next;
    } else {
        bp->s.next = p->s.next;
    }
    if (p + p->s.size == bp) {
        p->s.size += bp->s.size;
        p->s.next = bp->s.next;
    } else {    
        p->s.next = bp;
    }
    free_start_pointer = p; 
}
/* minimum #units to request */
#define NALLOC 1024 

/* morecore:  ask system for more memory */
static MyHeader *get_more_memory(unsigned nu)
{
    char *cp, *sbrk(int);
    MyHeader *up;
    if (nu < NALLOC){
        nu = NALLOC;
    }
    cp = sbrk(nu * sizeof(MyHeader));
    // no space at all 
    if (cp == (char *) -1){
        return NULL;
    }
    up = (MyHeader *) cp;
    up->s.size = nu;
    my_free((void *)(up+1));
    return free_start_pointer;
}

void *my_malloc(unsigned num_bytes)
{
    // *prevp;
    MyHeader *p, *pre_p;
    // *moreroce(unsigned);
    // MyHeader *get_more_memory(unsigned);
    // nunits;
    unsigned num_units;

    num_units = (num_bytes+sizeof(MyHeader)-1)/sizeof(header) + 1; 
    /* no free list yet */
    if ((pre_p = free_start_pointer) == NULL) { 
        empty_start.s.next = free_start_pointer = pre_p = &empty_start;
        empty_start.s.size = 0;
    }
    for (p = pre_p->s.next; ; pre_p = p, p = p->s.next) {
        /* big enough */
        if (p->s.size >= num_units) {  
            if (p->s.size == num_units) {
                /* exactly */
                pre_p->s.next = p->s.next;
            }
            else {              
                /* allocate tail end */
                p->s.size -= num_units;
                p += p->s.size;
                p->s.size = num_units;
            }
            free_start_pointer = pre_p;
            return (void *)(p+1);
        }
        /* wrapped around free list */
        if (p == free_start_pointer) {
            if ((p = get_more_memory(num_units)) == NULL){
            // if ((p = NULL) == NULL){
                /* none left */
                return NULL;    
            }

        }
    }
}

int main(int argc, char const *argv[])
{
    
    return 0;
}