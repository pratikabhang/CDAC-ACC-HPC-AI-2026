def string_methods():
    text = input("Enter text: ")

    print("Lowercase:", text.lower())
    print("Uppercase:", text.upper())
    print("Without spaces:", text.strip())
    print("Replace FUN:", text.replace("FUN", "amazing"))
    print("Starts with Py:", text.strip().startswith("Py"))
    print("Ends with !:", text.strip().endswith("!"))
    print("Count of o:", text.count("o"))

string_methods()