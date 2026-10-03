import rpyc


def main():
    conn = rpyc.connect("localhost", 12345)
    calci = conn.root           # proxy to the Calculator object in the server
    print(f"{calci.add(12, 34) = }")         # executes calci.exposed_add method on server
    print(f"{calci.subtract(12, 34) = }")    # executes calci.exposed_subtract method on server
    # print(f"{calci.multiply(12, 34) = }")  # error; there is no "exposed_multiply" on server


if __name__ == "__main__":
    main()
