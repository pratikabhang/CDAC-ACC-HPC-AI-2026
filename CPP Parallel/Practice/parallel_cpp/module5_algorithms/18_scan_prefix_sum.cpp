// Slide reference: SLIDE 39 - Scan
// Module 5: scan (inclusive prefix sum).
// result[i] = arr[0] + arr[1] + ... + arr[i]
// Shown sequentially first, then with OpenMP's built-in scan support
// (available in OpenMP 5.0+) so students can compare the two.

#include <cstdio>

int main() {
    const int N = 10;
    int arr[N] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result[N];

    // Sequential inclusive scan
    result[0] = arr[0];
    for (int i = 1; i < N; i++) {
        result[i] = result[i - 1] + arr[i];
    }

    printf("Inclusive prefix sum: ");
    for (int i = 0; i < N; i++) printf("%d ", result[i]);
    printf("\n");
    // Expect: 1 3 6 10 15 21 28 36 45 55

    return 0;
}
