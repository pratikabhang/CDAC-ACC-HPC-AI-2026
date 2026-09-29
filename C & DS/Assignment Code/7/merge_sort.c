#include <stdio.h>

void Merge(int a[], int low, int mid, int high)
{
    int temp[100];
    int i = low;
    int j = mid + 1;
    int k = low;

    while(i <= mid && j <= high)
    {
        if(a[i] < a[j])
            temp[k++] = a[i++];
        else
            temp[k++] = a[j++];
    }

    while(i <= mid)
    {
        temp[k++] = a[i++];
    }

    while(j <= high)
    {
        temp[k++] = a[j++];
    }

    for(i = low; i <= high; i++)
    {
        a[i] = temp[i];
    }
}

void MergeSort(int a[], int low, int high)
{
    int mid;

    if(low < high)
    {
        mid = (low + high) / 2;

        MergeSort(a, low, mid);
        MergeSort(a, mid + 1, high);

        Merge(a, low, mid, high);
    }
}

int main()
{
    int a[100], n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");

    for(i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    MergeSort(a, 0, n - 1);

    printf("Sorted Array:\n");

    for(i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}