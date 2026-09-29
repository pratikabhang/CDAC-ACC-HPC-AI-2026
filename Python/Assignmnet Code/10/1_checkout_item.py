def validate_checkout_item(item_dict):
    try:
        for key in ("name", "price", "quantity"):
            if key not in item_dict:
                raise KeyError(f"Missing key: {key}")
        assert isinstance(item_dict["quantity"], int) and item_dict["quantity"] > 0
        assert isinstance(item_dict["price"], (int, float)) and item_dict["price"] > 0
        return True
    except (KeyError, AssertionError) as error:
        print(f"Validation failed: {error}")
        raise

default_item = {"name": "Laptop", "price": 1200.00, "quantity": 2}
print(validate_checkout_item(default_item))

user_item = {
    "name": input("Enter name: "),
    "price": float(input("Enter price: ")),
    "quantity": int(input("Enter quantity: "))
}
print(validate_checkout_item(user_item))
