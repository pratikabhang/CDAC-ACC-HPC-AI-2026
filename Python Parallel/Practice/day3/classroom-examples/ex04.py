try:
    from mpi4py import MPI
    import numpy as np

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
        data = [
            12, 10, 4, 58, 2, 459, 39, 93, 95, 39, 284, 48, 4500, 999,29, 22, 100
        ]
        for _ in range(4 - len(data)%4):
            data.append(0)

        data = np.array(data).reshape(4, len(data)//4)
    else:
        data = None
        print(f"     [RECEIVER] Node with rank {rank}")

    # the following line will send data if rank==0; will receive data if rank!=0
    data_from_r1 = comm.scatter(data, root=0)
    print(f"     [RECEIVER] Node with rank {rank} got data from node with rank 0 -> {data_from_r1}\n")


if __name__ == "__main__":
    main()
