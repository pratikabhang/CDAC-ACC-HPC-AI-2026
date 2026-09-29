// Slide reference: SLIDE 41 - Parallel Sorting (also LAB 9 - Parallel Sorting/Search)
// Module 5: parallel sort (divide-and-conquer merge sort).
// Splits the array in half, sorts each half in parallel using tasks,
// then merges the results. A small threshold keeps task count reasonable.

#include <cstdio>
#include <cstdlib>

const int THRESHOLD = 8;

void merge(int* arr, int* temp, int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;

    while (i <= mid && j <= right) {
        temp[k++] = (arr[i] <= arr[j]) ? arr[i++] : arr[j++];
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];

    for (int x = left; x <= right; x++) arr[x] = temp[x];
}

void insertionSort(int* arr, int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i], j = i - 1;
        while (j >= left && arr[j] > key) { arr[j + 1] = arr[j]; j--; }
        arr[j + 1] = key;
    }
}

void parallelSort(int* arr, int* temp, int left, int right) {
    if (right - left < THRESHOLD) {
        insertionSort(arr, left, right);
        return;
    }

    int mid = left + (right - left) / 2;

    #pragma omp task shared(arr, temp)
    parallelSort(arr, temp, left, mid);

    #pragma omp task shared(arr, temp)
    parallelSort(arr, temp, mid + 1, right);

    #pragma omp taskwait
    merge(arr, temp, left, mid, right);
}

int main() {
    const int N = 20;
    int arr[N], temp[N];

    srand(1);
    for (int i = 0; i < N; i++) arr[i] = rand() % 100;

    printf("Before: ");
    for (int i = 0; i < N; i++) printf("%d ", arr[i]);
    printf("\n");

    #pragma omp parallel
    {
        #pragma omp single
        parallelSort(arr, temp, 0, N - 1);
    }

    printf("After:  ");
    for (int i = 0; i < N; i++) printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
