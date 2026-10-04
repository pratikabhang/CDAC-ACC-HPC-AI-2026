"""Interactive RPyC client for the Remote System Inspector."""

import rpyc


def print_menu():
    print("\n" + "=" * 50)
    print("RPYC REMOTE SYSTEM INSPECTOR (CLIENT CLI)")
    print("=" * 50)
    print("1. Inspect Remote Host System Info")
    print("2. List Files on Remote Directory")
    print("3. Compute Exponential Table on Remote Host")
    print("4. Evaluate Math Expression on Remote Host")
    print("5. Disconnect & Exit")
    print("-" * 50)


def main():
    try:
        conn = rpyc.connect("localhost", 18861)
        service = conn.root
    except Exception as exc:
        print(f"Could not connect to RPyC server: {exc}")
        return

    try:
        while True:
            print_menu()
            choice = input("Enter your choice [1-5]: ").strip()

            if choice == "1":
                info = service.get_system_info()
                print("\nREMOTE SYSTEM INFORMATION")
                print(f"OS          : {info['system']}")
                print(f"Release     : {info['release']}")
                print(f"Hostname    : {info['hostname']}")
                print(f"CPU Count   : {info['cpu_count']}")
                print(f"Server Time : {info['server_time']}")

            elif choice == "2":
                path = input("Enter remote directory [default=.]: ").strip() or "."
                files = service.list_files(path)
                print(f"\nFILES IN: {path}")
                for name in files:
                    print(f"- {name}")

            elif choice == "3":
                try:
                    base = float(input("Enter base (e.g. 2): "))
                    exponent = int(input("Enter maximum exponent (e.g. 10): "))
                    table = service.compute_powers(base, exponent)
                    print("\nPOWER TABLE")
                    for exp, value in table.items():
                        print(f"{base:g}^{exp} = {value}")
                except ValueError as exc:
                    print(f"Invalid input: {exc}")

            elif choice == "4":
                expression = input(
                    'Enter expression (e.g. "2**32 - 1" or "math.sqrt(144)"): '
                ).strip()
                print("Remote result:", service.execute_expression(expression))

            elif choice == "5":
                print("Disconnected from RPyC server.")
                break

            else:
                print("Invalid choice. Please select 1-5.")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
