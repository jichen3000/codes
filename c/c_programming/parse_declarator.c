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
// void dcl(void);
// void dirdcl(void);
// int gettoken(void);
// int tokentype;
// char token[MAXTOKEN];
// char name[MAXTOKEN];
// char datatype[MAXTOKEN];
// char out[1000];


int get_token(char const *, char *, int *);

int get_tokens()

int test_parse(void){
    char declaration[] = "  int *tmp";
    char token[1000];
    char token1[1000];
    int index = 0;
    // char *declaration = "int *";

    get_token(declaration, token, &index);
    printf("%d\n", index);
    get_token(declaration, token, &index);
    get_token(declaration, token, &index);
    printf("declaration: %s\n", declaration);
    // dcl(declaration);
    return 0;
}

/* convert declaration to words */
main(){  
    test_parse();
    return 0; 
}


// /* dcl:  parse a declarator */
// void dcl(char const *declaration, char *out)
// {
//     int ns;
//     /* count *'s */
//     for (ns = 0; gettoken() == '*'; ){        
//         ns++;
//     }
//     dirdcl();
//     while (ns-- > 0){
//         strcat(out, " pointer to");
//     }
// }

// /* dirdcl:  parse a direct declarator */
// void dirdcl(void){
//     int type;
//     if (tokentype == '(') {
//         /* ( dcl ) */
//         dcl();

//         if (tokentype != ')')
//             printf("error: missing )\n");
//     } else if (tokentype == NAME){

//         strcpy(name, token);
//     } else{        
//         printf("error: expected name or (dcl)\n");
//     }
//     while ((type=gettoken()) == PARENS || type == BRACKETS){
//         if (type == PARENS){
//          strcat(out, " function returning");
//      } else {
//          strcat(out, " array");
//          strcat(out, token);
//          strcat(out, " of");
//      } 

//  } 
// }  


int get_token(char const *declaration, char *token, int *index_pointer)
{
    int curren_char;
    int token_type=-100;
    int index=*index_pointer;
    printf("index: %d\n", index);
    char *tmp_token = token;
    do {
        curren_char = declaration[index++];
    } while (curren_char == ' ' || curren_char == '\t');
    if (curren_char == '('){
        curren_char = declaration[index++];
        if (curren_char == ')'){
            strcpy(token, "()");
            token_type = PARENS;
        } else {
            index--;
            token_type = '(';
        }
    } else if (curren_char == '[') {
        for (*tmp_token++ = curren_char; (*tmp_token++ = declaration[index++]) != ']';){
            ;
        }
        *tmp_token = '\0';
        token_type = BRACKETS;
    } else if (isalpha(curren_char)) {
        do{
            *tmp_token++ = curren_char;
            curren_char = declaration[index++];
        }while(isalnum(curren_char));
        *tmp_token = '\0';
        index--;
        token_type = NAME;
    } else {
        *tmp_token = '\0';
        token_type = curren_char;
    }
    printf("token: %s\n", token);
    printf("token_type: %d\n", token_type);
    *index_pointer = index;
    return token_type;
}

// /* return next token */
// int gettoken(void){
//     int c;
//     char *p = token;
//     while ((c = getch()) == ' ' || c == '\t') 
//         ;
//     if (c == '(') {
//         if ((c = getch()) == ')') {
//             strcpy(token, "()");
//             printf("token: %s\n", token);
//             return tokentype = PARENS;
//         } else {
//             ungetch(c);
//             printf("token: %s\n", token);
//             return tokentype = '(';
//         }
//     } else if (c == '[') {
//         for (*p++ = c; (*p++ = getch()) != ']'; )
//             ;
//         *p = '\0';
//         printf("token: %s\n", token);
//         return tokentype = BRACKETS;
//     } else if (isalpha(c)) {
//         for (*p++ = c; isalnum(c = getch()); )
//             *p++ = c;
//         *p = '\0';
//         ungetch(c);
//         printf("token: %s\n", token);
//         return tokentype = NAME;
//     } else {
//         printf("token: %s\n", token);
//         return tokentype = c;
//     }
// }
