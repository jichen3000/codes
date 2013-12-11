#include <stdio.h>

int p_int_pointer(int *address){
    printf("point address: %p \t value: %d\n", address, *address);
    return 1;
}
int p_int(int value){
    printf("int value: %d \n", value);
    return 1;
}
int p_char_pointer(char const *address){
    printf("point address: %p \t value: %d\n", address, *address);
    return 1;
}
int p_pointer(void const *address){
    printf("point address: %p\n", address);
    return 1;
}
int p_msg(const char msg[]){
    printf("message: %s\n", msg);
    return 1;
}

int show_int(int int1){
    p_msg("This is show that when c go into a function,");
    p_msg("it always copys its argument's value.");
    p_msg("inside show_int:");  
    p_int_pointer(&int1);
    return int1;
}

int test_show_int(void){
    int x = 1;
    p_msg("before show_int:");  
    p_int_pointer(&x);

    show_int(x);

    return 1;
}

int swap(int *pointer1, int *pointer2){
    p_msg("This is show that when c go into a function,");
    p_msg("it always copys its argument's value even which is a pointer.");
    int temp;
    p_msg("inside swap:");  
    p_int_pointer(pointer1);
    p_int_pointer(pointer2);
    p_pointer(&pointer1);
    p_pointer(&pointer2);
    // p_pointer(&(&pointer2));
    temp = *pointer1;
    *pointer1 = *pointer2;
    *pointer2 = temp;

    return 1;
}

int test_swap(void){
    int x = 1, y = 2;

    p_msg("before swap:");  
    p_int_pointer(&x);
    p_int_pointer(&y);

    swap(&x, &y);

    p_msg("after swap:");  
    p_int_pointer(&x);
    p_int_pointer(&y);
    p_int_pointer(&y-10);

    return 1;
}

// this argument is a local variable.
// int strlen(const char *s){ is same
int strlen(const char s[]){
    int n;
    for (int n = 0; *s != '\0'; s++){
        n++;
    }
    return n;
}

/* strcpy:  copy t to s; pointer version 3 */
void strcpy(char *s, char *t)
{
    while (*s++ = *t++)
        ;
}

int *get_int(int *int_arr[], int index){
    return int_arr[index];
}

int test_array_pointer_in_argument(void){
    //int_arr:  array[100] of pointer to int
    int *int_arr[100];
    int a=3,b=4;
    // *int_arr = {1,2};
    // int_arr[0] = &a;
    int_arr[1] = &b;
    // *int_arr[2] = 4;
    // *int_arr[3] = 4;
    // *int_arr = {1,2,3,4,5,6,7,8};
    p_int(*get_int(int_arr, 4));
}

int test_array_point(void){
    int arr[] = {1,2,3,4,5,6,7,8};
    p_msg("show array point:");
    p_int_pointer(arr);
    p_int_pointer(&arr[0]);
    p_int_pointer(&arr[1]);
    p_int_pointer(arr+1);
    // c would not check index range
    printf("%d\n", arr[10]);
    p_int_pointer(&arr[-10]);
    p_int_pointer(arr-100);
    // it will report error
    // since an array name is not a variable.
    // p_int_pointer(arr++);
    printf("strlen: %d\n", strlen("I'm Colin Ji."));
    return 1;
}

int test_string_point(void){
    char const *point_msg;
    point_msg = "now is the time";
    p_char_pointer("now is the time");

    // amessage cannot be chagned!
    char amessage[] = "now is the time"; /* an array */
    // pmessage can be changed!
    char const *pmessage = "now is the time"; /* a pointer */
    return 1;
}

int test_simple(void){
    int x = 1, y = 2, z[10];
    int *ip; /* ip is a pointer to int */
    p_msg("ip is a pointer to int");  
    p_int_pointer(ip);
    ip = &x; /* ip now points to x */
    p_msg("ip now points to x");
    p_int_pointer(ip);
    p_int_pointer(&x);
    y = *ip;    /* y is now 1 */
    p_msg("y is now 1");
    p_int_pointer(ip);
    p_int_pointer(&y);
    *ip = 0;    /* x is now 0 */
    p_msg("x is now 0");
    p_int_pointer(ip);
    p_int_pointer(&x);
    (*ip)++;
    p_msg("x is now 1, notice must add parentheses.");
    p_int_pointer(ip);
    p_int_pointer(&x);
    ip = &z[0]; /* ip now points to z[0] */
    p_msg("ip now points to z[0]");
    p_int_pointer(ip);
    p_int_pointer(&z[0]);
    p_int_pointer(z);
}

int main(int argc, char const *argv[]){
    // test_simple();
    // test_swap();
    // test_show_int();
    // test_array_point();
    test_string_point();
    test_array_pointer_in_argument();
    return 0;
}