#include <iostream>
#include <vector>
#include <algorithm>

// Sorting Algorithms
void bubble_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1);
    std::vector<int> R(n2);

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
}

void merge_sort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Searching Algorithm
int binary_search(const std::vector<int>& arr, int x) {
    int left = 0;
    int right = arr.size() - 1;
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
std::vector<int> fibonacci_iterative(int n) {
    std::vector<int> fib_seq(n);
    if (n > 0) fib_seq[0] = 0;
    if (n > 1) fib_seq[1] = 1;
    for (int i = 2; i < n; ++i) {
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2];
    }
    return fib_seq;
}

int fibonacci_recursive_helper(int n) {
    if (n <= 1) return n;
    return fibonacci_recursive_helper(n - 1) + fibonacci_recursive_helper(n - 2);
}

std::vector<int> fibonacci_recursive(int n) {
    std::vector<int> fib_seq(n);
    for (int i = 0; i < n; ++i) {
        fib_seq[i] = fibonacci_recursive_helper(i);
    }
    return fib_seq;
}

std::vector<int> fibonacci_dynamic(int n) {
    std::vector<int> fib_seq(n);
    if (n > 0) fib_seq[0] = 0;
    if (n > 1) fib_seq[1] = 1;
    for (int i = 2; i < n; ++i) {
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2];
    }
    return fib_seq;
}

int main() {
    std::cout << "Available algorithms:\n";
    std::cout << "1. bubble_sort\n";
    std::cout << "2. merge_sort\n";
    std::cout << "3. binary_search\n";
    std::cout << "4. fibonacci_iterative\n";
    std::cout << "5. fibonacci_recursive\n";
    std::cout << "6. fibonacci_dynamic\n";

    int choice;
    std::cout << "Enter the number of the algorithm you would like to use: ";
    std::cin >> choice;

    switch (choice) {
        case 1: {
            int n;
            std::cout << "Enter the number of elements: ";
            std::cin >> n;
            std::vector<int> data(n);
            std::cout << "Enter the elements: ";
            for (int i = 0; i < n; ++i) {
                std::cin >> data[i];
            }
            bubble_sort(data);
            std::cout << "Sorted data: ";
            for (int num : data) {
                std::cout << num << " ";
            }
            std::cout << "\n";
            break;
        }
        case 2: {
            int n;
            std::cout << "Enter the number of elements: ";
            std::cin >> n;
            std::vector<int> data(n);
            std::cout << "Enter the elements: ";
            for (int i = 0; i < n; ++i) {
                std::cin >> data[i];
            }
            merge_sort(data, 0, data.size() - 1);
            std::cout << "Sorted data: ";
            for (int num : data) {
                std::cout << num << " ";
            }
            std::cout << "\n";
            break;
        }
        case 3: {
            int n, x;
            std::cout << "Enter the number of elements: ";
            std::cin >> n;
            std::vector<int> data(n);
            std::cout << "Enter the elements (sorted): ";
            for (int i = 0; i < n; ++i) {
                std::cin >> data[i];
            }
            std::cout << "Enter the number to search for: ";
            std::cin >> x;
            int result = binary_search(data, x);
            if (result != -1) {
                std::cout << "Element found at index " << result << "\n";
            } else {
                std::cout << "Element not found\n";
            }
            break;
        }
        case 4: {
            int n;
            std::cout << "Enter the number of Fibonacci numbers to generate: ";
            std::cin >> n;
            std::vector<int> fib_seq = fibonacci_iterative(n);
            std::cout << "Fibonacci sequence: ";
            for (int num : fib_seq) {
                std::cout << num << " ";
            }
            std::cout << "\n";
            break;
        }
        case 5: {
            int n;
            std::cout << "Enter the number of Fibonacci numbers to generate: ";
            std::cin >> n;
            std::vector<int> fib_seq = fibonacci_recursive(n);
            std::cout << "Fibonacci sequence: ";
            for (int num : fib_seq) {
                std::cout << num << " ";
            }
            std::cout << "\n";
            break;
        }
        case 6: {
            int n;
            std::cout << "Enter the number of Fibonacci numbers to generate: ";
            std::cin >> n;
            std::vector<int> fib_seq = fibonacci_dynamic(n);
            std::cout << "Fibonacci sequence: ";
            for (int num : fib_seq) {
                std::cout << num << " ";
            }
            std::cout << "\n";
            break;
        }
        default:
            std::cout << "Invalid choice\n";
            break;
    }

    return 0;
}
