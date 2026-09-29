// Slide reference: SLIDE 3 - Template Metaprogramming
// Introductory example: template metaprogramming
// The compiler computes Square<5>::value at compile time, not at run time.

#include <cstdio>

template <int N>
struct Square {
    static const int value = N * N;
};

int main() {
    printf("Square of 5, computed at compile time: %d\n", Square<5>::value);
    printf("Square of 9, computed at compile time: %d\n", Square<9>::value);
    return 0;
}
