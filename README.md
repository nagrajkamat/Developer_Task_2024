# Developer_Task_2024
Python Code Documentation

1. Product Details
# Product details as dictionary
products = {
    "Product A": {"price": 20},
    "Product B": {"price": 40},
    "Product C": {"price": 50}
}
Defines a dictionary products containing information about different products and their prices.

2. Cart Details
# Cart details as list of dictionaries
cart = []
Initializes an empty list cart to store the selected products and their quantities.

3. Discount Rules
# Discount rules
def apply_discount(subtotal, total_quantity, product_quantities):
    # ... (discount calculations)
Defines a function apply_discount to calculate discounts based on various rules.
4. Total Calculation
# Calculate total
def calculate_total():
    # ... (subtotal calculation, product quantities, discount calculation, shipping, and gift wrap fees)
Defines a function calculate_total to calculate the total amount considering subtotal, discounts, shipping, and gift wrap fees.

5. User Input
# User input
for product_name, product_info in products.items():
    # ... (user input for product quantities and gift status)
Takes user input for the quantity of each product and whether it's a gift or not.

6. Detailed Output
# Calculate and display detailed output
subtotal = 0
for item in cart:
    # ... (calculates total amount for each product in the cart and updates subtotal)
Calculates and displays detailed output for each product in the cart.

7. Summary and Total Amount Display
# Calculate and display total
total_amount, _, discount_name, discount_amount, shipping_fee, gift_wrap_fee = calculate_total()
print("\nSummary:")
# ... (prints subtotal, discounts, shipping fee, gift wrap fee, and total amount)
Calculates and displays the summary, including subtotal, discounts, shipping, gift wrap fee, and total amount.

8. Payment
# Payment input
amount_paid = float(input("\nEnter the amount for payment: $"))
# ... (checks if the payment is sufficient and provides change or prompts for correct payment)
Takes user input for the payment amount and checks if it's sufficient.

9. End of Program
print("Visit again!")
Prints a closing message for the user.


#Steps to Run the code
1)Copy the provided Python code.
2)Open a Python interpreter or create a Python script.
3)Paste the code into the interpreter or script.
4)Run the code.
5)Follow the prompts to input quantities and gift status for each product.
6)Enter the payment amount when prompted.
7)Review the detailed output, summary, and payment information.

#Note:-
The code will prompt for user input, and you need to enter values accordingly.
