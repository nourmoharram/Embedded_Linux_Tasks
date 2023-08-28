/*
Task Description: multiplication table
*/
#include<iostream>
#include<math.h>
using namespace std;

void multiplication_table(int number)
{
    for(int i=1;i<=12;i++)
    {
        cout<<number<<" x "<<i<<" = "<<number*i<<endl;
    }
}

int main(void)
{
    int number=0;
    cout<<"enter the number for multiplication table"<<endl;
    cin>>number;
    multiplication_table(number);
    return 0;
}