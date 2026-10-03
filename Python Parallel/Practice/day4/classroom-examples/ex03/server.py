import time
import rpyc
from rpyc.utils.server import ThreadedServer


class Calculator(rpyc.Service):

    def exposed_add(self, a, b):
        print(f"adding {a} and {b}...")
        time.sleep(5)
        res = a + b
        print(f"result obtained as {res}")
        return res

    def exposed_subtract(self, a, b):
        print(f"subtracting {a} and {b}...")
        res = a - b
        print(f"result obtained as {res}")
        return res

    def multiply(self, a, b):
        print(f"multiplying {a} and {b}...")
        res = a * b
        print(f"result obtained as {res}")
        return res

    def divide(self, a, b):
        print(f"dividing {a} and {b}...")
        res = a / b
        print(f"result obtained as {res}")
        return res


def main():
    server_port = 12345

    server = ThreadedServer(
        Calculator,                 # in client, proxy of the object of this class is accessed as conn.root
        port=server_port
    )    
    print(f"Starting the RPC server on port {server_port}..")
    server.start()


if __name__ == "__main__":
    main()
