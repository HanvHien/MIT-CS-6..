#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int main(int argc, string argv[])
{
    // argument handling

    if (argc==1||argc>2)
    {
        printf("you should add 1 command line argument\n");
        return 1;
    }
    string s1 = argv[1];
    for (int i = 0, n = strlen(s1); i < n; i++)
    {
        if (!isdigit(s1[i]))
        {
            printf("you should add 1 command line argument that is an int\n");
            return 1;       
        }
    } // loop isalpha
    
    
    int k = atoi(s1);
    // conversion
    string s = GetString();
    int a;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (isalpha(s[i]))
        {
           if (islower(s[i])) 
           {  
               a = s[i] - 97 + k;
               a = a % 26;
               a = a + 97;

           }
           else if (isupper(s[i]))
            {

               a = s[i] - 65 + k;
               a = a % 26;
               a = a + 65;

           }
        printf("%c",a);   
        }
        else 
        {
            printf("%c",s[i]);
        }
    }
    printf("\n");
    return 0;
}
