#include <stdio.h>
#include <stdarg.h>

void min_p(char const *fmt, ...)
{
    /* points to each unnamed arg in turn */
    va_list ap; 
    char const *p, *sval;
    int ival;
    double dval;
    /* make ap point to 1st unnamed arg */       
    va_start(ap, fmt); 
    for (p = fmt; *p; p++) {
        if (*p != '%') {
            putchar(*p);
            continue; 
        }
        switch (*++p) {
        case 'd':
            ival = va_arg(ap, int);
            printf("%d", ival);
            break;
        case 'f':
            dval = va_arg(ap, double);
            printf("%f", dval);
            break;
        case 's':
            for (sval = va_arg(ap, char *); *sval; sval++)
                putchar(*sval);
            break;
        default:
            putchar(*p);
            break; 
        }
    }
   va_end(ap); 
}

int main(int argc, char const *argv[])
{
    min_p("int: %d\n", 4);
    min_p("str: %s\n", "mm");
    return 0;
}