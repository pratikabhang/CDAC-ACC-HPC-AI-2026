#include<iostream>
using namespace std;

int SumOfDigits(int n)
{
    int r = n % 10;
    int d = n / 10;
    if(n==0)
    {
        return 0;
    }

    return r + SumOfDigits(d);
}

int main()
{
    int n, ans;

    cout<<"Enter Number: ";
    cin>>n;

    ans = SumOfDigits(n);

    cout<<"Sum Of Digits = "<<ans;

    return 0;
}