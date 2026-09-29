class DataMissingError(RuntimeError):
    pass


def process_monthly_report(filename):
    file_stream = None

    try:
        try:
            file_stream = open(filename, "r")
            return file_stream.read()

        except FileNotFoundError:
            print("Warning: Source file not found. Trying backup_data.csv instead.")

            try:
                file_stream = open("backup_data.csv", "r")
                return file_stream.read()

            except FileNotFoundError:
                raise DataMissingError(
                    "No source data or backup files available."
                )

    finally:
        if file_stream is not None:
            file_stream.close()


filename = input("Enter sales filename: ")

try:
    print(process_monthly_report(filename))
except DataMissingError as error:
    print(error)