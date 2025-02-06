import re

GST_RATE = 0.18  # 18% GST

# Theatre seat configuration
seat_rows = {
    "First Class": {"rows": "A-G", "price": 200},
    "Second Class": {"rows": "H-X", "price": 150},
    "Economic Class": {"rows": "Y-Z", "price": 50},
}

# Snacks menu with prices
snacks_menu = {
    "1": ("Popcorn", 100),
    "2": ("Ice Cream", 80),
    "3": ("Puffs", 60),
    "4": ("Tea", 40),
    "5": ("Soft Drinks", 50),
}

# Function to validate input
def validate_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        print("Invalid input. Please try again.")

# Collect user details
name = input("Enter your name: ")
phone = validate_input("Enter your phone number: ", r"^\d{10}$")
dob = validate_input("Enter your date of birth (YYYY-MM-DD): ", r"^\d{4}-\d{2}-\d{2}$")

# Get seat booking details
num_seats = int(input("Enter the total number of seats: "))

print("\nAvailable Seats:")
for category, details in seat_rows.items():
    print(f"{category}: {details['rows']} - Rs.{details['price']} + GST")

selected_seats = input(f"Select your {num_seats} seats (e.g., A2 A3 A4): ").split()
seat_price = 0

# Calculate ticket price
for seat in selected_seats:
    row = seat[0].upper()
    for category, details in seat_rows.items():
        if row in details["rows"]:
            seat_price += details["price"]
            break

ticket_total = seat_price + (seat_price * GST_RATE)

# Snacks selection
snacks_total = 0
snacks_order = {}

if input("Do you want Snacks? (Yes/No): ").strip().lower() == "yes":
    print("\nAvailable Snacks:")
    for key, (snack, price) in snacks_menu.items():
        print(f"{key}. {snack} - Rs.{price}")

    num_snacks = int(input("How many types of snacks do you want?: "))
    for _ in range(num_snacks):
        snack_choice = input("Enter snack number: ")
        if snack_choice in snacks_menu:
            quantity = int(input(f"How many {snacks_menu[snack_choice][0]}?: "))
            snacks_total += snacks_menu[snack_choice][1] * quantity
            snacks_order[snacks_menu[snack_choice][0]] = quantity
        else:
            print("Invalid snack choice, skipping...")

# Print the final bill
print("\nBooking Confirmation:")
print(f"Hi {name}! You have successfully booked {num_seats} tickets.")
print(f"Seats: {', '.join(selected_seats)}")
print(f"Your total ticket price: Rs.{ticket_total:.2f}")
if snacks_order:
    print(f"Your snacks total price: Rs.{snacks_total:.2f}")
    print("Snacks Ordered:")
    for snack, qty in snacks_order.items():
        print(f"- {snack}: {qty}")

print("\nThank you for booking with us!")
