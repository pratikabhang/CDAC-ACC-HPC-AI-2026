// Slide reference: SLIDE 15 - Fork-Join Pattern
// Module 2: what goes wrong when "join" is skipped.
// A fork-join algorithm forks parallel branches, then joins them (waits
// for them to finish) before continuing. This program forks 4 branches
// but never joins them - it just lets the std::thread objects go out of
// scope while still joinable.
//
// That's not just risky, it's a hard error: the C++ standard requires
// every joinable std::thread to be joined (or explicitly detached)
// before its destructor runs. Skip that, and std::terminate() is called
// and the whole program aborts - regardless of whether the branches had
// already finished their work by then. Compare with
// 10c_fork_join_with_join.cpp, which does the exact same fork but joins
// properly.

#include <cstdio>
#include <thread>
#include <vector>

void branch(int id) {
    printf("  branch %d running\n", id);
    fflush(stdout);
}

int main() {
    printf("Fork: creating 4 branches...\n");
    fflush(stdout);   // abort() below won't flush buffered stdout for us

    // vector of threads
    std::vector<std::thread> branches;
    for (int i = 0; i < 4; i++) {
        // Create a new thread that executes the function branch, passing i as its argument.
        branches.emplace_back(branch, i);
    }

    printf("Continuing without joining - watch what happens...\n");
    fflush(stdout);

    // No join() (and no detach()) here. When `branches` is destroyed at
    // the end of main, each still-joinable std::thread's destructor
    // calls std::terminate() instead of letting the program exit
    // normally.
    return 0;
}
