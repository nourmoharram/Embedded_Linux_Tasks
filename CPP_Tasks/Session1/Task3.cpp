/*
Task Description: Decide if the Triangle is Right Angle Triangle or not
*/
#include<iostream>
#include<math.h>
using namespace std;



bool Check(int s1, int s2, int s3)
{
    if(pow(s1,2) == (pow(s2,2)+pow(s3,2)))
    {
        return true;
    }
    return false;
}
bool max_number(int s1, int s2, int s3)
{
    bool Type = false;

    if(s1 > s2 && s1 > s3)
    {
        Type = Check(s1,s2,s3);
    }
    else if(s2 > s1 && s2 > s3)
    {
        Type = Check(s2,s1,s3);
    }
    else if(s3 > s1 && s3 > s2)
    {
        Type = Check(s3,s2,s1);
    }
    else
    {
        return Type;
    }
    return Type;
}
int main(void)
{
    int x,y,z,result;
    cout<<"Enter the size of 3 sides of triangle"<<endl;
    cin>>x>>y>>z;
    result = max_number(x, y, z);
    if(result)
    {
        cout<<"the triangle is right angle triangle"<<endl;
    }
    else
    {
        cout<<"the triangle is not right angle triangle"<<endl;
    }
    return 0;
}