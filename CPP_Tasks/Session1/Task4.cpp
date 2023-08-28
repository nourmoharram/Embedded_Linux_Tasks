/*
Task Description: decide the letter is vowel or not
*/
#include <cctype>
#include <ios>
#include<iostream>
#include<string.h>
using namespace std;

bool Is_Vowel(char letter)
{
    char vowels[5]={'a','e','i','o','u'};
    for(int i=0;i<5;i++)
    {
        if(tolower(letter)==vowels[i])
        {
            return true;
        }
    }
    return false;
}

int main(void)
{
    char letter;
    cout<<"enter the letter for check"<<endl;
    cin>>letter;
    cout<<boolalpha<<" "<<Is_Vowel(letter)<<endl;
    return 0;
}