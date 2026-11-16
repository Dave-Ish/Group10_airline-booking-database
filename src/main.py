"""Simple menu that runs the four features."""
from booking_actions import delete_booking, update_seat_preference
from ticket_receipt import print_receipt
from tier_report import list_premium_bookings

MENU = """
=== Airline Booking Database ===
1. List Business/First bookings
2. Print ticket receipt
3. Update seat preference
4. Delete a booking
0. Exit
"""


def ask_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a whole number.")
        return None


def main():
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "1":
            list_premium_bookings()
        elif choice == "2":
            b_id = ask_int("Booking ID: ")
            if b_id is not None:
                print_receipt(b_id)
        elif choice == "3":
            b_id = ask_int("Booking ID: ")
            if b_id is not None:
                update_seat_preference(b_id, input("New seat preference: ").strip())
        elif choice == "4":
            b_id = ask_int("Booking ID: ")
            if b_id is not None:
                delete_booking(b_id)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
