import random
import threading

# 1. Create two 5x5 matrices with random integers between 1 and 10[cite: 2]
matrix_a = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
matrix_b = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

# 2. Create a shared result matrix initialized to zeros[cite: 2]
result_matrix = [[0] * 5 for _ in range(5)]

# 3. Write a function to compute the sum of a specific row[cite: 2]
def add_row(a, b, result, row_index):
    for col in range(5):
        result[row_index][col] = a[row_index][col] + b[row_index][col]

def main():
    print("Matrix A:")
    for row in matrix_a:
        print(row)
        
    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    # 4. Create one thread per row (5 threads total)[cite: 2]
    threads = []
    for i in range(5):
        t = threading.Thread(target=add_row, args=(matrix_a, matrix_b, result_matrix, i))
        threads.append(t)
        t.start()

    # 5. Start and join all threads before reading the result[cite: 2]
    for t in threads:
        t.join()

    print("\nThreaded Result Matrix")
    for row in result_matrix:
        print(row)

    # 6. Verify correctness by computing the same result sequentially[cite: 2]
    expected_matrix = [[matrix_a[i][j] + matrix_b[i][j] for j in range(5)] for i in range(5)]

    print("\n Expected Sequential Result Matrix ")
    for row in expected_matrix:
        print(row)

    # Final comparison verification
    if result_matrix == expected_matrix:
        print("\nVerification Successful: Threaded and sequential results match!")
    else:
        print("\nVerification Failed: Results do not match.")

if __name__ == "__main__":
    main()