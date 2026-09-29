// Slide reference: SLIDE 15 - Fork-Join Pattern
// Module 2: fork-join done correctly.
// Same 4 branches as 10b_fork_join_without_join.cpp, but this time every
// thread is joined - the program waits for all branches to finish before
// continuing, exactly as the fork-join pattern requires.

#include <cstdio>
#include <thread>
#include <vector>

void branch(int id) {
    printf("  branch %d running\n", id);
}

int main() {
    printf("Fork: creating 4 branches...\n");

    std::vector<std::thread> branches;
    for (int i = 0; i < 4; i++) {
        branches.emplace_back(branch, i);
    }

    printf("Join: waiting for all branches to finish...\n");
    for (auto& t : branches) {
        t.join();
    }

    printf("All branches joined. Continuing serial execution.\n");
    return 0;
}
