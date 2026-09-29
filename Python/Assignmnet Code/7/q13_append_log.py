from datetime import datetime

def append_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

    print("Log message appended.")


message = input("Enter a log message: ")

append_log(message)