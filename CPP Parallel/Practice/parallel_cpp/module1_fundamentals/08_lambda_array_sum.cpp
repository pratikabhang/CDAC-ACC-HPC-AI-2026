// Slide reference: SLIDE 4 - Lambda Expressions
// Module 1: sum an array two ways - a plain loop, and std::for_each + lambda.
// Shows that a lambda can replace a small loop body without changing behavior.

#include <cstdio>
#include <algorithm>

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = 10;

    // Plain loop
    int sumLoop = 0;
    for (int i = 0; i < n; i++) {
        sumLoop += arr[i];
    }

    // Same computation using std::for_each and a lambda
    int sumLambda = 0;
    std::for_each(arr, arr + n, [&sumLambda](int x) { sumLambda += x; });

    printf("Sum (plain loop):   %d\n", sumLoop);
    printf("Sum (lambda-based): %d\n", sumLambda);

    return 0;
}
