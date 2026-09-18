inventory = 0
failed_entries = 0


def get_valid_input():
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    # Check if user wants to quit
    if stock.lower() == "quit":
        return "quit"

    # Check if input is a valid integer
    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        return None

    stock = int(stock)

    # Reject negative numbers
    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        return None

    return stock


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("\n--- Inventory Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


while True:
    stock = get_valid_input()

    # Check if user wants to quit
    if stock == "quit":
        break

    # Check if input was rejected
    if stock is None:
        failed_entries += 1
        continue

    # Check if delivery would exceed 500 units
    if inventory + stock > 500:
        print("ALERT: Inventory cannot exceed 500 units!")
        failed_entries += 1
        continue

    # Process valid delivery
    inventory = process_delivery(inventory, stock)

    # Calculate tax for the delivery
    tax = calculate_tax(stock)

    print("Stock added successfully.")
    print("Current inventory:", inventory)
    print("Tax for this delivery:", tax)

# Final report
generate_report(inventory, failed_entries)