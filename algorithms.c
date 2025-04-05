#include <stdio.h>
#include <stdlib.h>

// Sorting Algorithms
void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; ++i)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; ++j)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }

    while (i < n1) {
        arr[k++] = L[i++];
    }

    while (j < n2) {
        arr[k++] = R[j++];
    }

    free(L);
    free(R);
}

void merge_sort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Searching Algorithm
int binary_search(int arr[], int n, int x) {
    int left = 0;
    int right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

// Fibonacci Algorithms
void fibonacci_iterative(int n, int fib_seq[]) {
    if (n > 0) fib_seq[0] = 0;
    if (n > 1) fib_seq[1] = 1;
    for (int i = 2; i < n; ++i) {
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2];
    }
}

int fibonacci_recursive_helper(int n) {
    if (n <= 1) return n;
    return fibonacci_recursive_helper(n - 1) + fibonacci_recursive_helper(n - 2);
}

void fibonacci_recursive(int n, int fib_seq[]) {
    for (int i = 0; i < n; ++i) {
        fib_seq[i] = fibonacci_recursive_helper(i);
    }
}

void fibonacci_dynamic(int n, int fib_seq[]) {
    if (n > 0) fib_seq[0] = 0;
    if (n > 1) fib_seq[1] = 1;
    for (int i = 2; i < n; ++i) {
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2];
    }
}

int main() {
    printf("Available algorithms:\n");
    printf("1. bubble_sort\n");
    printf("2. merge_sort\n");
    printf("3. binary_search\n");
    printf("4. fibonacci_iterative\n");
    printf("5. fibonacci_recursive\n");
    printf("6. fibonacci_dynamic\n");

    int choice;
    printf("Enter the number of the algorithm you would like to use: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1: {
            int n;
            printf("Enter the number of elements: ");
            scanf("%d", &n);
            int* data = (int*)malloc(n * sizeof(int));
            printf("Enter the elements: ");
            for (int i = 0; i < n; ++i) {
                scanf("%d", &data[i]);
            }
            bubble_sort(data, n);
            printf("Sorted data: ");
            for (int i = 0; i < n; ++i) {
                printf("%d ", data[i]);
            }
            printf("\n");
            free(data);
            break;
        }
        case 2: {
            int n;
            printf("Enter the number of elements: ");
            scanf("%d", &n);
            int* data = (int*)malloc(n * sizeof(int));
            printf("Enter the elements: ");
            for (int i = 0; i < n; ++i) {
                scanf("%d", &data[i]);
            }
            merge_sort(data, 0, n - 1);
            printf("Sorted data: ");
            for (int i = 0; i < n; ++i) {
                printf("%d ", data[i]);
            }
            printf("\n");
            free(data);
            break;
        }
        case 3: {
            int n, x;
            printf("Enter the number of elements: ");
            scanf("%d", &n);
            int* data = (int*)malloc(n * sizeof(int));
            printf("Enter the elements (sorted): ");
            for (int i = 0; i < n; ++i) {
                scanf("%d", &data[i]);
            }
            printf("Enter the number to search for: ");
            scanf("%d", &x);
            int result = binary_search(data, n, x);
            if (result != -1) {
                printf("Element found at index %d\n", result);
            } else {
                printf("Element not found\n");
            }
            free(data);
            break;
        }
        case 4: {
            int n;
            printf("Enter the number of Fibonacci numbers to generate: ");
            scanf("%d", &n);
            int* fib_seq = (int*)malloc(n * sizeof(int));
            fibonacci_iterative(n, fib_seq);
            printf("Fibonacci sequence: ");
            for (int i = 0; i < n; ++i) {
                printf("%d ", fib_seq[i]);
            }
            printf("\n");
            free(fib_seq);
            break;
        }
        case 5: {
            int n;
            printf("Enter the number of Fibonacci numbers to generate: ");
            scanf("%d", &n);
            int* fib_seq = (int*)malloc(n * sizeof(int));
            fibonacci_recursive(n, fib_seq);
            printf("Fibonacci sequence: ");
            for (int i = 0; i < n; ++i) {
                printf("%d ", fib_seq[i]);
            }
            printf("\n");
            free(fib_seq);
            break;
        }
        case 6: {
            int n;
            printf("Enter the number of Fibonacci numbers to generate: ");
            scanf("%d", &n);
            int* fib_seq = (int*)malloc(n * sizeof(int));
            fibonacci_dynamic(n, fib_seq);
            printf("Fibonacci sequence: ");
            for (int i = 0; i < n; ++i) {
                printf("%d ", fib_seq[i]);
            }
            printf("\n");
            free(fib_seq);
            break;
        }
        default:
            printf("Invalid choice\n");
            break;
    }

    return 0;
}
