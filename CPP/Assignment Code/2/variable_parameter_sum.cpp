#include<iostream>
#include<cstdarg>
using namespace std;

int Sum(int n,...)
{
    va_list list;

    va_start(list,n);

    int ans = 0;

    for(int i=0;i<n;i++)
    {
        ans = ans + va_arg(list,int);
    }

    va_end(list);

    return ans;
}

int main()
{
    cout<<"Sum = "<<Sum(3,10,20,30)<<endl;
    cout<<"Sum = "<<Sum(5,2,4,6,8,10);

    return 0;
}