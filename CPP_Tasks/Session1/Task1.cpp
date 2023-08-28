/*
Task Description: Create a table for AscII code
*/
#include<iostream>
using namespace std;


int main(void)
{
    char letter = 'A';
    for(int i=0;i<26;i++)
    {
        cout<<"|  "<<char(65+i)<<" | "<<65+i<<" |"<<endl;
    }
    return 0;
}