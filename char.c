//ILL TELL YOU IF YOUR CHARACTER IS A LETTER, A NUMBER OR A SPECIAL CHAR
#include <stdio.h>

int main()
{
    char ch;//variable declaration
	//getting char from user
    printf("Enter a single character:\n");
    scanf("%c", &ch);

	//ayo, alphabeth check(capital or lowercase letter)
    if((ch>='a'&&ch<='z') || (ch>='A'&&ch<='Z'))
    {
        printf("'%c' is a letter!", ch);
    }
    else if(ch >= '0' && ch <= '9')//checking if char is a number
    {
        printf("'%c' is a digit!", ch);
    }
    else //if it isnt a letter or number, take it as a "special character"
    {
        printf("'%c' is a special character!", ch);
    }

    return 0;
}