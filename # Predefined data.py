# Predefined data
barbers = [
    {"name": "Jaspher Bahian", "rating": 8},  # Rating out of 10 for how well they cut
    {"name": "Johary Casidar", "rating": 9},
    {"name": "Neil Tumapon", "rating": 7}
]

# Pre-populated bookings with dummy data
bookings = [
    {"customer": "John Elly G. Jusay", "cellphone": "09365009032", "barber": "Jaspher Bahian", "time": "9AM"},
    {"customer": "Jane Doe", "cellphone": "09123456789", "barber": "Johary Casidar", "time": "2PM"}
]

# Sign in function
def sign_in():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "ADMIN" and password == "admin123":
            print("Sign in successful!")
            return True
        else:
            print("Invalid credentials. Try again.")

# Main program
if sign_in():
    role = input("Are you a customer or a barber? (1 for customer, 2 for barber): ")
    
    if role == "2":  # Barber
        print("\nCustomer Bookings:")
        for i, booking in enumerate(bookings, 1):
            print(f"{i}. Customer: {booking['customer']}, Barber: {booking['barber']}, Time: {booking['time']}")
        
        choice = int(input("Enter the booking number to view details (or 0 to skip): "))
        if choice > 0 and choice <= len(bookings):
            booking = bookings[choice - 1]
            print(f"Details: Customer: {booking['customer']}, Cellphone: {booking['cellphone']}, Barber: {booking['barber']}, Time: {booking['time']}")
        print("End.")
    
    elif role == "1":  # Customer
        print("\nList of Barbers:")
        for i, barber in enumerate(barbers, 1):
            print(f"{i}. Name: {barber['name']}, Rating: {barber['rating']}/10")
        
        while True:
            try:
                choice = int(input("Select your preferred barber (enter number): "))
                if 1 <= choice <= len(barbers):
                    selected_barber = barbers[choice - 1]
                    print(f"You selected: {selected_barber['name']}")
                    break
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Please enter a number.")
        
        customer_name = input("Enter your name: ")
        cellphone = input("Enter your cellphone number: ")
        booking_time = input("Enter preferred time: ")
        
        # Add booking
        bookings.append({
            "customer": customer_name,
            "cellphone": cellphone,
            "barber": selected_barber['name'],
            "time": booking_time
        })
        print("Booking done!")
        print("End.")
    
    else:
        print("Invalid role selected.")
