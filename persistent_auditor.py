import json

inventory = 0
failed_entries = 0
transaction_history = []


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            data = json.load(file)

            inventory = data.get("inventory", 0)
            transaction_history = data.get("transaction_history", [])

            return inventory, transaction_history

    except FileNotFoundError:
        return 0, []


def save_inventory(inventory, transaction_history):
    data = {
        "inventory": inventory,
        "transaction_history": transaction_history
    }

    with open("inventory.txt", "w") as file:
        json.dump(data, file, indent=4)


def get_valid_input():
    product_name = input("Enter Product Name (or 'quit' to exit): ")

    # Check if user wants to quit
    if product_name.lower() == "quit":
        return "quit"

    # Check if product name is empty
    if product_name.strip() == "":
        print("Error: Product name cannot be empty.")
        return None

    quantity = input("Enter Quantity: ")

    # Check if input is a valid integer
    if not quantity.isdigit():
        print("Error: Please enter a valid integer.")
        return None

    quantity = int(quantity)

    # Reject zero or negative numbers
    if quantity <= 0:
        print("Error: Quantity must be greater than 0.")
        return None

    return product_name, quantity


def process_delivery(current_total, new_value):
    return current_total + new_value


def generate_report(total_transactions, total_inventory, failed_attempts):
    print("\n--- Inventory Report ---")
    print("Total Transactions Recorded:", total_transactions)
    print("Total Inventory Processed:", total_inventory)
    print("Failed/Rejected Entries:", failed_attempts)


def get_next_order_id(transaction_history):
    if not transaction_history:
        return 1001

    return transaction_history[-1]["order_id"] + 1


# Load previously saved inventory and transaction history
inventory, transaction_history = load_inventory()

print("Current Orders:")

for order in transaction_history:
    print(
        f'{order["order_id"]}, '
        f'{order["product_name"]}, '
        f'{order["quantity"]}'
    )


while True:
    result = get_valid_input()

    # Check if user wants to quit
    if result == "quit":
        save_inventory(inventory, transaction_history)
        break

    # Check if input was rejected
    if result is None:
        failed_entries += 1
        continue

    product_name, quantity = result

    # Check if inventory would exceed 500 units
    if inventory + quantity > 500:
        print("ALERT: Inventory cannot exceed 500 units!")
        failed_entries += 1
        continue

    # Generate the next order ID
    order_id = get_next_order_id(transaction_history)

    # Process valid delivery
    inventory = process_delivery(inventory, quantity)

    # Add valid transaction to history
    transaction_history.append({
        "order_id": order_id,
        "product_name": product_name,
        "quantity": quantity
    })

    print("\nNew Order Added:")
    print(f"{order_id}, {product_name}, {quantity}")

    print("\nOrder successfully saved to inventory.txt")
    print("Current inventory:", inventory)


# Final report
generate_report(
    len(transaction_history),
    inventory,
    failed_entries
)
