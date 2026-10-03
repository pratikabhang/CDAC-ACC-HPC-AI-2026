import time
import Pyro4

@Pyro4.expose
class Calculator:
    def add(self, a, b):
        print(f"adding {a} and {b}...")
        time.sleep(5)
        res = a + b
        print(f"result obtained as {res}")
        return res

    def subtract(self, a, b):
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
    calc = Calculator()             # object for serving the clients
    server = Pyro4.Daemon()         # server's representation (skeleton)
    uri = server.register(calc)     # register the service objects
    print(f"Server object's URI is {uri}")
    print("Starting the server....")
    ns = Pyro4.locateNS()           # start the name server by running this command:  `pyro-ns`
    ns.register("MyCalculator", uri)
    server.requestLoop()


if __name__ == "__main__":
    main()
