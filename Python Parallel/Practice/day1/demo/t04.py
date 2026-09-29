import pickle
from t03 import Employee


def main():

    filename = "employee.bin"
    with open(filename, "rb") as file:
        e1 = pickle.load(file)

        e1.print()


if __name__ == "__main__":
    print("-"*80)
    main()
    print("-"*80)