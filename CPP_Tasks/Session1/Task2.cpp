/*
Task Description: maximum number between three values
*/
#include<iostream>
using namespace std;

int max_number(int v1, int v2, int v3)
{
    if(v1 > v2 && v1 > v3)
    {
        return v1;
    }
    else if(v2 > v1 && v2 > v3)
    {
        return v2;
    }
    return v3;
}

int main(void)
{
    int x,y,z,result;
    cout<<"Enter the 3 numbers"<<endl;
    cin>>x>>y>>z;
    result = max_number(x, y, z);
    cout<<"the maximum number = "<<result<<endl;
    return 0;
}