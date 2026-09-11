inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    # Check if user wants to quit
    if stock.lower() == "quit":
        break

    # Check if input is a valid integer
    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    # Reject negative numbers
    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    # Add valid stock to inventory
    inventory += stock

    print("Stock added successfully.")
    print("Current inventory:", inventory)

    # Check for overstock
    if inventory > 500:
        print("ALERT: Inventory exceeds 500 units!")
        break

# Final report
print("\n--- Inventory Report ---")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)