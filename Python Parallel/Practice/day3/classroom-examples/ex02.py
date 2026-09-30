try:
    from mpi4py import MPI
    MPI_AVAILABLE = True
except:
    MPI_AVAILABLE = False


def check_mpi_availability():
    if not MPI_AVAILABLE:
        print(
            "MPI not available. Make sure to install and set it up. \n"
            "Also ensure to run this with `mpirun -n 2 python3 ex02.py`"
        )
        return None, 0, 1

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    return comm, rank, size


def main():
    comm, rank, size = check_mpi_availability()

    if not comm:
        return

    if rank == 0:
        print(f"[SENDER] Hello from node with rank {rank}")
        print(f"No of nodes is {size}")
        # assume/imagine some complex task is performed here
        # the result of this task, we want to share with another
        # process who's rank is 3 (assuming we are having at least 4 processes)
        data = {"text": "This is the result of a complex task"}
        comm.send(data, 3)
    else:
        print(f"     [RECEIVER] Node with rank {rank}")
        if rank == 3:
            data_from_r1 = comm.recv(source=0)
            print(f"     [RECEIVER] Node with rank {rank} got data from node with rank 0 -> {data_from_r1}")
    


if __name__ == "__main__":
    main()
