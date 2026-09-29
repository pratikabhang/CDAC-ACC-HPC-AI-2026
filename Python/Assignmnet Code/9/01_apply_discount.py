def apply_discount(price, discount_percentage):
    assert 0 < discount_percentage < 100, "Discount percentage must be between 0 and 100"

    final_price = price - (price * discount_percentage / 100)

    assert 0 <= final_price <= price, "Final price is invalid"

    return final_price


print("Valid discount:")
print(apply_discount(1000, 20))

print("\nInvalid discount:")
print(apply_discount(1000, 120))