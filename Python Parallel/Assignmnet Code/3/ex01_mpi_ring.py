from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 3:
    if rank == 0:
        print("Please run with at least 3 MPI processes.")
    raise SystemExit

next_rank = (rank + 1) % size
prev_rank = (rank - 1 + size) % size

if rank == 0:
    token = {"hops": 0, "history": [0]}
    token = comm.sendrecv(token, dest=next_rank, source=prev_rank)
    print("Total hops:", token["hops"])
    print("Traversal history:", token["history"])
else:
    token = comm.recv(source=prev_rank)
    token["hops"] += 1
    token["history"].append(rank)
    comm.send(token, dest=next_rank)
