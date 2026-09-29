#include <iostream>
using namespace std;

class Box
{
private:
    int length, width, height;

public:
    Box()
    {
        length = 0;
        width = 0;
        height = 0;
    }

    Box(int l, int w, int h)
    {
        length = l;
        width = w;
        height = h;
    }

    friend class BoxCalculator;
};

class BoxCalculator
{
public:
    void calculateVolume(const Box &b)
    {
        int volume = b.length * b.width * b.height;

        cout << "\n\t========== BOX DETAILS ==========";
        cout << "\n\tBox Length  : " << b.length;
        cout << "\n\tBox Width   : " << b.width;
        cout << "\n\tBox Height  : " << b.height;
        cout << "\n\tBox Volume  : " << volume;
    }
};

int main()
{
    Box b1(10, 4, 5);
    BoxCalculator calc;

    calc.calculateVolume(b1);

    return 0;
}