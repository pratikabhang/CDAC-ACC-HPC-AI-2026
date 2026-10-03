import Pyro4


def main():
    # uri = "PYRO:obj_00f01c9a16ff4869b679c33162d3ea9a@localhost:61334"
    uri = "PYRONAME:MyCalculator"
    calci = Pyro4.Proxy(uri)
    print(f"{calci.subtract(12, 34) = }")
    print(f"{calci.multiply(12, 34) = }")
    print(f"{calci.add(12, 34) = }")
    print(f"{calci.divide(12, 34) = }")


if __name__ == "__main__":
    main()
