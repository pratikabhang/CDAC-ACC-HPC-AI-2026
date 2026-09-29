// Slide reference: SLIDE 29 - Granularity, SLIDE 30 - Determining the Threshold (also LAB 6 - Granularity Experiment)
// Module 4: granularity experiment.
// Parallel merge sort with an editable THRESHOLD - subarrays smaller than
// THRESHOLD are sorted sequentially instead of spawning more tasks.
// Change THRESHOLD, recompile, and re-run to see the effect on timing.

#include <cstdio>
#include <cstdlib>
#include <chrono>
#include <omp.h>

int THRESHOLD = 1000;   // try changing this value, e.g. 10, 100, 10000

void merge(int* arr, int* temp, int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;

    while (i <= mid && j <= right) {
        temp[k++] = (arr[i] <= arr[j]) ? arr[i++] : arr[j++];
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];

    for (int x = left; x <= right; x++) arr[x] = temp[x];
}

void mergeSort(int* arr, int* temp, int left, int right) {
    if (left >= right) return;

    if (right - left < THRESHOLD) {
        // Small enough - sort sequentially, no new tasks.
        for (int i = left + 1; i <= right; i++) {
            int key = arr[i], j = i - 1;
            while (j >= left && arr[j] > key) { arr[j + 1] = arr[j]; j--; }
            arr[j + 1] = key;
        }
        return;
    }

    int mid = left + (right - left) / 2;

    #pragma omp task shared(arr, temp)
    mergeSort(arr, temp, left, mid);

    #pragma omp task shared(arr, temp)
    mergeSort(arr, temp, mid + 1, right);

    #pragma omp taskwait
    merge(arr, temp, left, mid, right);
}

int main() {
    const int N = 200000;
    int* arr = new int[N];
    int* temp = new int[N];

    srand(42);
    for (int i = 0; i < N; i++) arr[i] = rand() % 1000000;

    auto start = std::chrono::high_resolution_clock::now();

    #pragma omp parallel
    {
        #pragma omp single
        mergeSort(arr, temp, 0, N - 1);
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    bool sorted = true;
    for (int i = 1; i < N; i++) if (arr[i - 1] > arr[i]) sorted = false;

    printf("Threshold: %d\n", THRESHOLD);
    printf("Sorted correctly: %s\n", sorted ? "yes" : "no");
    printf("Time: %f seconds\n", elapsed.count());

    delete[] arr;
    delete[] temp;
    return 0;
}
