#include <stdio.h>

static char daytab[2][13] = {
    {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}, 
    {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
};

int is_leap(int year){
    return year%4 == 0 && year%100 != 0 || year%400 == 0;
}

/* day_of_year: set day of year from month & day */ 
int day_of_year(int year, int month, int day)
{
    int i, leap;
    leap = is_leap(year); 
    for (i = 1; i < month; i++)
           day += daytab[leap][i];
    return day;
}

/* month_day: set month, day from day of year */
void month_day(int year, int yearday, int *pmonth, int *pday) {
    int i, leap;
    leap = is_leap(year); 
    for (i = 1; yearday > daytab[leap][i]; i++)
        yearday -= daytab[leap][i];
    *pmonth = i;
    *pday = yearday;
}

/* month_name:  return name of n-th month */
char *month_name(int n)
{
    static char *name[] = {
        "Illegal month",
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    };
    return (n < 1 || n > 12) ? name[0] : name[n];
}

int test_day_of_year(void){
    printf("%d\n", day_of_year(2013, 1, 1));
    printf("%d\n", day_of_year(2013, 12, 3));
    return 1;
}

int test_moth_day(void){
    int month, day;
    month_day(2013, 337, &month, &day);
    printf("%d, %d\n", month, day);
    return 1;
}

int main(int argc, char const *argv[]){
    test_day_of_year();
    test_moth_day();
    printf("%d\n", argc);
    printf("%s\n", *(argv+argc-1));
    return 0;
}