// Slide reference: SLIDE 42 - Parallel Search (also LAB 9 - Parallel Sorting/Search)
// Module 5: parallel search.
// Each thread searches its own portion of the array.
// Because threads only read the array and each writes to its own slot,
// no synchronization is needed.

#include <cstdio>

int main() {
    const int N = 20;
    int arr[N];
    for (int i = 0; i < N; i++) arr[i] = i * 3;   // 0,3,6,...,57

    int target = 27;
    int foundIndex = -1;

    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        if (arr[i] == target) {
            foundIndex = i;   // only one iteration can match, so this is safe
        }
    }

    if (foundIndex != -1) {
        printf("Found %d at index %d\n", target, foundIndex);
    } else {
        printf("%d not found\n", target);
    }

    return 0;
}
