# Product details as dictionary
products = {
    "Product A": {"price": 20},
    "Product B": {"price": 40},
    "Product C": {"price": 50}
}


cart = []

# Discount rules
def apply_discount(subtotal, total_quantity, product_quantities):
    discounts = (
        ("flat_10_discount", 10) if subtotal > 200 else ("no_discount", 0),
        ("bulk_10_discount", 0.1 * subtotal) if total_quantity > 20 else ("no_discount", 0),
        ("bulk_5_discount", 
            sum(products[product]["price"] * product_quantities[product] * 0.05 
                for product in products 
                if product_quantities[product] > 10
            ) if any(product_quantities[product] > 10 for product in products) else ("no_discount", 0)),
        ("tiered_50_discount", 
            sum(products[product]["price"] * (product_quantities[product] - 15) * 0.5 
                if product_quantities[product] > 15
                else 0
                for product in products
            ) if total_quantity > 30 and any(product_quantities[product] > 15 for product in products) else ("no_discount", 0))
    )

    # Choose the most beneficial discount
    best_discount_name, best_discount_amount = max(discounts, key=lambda x: x[1])

    return best_discount_name, best_discount_amount

# Calculate total
def calculate_total():
    subtotal = sum(product_info["price"] * item["quantity"] for item in cart)
    total_quantity = sum(item["quantity"] for item in cart)
    
    # Count product quantities
    product_quantities = {product: item["quantity"] for item in cart for product in products}

    discount_name, discount_amount = apply_discount(subtotal, total_quantity, product_quantities)

    shipping_fee = 5 * (total_quantity // 10)
    gift_wrap_fee = total_quantity

    
    total_before_discount = subtotal + shipping_fee + gift_wrap_fee

    
    total_after_discount = total_before_discount - discount_amount

    return total_after_discount, subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee

# User input
for product_name, product_info in products.items():
    quantity = int(input(f"Enter quantity for {product_name}: "))
    is_gift = input(f"Is {product_name} a gift? (yes/no): ").lower() == "yes"
    cart.append({"product": product_name, "quantity": quantity, "is_gift": is_gift})


subtotal = 0 
for item in cart:
    product_name = item["product"]
    quantity = item["quantity"]
    product_price = products[product_name]["price"]
    total_product_amount = product_price * quantity
    subtotal += total_product_amount  # Update subtotal

    print(f"\nProduct: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Total Amount for {product_name}: ${total_product_amount}")


total_amount, _, discount_name, discount_amount, shipping_fee, gift_wrap_fee = calculate_total()
print("\nSummary:")
print(f"Subtotal: ${subtotal}")
print(f"Discount Applied ({discount_name}): ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total Amount: ${total_amount}")

# Payment input
amount_paid = float(input("\nEnter the amount for payment: $"))

# Check if the amount paid is sufficient[Additional Function]
if amount_paid >= total_amount:
    change_due = amount_paid - total_amount
    print(f"Thanks for your payment! Your change: ${change_due}")
else:
    print("Insufficient payment. Please provide the correct amount.")
print("Visit again!")
