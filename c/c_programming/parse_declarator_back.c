// the grammar that specifies a declarator, a simplified form
// dcl:       optional *'s direct-dcl
// direct-dcl name
//                  (dcl)
//                  direct-dcl()
//                  direct-dcl[optional size]

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXTOKEN  100
enum { NAME, PARENS, BRACKETS };
void dcl(void);
void dirdcl(void);
int gettoken(void);
int tokentype;
char token[MAXTOKEN];
char name[MAXTOKEN];
char datatype[MAXTOKEN];
char out[1000];

/* convert declaration to words */
main(){  
    /* 1st token on line */ 
    while (gettoken() != EOF) { 
        /* is the datatype */ 
        strcpy(datatype, token); 
        out[0] = '\0';
        /* parse rest of line */
        dcl(); 
        if (tokentype != '\n')
            printf("syntax error: %d\n", tokentype);
        printf("%s: %s %s\n", name, out, datatype); 
    }
    return 0; 
}

/* dcl:  parse a declarator */
void dcl(void){
    int ns;
    /* count *'s */
    for (ns = 0; gettoken() == '*'; ){        
        ns++;
    }
    dirdcl();
    while (ns-- > 0){
        strcat(out, " pointer to");
    }
}

/* dirdcl:  parse a direct declarator */
void dirdcl(void){
    int type;
    if (tokentype == '(') {
        /* ( dcl ) */
        dcl();

        if (tokentype != ')')
            printf("error: missing )\n");
    } else if (tokentype == NAME){

        strcpy(name, token);
    } else{        
        printf("error: expected name or (dcl)\n");
    }
    while ((type=gettoken()) == PARENS || type == BRACKETS){
        if (type == PARENS){
         strcat(out, " function returning");
     } else {
         strcat(out, " array");
         strcat(out, token);
         strcat(out, " of");
     } 

 } 
}  


#define BUFSIZE 100
static char buf[BUFSIZE]; /* buffer for ungetch */
static int bufp = 0; /* next free position in buf */

/* get a (possibly pushed-back) character */
int getch(void){
    return (bufp > 0) ? buf[--bufp] : getchar();
}


/* push character back on input */ 
void ungetch(int c){
    if (bufp >= BUFSIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}

/* return next token */
int gettoken(void){
    int c;
    char *p = token;
    while ((c = getch()) == ' ' || c == '\t') 
        ;
    if (c == '(') {
        if ((c = getch()) == ')') {
            strcpy(token, "()");
            printf("token: %s\n", token);
            return tokentype = PARENS;
        } else {
            ungetch(c);
            printf("token: %s\n", token);
            return tokentype = '(';
        }
    } else if (c == '[') {
        for (*p++ = c; (*p++ = getch()) != ']'; )
            ;
        *p = '\0';
        printf("token: %s\n", token);
        return tokentype = BRACKETS;
    } else if (isalpha(c)) {
        for (*p++ = c; isalnum(c = getch()); )
            *p++ = c;
        *p = '\0';
        ungetch(c);
        printf("token: %s\n", token);
        return tokentype = NAME;
    } else {
        printf("token: %s\n", token);
        return tokentype = c;
    }
}
