from mpi4py import MPI
import random
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start = MPI.Wtime()

if rank == 0:
    total_samples = 12_000_000
else:
    total_samples = None

total_samples = comm.bcast(total_samples, root=0)
local_samples = total_samples // size

random.seed(rank * 100 + 42)

local_inside = 0
for _ in range(local_samples):
    x = random.random()
    y = random.random()
    if x * x + y * y <= 1:
        local_inside += 1

total_inside = comm.reduce(local_inside, op=MPI.SUM, root=0)

if rank == 0:
    pi_approx = 4 * total_inside / (local_samples * size)
    error = abs(pi_approx - math.pi)
    runtime = MPI.Wtime() - start

    print(f"Pi approximation: {pi_approx}")
    print(f"Error: {error}")
    print(f"Execution time: {runtime:.6f} seconds")
