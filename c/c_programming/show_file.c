#include <stdio.h>
#include <stdlib.h>

/* filecopy:  copy file ifp to file ofp */
void filecopy(FILE *ifp, FILE *ofp)
{
    int c;
    while ((c = getc(ifp)) != EOF){
        putc(c, ofp);
    }
}

int test_output_file()
{
    char const *file_name;
    FILE *fp;

    file_name = "show_file.c";
    // file_name = "cc.c";
    if ((fp = fopen(file_name, "r")) == NULL) {
        fprintf(stderr, "cat: can't open %s\n", file_name);
        exit(1);
    } else {
        filecopy(fp, stdout);
        fclose(fp);
    } 
    return 0;

}

int test_fgets()
{
    char const *file_name;
    char *lines;
    FILE *fp;

    file_name = "show_file.c";
    if ((fp = fopen(file_name, "r")) == NULL) {
        fprintf(stderr, "cat: can't open %s\n", file_name);
        exit(1);
    } else {
        fgets(lines, 100, fp);
        fputs(lines, stdout);
        // filecopy(fp, stdout);
        fclose(fp);
    } 
}

// cannot find the syscalls.h
#include <unistd.h>
int use_sys_call(void)
{
    char buf[BUFSIZ];
    int n;

    while ((n = read(0, buf, BUFSIZ)) > 0)
       write(1, buf, n);
    return 0; 
}

main(int argc, char *argv[])
{
    // test_output_file();
    int result = system("date");
    printf("system date %d\n", result);
    return 0;
}

