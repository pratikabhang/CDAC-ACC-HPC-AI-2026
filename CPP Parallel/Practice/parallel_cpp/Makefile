# Makefile for the Parallel Programming in C++ course.
# Builds each .cpp file into its own executable inside bin/.
# Executables are numbered to match the course's suggested order (01-23).
#
# Usage examples:
#   make                        -> builds everything
#   make bin/10_fibonacci_openmp -> builds just that one program
#   make clean                  -> deletes all built executables
#
# Flags:
#   CXXFLAGS  - always used
#   OMPFLAG   - added only for programs that use OpenMP (#pragma omp ...)
#   PTFLAG    - added only for programs that use std::thread/mutex/atomic
#               or the Pthreads library directly

CXX      = g++
CXXFLAGS = -std=c++17 -O2 -Wall
OMPFLAG  = -fopenmp
PTFLAG   = -pthread
TBBFLAG  = -ltbb
BIN      = bin

all: $(BIN) \
     intro_examples \
     module1 \
     module2 \
     module3 \
     module4 \
     module5 \
     module6

$(BIN):
	mkdir -p $(BIN)

# ---------- 00_intro_examples (01-07) ----------
intro_examples: $(BIN)/01_lambda_hello $(BIN)/01b_lambda_parallel_stl \
                $(BIN)/02_template_hello $(BIN)/02b_complexity_classes \
                $(BIN)/03_openmp_hello $(BIN)/04_openmp_parallel_for \
                $(BIN)/05_pthreads_hello $(BIN)/05_openmp_hello \
                $(BIN)/06_mutex_hello $(BIN)/07_atomic_hello

$(BIN)/01_lambda_hello: 00_intro_examples/01_lambda_hello.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN)/01b_lambda_parallel_stl: 00_intro_examples/01b_lambda_parallel_stl.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@ $(TBBFLAG)

$(BIN)/02_template_hello: 00_intro_examples/02_template_hello.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN)/02b_complexity_classes: 00_intro_examples/02b_complexity_classes.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN)/03_openmp_hello: 00_intro_examples/03_openmp_hello.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/04_openmp_parallel_for: 00_intro_examples/04_openmp_parallel_for.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/05_pthreads_hello: 00_intro_examples/05_pthreads_hello.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

$(BIN)/05_openmp_hello: 00_intro_examples/05_openmp_hello.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/06_mutex_hello: 00_intro_examples/06_mutex_hello.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

$(BIN)/07_atomic_hello: 00_intro_examples/07_atomic_hello.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

# ---------- module1_fundamentals (08) ----------
module1: $(BIN)/08_lambda_array_sum

$(BIN)/08_lambda_array_sum: module1_fundamentals/08_lambda_array_sum.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

# ---------- module2_concepts (09-14) ----------
module2: $(BIN)/09_fibonacci_serial $(BIN)/10_fibonacci_openmp \
         $(BIN)/10b_fork_join_without_join $(BIN)/10c_fork_join_with_join \
         $(BIN)/11_array_increment_serial $(BIN)/12_array_increment_openmp \
         $(BIN)/11b_array_sqrt_serial $(BIN)/12b_array_sqrt_openmp \
         $(BIN)/13_sum_pthreads $(BIN)/14_sum_openmp \
         $(BIN)/14b_sum_openmp_reduction

$(BIN)/09_fibonacci_serial: module2_concepts/09_fibonacci_serial.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN)/10_fibonacci_openmp: module2_concepts/10_fibonacci_openmp.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/10b_fork_join_without_join: module2_concepts/10b_fork_join_without_join.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

$(BIN)/10c_fork_join_with_join: module2_concepts/10c_fork_join_with_join.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

$(BIN)/11_array_increment_serial: module2_concepts/11_array_increment_serial.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN)/12_array_increment_openmp: module2_concepts/12_array_increment_openmp.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/11b_array_sqrt_serial: module2_concepts/11b_array_sqrt_serial.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN)/12b_array_sqrt_openmp: module2_concepts/12b_array_sqrt_openmp.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/13_sum_pthreads: module2_concepts/13_sum_pthreads.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

$(BIN)/14_sum_openmp: module2_concepts/14_sum_openmp.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/14b_sum_openmp_reduction: module2_concepts/14b_sum_openmp_reduction.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

# ---------- module3_experimental (15) ----------
module3: $(BIN)/15_speedup_table

$(BIN)/15_speedup_table: module3_experimental/15_speedup_table.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

# ---------- module4_granularity (16) ----------
module4: $(BIN)/16_mergesort_threshold

$(BIN)/16_mergesort_threshold: module4_granularity/16_mergesort_threshold.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

# ---------- module5_algorithms (17-20) ----------
module5: $(BIN)/17_reduction_sum $(BIN)/18_scan_prefix_sum \
         $(BIN)/19_parallel_search $(BIN)/20_parallel_sort

$(BIN)/17_reduction_sum: module5_algorithms/17_reduction_sum.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/18_scan_prefix_sum: module5_algorithms/18_scan_prefix_sum.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN)/19_parallel_search: module5_algorithms/19_parallel_search.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

$(BIN)/20_parallel_sort: module5_algorithms/20_parallel_sort.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(OMPFLAG) $< -o $@

# ---------- module6_race_conditions (21-26) ----------
module6: $(BIN)/21_counter_unsynchronized $(BIN)/22_counter_mutex $(BIN)/23_counter_atomic \
         $(BIN)/24_bank_account_unsynchronized $(BIN)/25_bank_account_mutex \
         $(BIN)/26_bank_account_ownership

# -O0 (no optimization) is used here on purpose: at -O2 the compiler can
# prove the loop is equivalent to "counter += ITERATIONS" and collapse it
# into one operation per thread, which hides the race we want to show.
$(BIN)/21_counter_unsynchronized: module6_race_conditions/21_counter_unsynchronized.cpp | $(BIN)
	$(CXX) -std=c++17 -O0 -Wall $(PTFLAG) $< -o $@

$(BIN)/22_counter_mutex: module6_race_conditions/22_counter_mutex.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

$(BIN)/23_counter_atomic: module6_race_conditions/23_counter_atomic.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

# Same -O0 reasoning as 21_counter_unsynchronized above.
$(BIN)/24_bank_account_unsynchronized: module6_race_conditions/24_bank_account_unsynchronized.cpp | $(BIN)
	$(CXX) -std=c++17 -O0 -Wall $(PTFLAG) $< -o $@

$(BIN)/25_bank_account_mutex: module6_race_conditions/25_bank_account_mutex.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

$(BIN)/26_bank_account_ownership: module6_race_conditions/26_bank_account_ownership.cpp | $(BIN)
	$(CXX) $(CXXFLAGS) $(PTFLAG) $< -o $@

clean:
	rm -rf $(BIN)

.PHONY: all clean intro_examples module1 module2 module3 module4 module5 module6
