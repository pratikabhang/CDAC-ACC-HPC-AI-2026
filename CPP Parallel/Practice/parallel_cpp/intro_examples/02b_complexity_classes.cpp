// Slide reference: SLIDE 5 - Complexity and Classification
// (check this slide number against your deck - "Complexity and
// Classification" sits between Templates/Lambdas and Speedup/Efficiency,
// but its exact number wasn't confirmed when this file was written.)
//
// Introductory example: the six complexity classes from the slide table,
// shown two ways. First, by counting actual fundamental operations
// (comparisons, array accesses, recursive calls), which reproduces the
// slide's table exactly. Second, by measuring real wall-clock time - a
// single call at n=10/100/1000 is far too fast to time directly (a few
// nanoseconds), so each operation is repeated enough times to add up to
// a measurable duration, then divided back down to time per call.
//
// Why this matters for parallel programming (per the slide): the amount
// of available parallel work is bounded by this same growth rate, and
// synchronization/communication overhead is a cost on top of it. An
// O(n^2) or O(2^n) algorithm has plenty of independent operations to
// spread across threads, but the sheer operation count can still make it
// impractical - parallelism reduces wall-clock time, not operation count.

#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <chrono>

using Clock = std::chrono::high_resolution_clock;

int main() {
    const std::vector<int> sizes = {10, 100, 1000};

    printf("%-10s %-22s %8s %8s %8s\n",
           "Class", "Example", "n=10", "n=100", "n=1000");

    // O(1): array access - always exactly 1 operation, regardless of n.
    printf("%-10s %-22s %8d %8d %8d\n", "O(1)", "Access a[5]", 1, 1, 1);

    // O(log n): binary search on a sorted array, searching for a value
    // that isn't present so it always takes the full log2(n) comparisons.
    printf("%-10s %-22s", "O(log n)", "Binary search");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;
        long long comparisons = 0;
        std::binary_search(a.begin(), a.end(), -1,
                            [&](int x, int y) { comparisons++; return x < y; });
        printf(" %8lld", comparisons);
    }
    printf("\n");

    // O(n): linear search for a value that isn't present, so it scans
    // every element - one comparison per element.
    printf("%-10s %-22s", "O(n)", "Linear search");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;
        long long comparisons = 0;
        for (int x : a) { comparisons++; if (x == -1) break; }
        printf(" %8lld", comparisons);
    }
    printf("\n");

    // O(n log n): std::sort's comparator lets us count exactly how many
    // comparisons the sort performs.
    printf("%-10s %-22s", "O(n log n)", "Sort (std::sort)");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = n - i;
        long long comparisons = 0;
        std::sort(a.begin(), a.end(),
                  [&](int x, int y) { comparisons++; return x < y; });
        printf(" %8lld", comparisons);
    }
    printf("\n");

    // O(n^2): nested loops - every pair of elements is visited once.
    printf("%-10s %-22s", "O(n^2)", "Nested loops");
    for (int n : sizes) {
        long long ops = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                ops++;
        printf(" %8lld", ops);
    }
    printf("\n");

    // O(2^n): recursive subset generation - each of the 2^n leaf calls
    // (include/exclude each element) is one subset. Only n=10 is actually
    // run; n=100 and n=1000 would take longer than the age of the
    // universe, so we print what the table says instead: "impractical".
    printf("%-10s %-22s", "O(2^n)", "Subset generation");
    for (int n : sizes) {
        if (n > 20) {
            printf(" %8s", "impract.");
            continue;
        }
        long long leaves = 0;
        // Two-way branch per element (include/exclude); base case counts
        // one subset. No memoization - this is deliberately exponential.
        std::function<void(int)> generate = [&](int remaining) {
            if (remaining == 0) { leaves++; return; }
            generate(remaining - 1);
            generate(remaining - 1);
        };
        generate(n);
        printf(" %8lld", leaves);
    }
    printf("\n");

    // ---- Measured wall-clock time ----
    // The counts above are far too fast to time in a single call (a few
    // nanoseconds), so each operation is repeated enough times to add up
    // to a measurable duration, then divided back down to time per call.
    // How many repeats "enough" is depends on the operation's own cost,
    // so each class picks its own repeat count below.
    printf("\n%-10s %-22s %8s %8s %8s\n",
           "Class", "Example", "n=10", "n=100", "n=1000");

    // O(1): cost doesn't depend on n, so the repeat count doesn't either.
    printf("%-10s %-22s", "O(1)", "Access a[5]");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;
        const long long repeats = 100000000;
        volatile int sink = 0;
        auto t0 = Clock::now();
        for (long long r = 0; r < repeats; r++) sink = a[5];
        auto t1 = Clock::now();
        (void)sink;
        printf(" %8.2f", std::chrono::duration<double, std::nano>(t1 - t0).count() / repeats);
    }
    printf("  ns/call\n");

    // O(log n): searching for a value that isn't present forces the full
    // log2(n) comparisons every time.
    printf("%-10s %-22s", "O(log n)", "Binary search");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;
        const long long repeats = 5000000;
        volatile bool sink = false;
        auto t0 = Clock::now();
        for (long long r = 0; r < repeats; r++)
            sink = std::binary_search(a.begin(), a.end(), -1 - static_cast<int>(r & 7));
        auto t1 = Clock::now();
        (void)sink;
        printf(" %8.2f", std::chrono::duration<double, std::nano>(t1 - t0).count() / repeats);
    }
    printf("  ns/call\n");

    // O(n): repeat count is scaled down as n grows, so total work per
    // column stays roughly constant instead of exploding.
    printf("%-10s %-22s", "O(n)", "Linear search");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;
        long long repeats = std::max<long long>(1, 5000000 / n);
        volatile bool sink = false;
        auto t0 = Clock::now();
        for (long long r = 0; r < repeats; r++)
            sink = std::find(a.begin(), a.end(), -1) != a.end();
        auto t1 = Clock::now();
        (void)sink;
        printf(" %8.2f", std::chrono::duration<double, std::nano>(t1 - t0).count() / repeats);
    }
    printf("  ns/call\n");

    // O(n log n): reverse the array before each sort so there's always
    // real work to do (sorting an already-sorted array is much cheaper).
    printf("%-10s %-22s", "O(n log n)", "Sort (std::sort)");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;
        long long repeats = std::max<long long>(1, 2000000 / n);
        auto t0 = Clock::now();
        for (long long r = 0; r < repeats; r++) {
            std::reverse(a.begin(), a.end());
            std::sort(a.begin(), a.end());
        }
        auto t1 = Clock::now();
        printf(" %8.2f", std::chrono::duration<double, std::nano>(t1 - t0).count() / repeats);
    }
    printf("  ns/call\n");

    // O(n^2): accumulate a[i]^a[j] into the result (instead of a bare
    // counter) so the compiler can't collapse the loop into a single
    // multiplication - the sum is genuinely data-dependent.
    printf("%-10s %-22s", "O(n^2)", "Nested loops");
    for (int n : sizes) {
        std::vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;
        long long repeats = std::max<long long>(1, 20000000LL / (static_cast<long long>(n) * n + 1));
        volatile long long sink = 0;
        auto t0 = Clock::now();
        for (long long r = 0; r < repeats; r++) {
            long long sum = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    sum += a[i] ^ a[j];
            sink = sum;
        }
        auto t1 = Clock::now();
        (void)sink;
        printf(" %8.2f", std::chrono::duration<double, std::nano>(t1 - t0).count() / repeats);
    }
    printf("  ns/call\n");

    // O(2^n): same "only n<=20" limit as the count table above - anything
    // larger is not just slow to time, it's slow to ever finish.
    printf("%-10s %-22s", "O(2^n)", "Subset generation");
    for (int n : sizes) {
        if (n > 20) {
            printf(" %8s", "impract.");
            continue;
        }
        long long repeats = std::max<long long>(1, 20000000LL / (1LL << n));
        volatile long long sink = 0;
        std::function<long long(int)> generate = [&](int remaining) -> long long {
            if (remaining == 0) return 1;
            return generate(remaining - 1) + generate(remaining - 1);
        };
        auto t0 = Clock::now();
        for (long long r = 0; r < repeats; r++) sink = generate(n);
        auto t1 = Clock::now();
        (void)sink;
        printf(" %8.2f", std::chrono::duration<double, std::nano>(t1 - t0).count() / repeats);
    }
    printf("  ns/call\n");

    return 0;
}
