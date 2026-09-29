// Slide reference: SLIDE 4 - Lambda Expressions
// Introductory example: lambda expressions
// A lambda is a small anonymous function defined right where it is used.

#include <cstdio>

int main() {
    int factor = 3;

    // [factor] captures 'factor' from the surrounding scope by value
    auto multiply = [factor](int x) { return x * factor; };

    printf("multiply(5) = %d\n", multiply(5));   // 15
    printf("multiply(7) = %d\n", multiply(7));   // 21

    return 0;
}
