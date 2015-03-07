#include <iostream>
using namespace std;

void concatString(char szTarget[], const char szSource[]){
    // find the end of the first string 
    int targetIndex = 0; 
    while(szTarget[targetIndex]){
        targetIndex++; 
    }
    // tack the second onto the end of the first 
    int sourceIndex = 0; 
    while(szSource[sourceIndex]){
        szTarget[targetIndex] = szSource[sourceIndex];
        targetIndex++;
        sourceIndex++; 
    }
    // tack on the terminating null
    szTarget[targetIndex] = '\0';   
}

const char *const pszMonths[] = {
    "invalid", 
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"};

const char* int2month(int nMonth){
    if (nMonth < 1 || nMonth > 12){
        return "invalid"; 
    }
    return pszMonths[nMonth];
}

int main(int argc, char const *argv[])
{
    char szString1[] = "123";
    char szString2[6] = "456";
    concatString(szString1, szString2);
    cout << szString1 << endl;
    cout << "string length: " << strlen(szString1) << endl;
    char szString3[100];
    cout << "string copy: " << strcpy(szString3, szString1) << endl;
    cout << "szString3: " << szString3 << endl;
    cout << "string length: " << strlen(szString3) << endl;
    cout << "strstr: " << strstr(szString3, "34") << endl;
    cout << "strcmp: " << strcmp("56", "34") << endl;
    cout << "strcmp: " << strcmp("123456", "34") << endl;
    cout << "strcmp: " << strcmp("34", "123456") << endl;

    cout << "the second month is : " << int2month(2) << endl;
    return 0;
}