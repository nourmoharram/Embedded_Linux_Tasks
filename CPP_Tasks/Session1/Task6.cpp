/*
Task Description: summation the digits of integer entered by user
*/
#include<iostream>
using namespace std;


int main(void)
{
    int num=0,result=0;
    //take number from user
    cout<<"Enter the number"<<endl;
    cin>>num;
    // sum the digits of number
    for(int i=1;i<=num;i++)
    {
        result += i;
    }
    cout<<"the sum of number digits = "<<result<<endl;
    return 0;
}