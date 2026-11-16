
"""
booking_actions.py (Ian)

Targeted UPDATE and DELETE operations for airline_db.
Every operation:
  - requires an ID,
  - uses a WHERE clause (and %s placeholders, never string formatting),
  - returns a result dictionary so the change can be checked before/after.

Deleting a booking removes only the bookings row. The passenger stays,
so the foreign key is never broken and no cascade is used.
"""

import mysql.connector

from db import get_connection  # Thiery's connection helper


# ---------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------
def _valid_id(value, label):
    """Return value as a positive whole number, or raise a clear ValueError."""
    try:
        number = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"{label} must be a whole number, for example 1.") from None
    if number <= 0:
        raise ValueError(f"{label} must be greater than 0.")
    return number


def _get_bookings(cursor, passenger_id):
    """Return the passenger's bookings together with their destination."""
    cursor.execute(
        """
        SELECT p.passenger_id, p.passenger_name, p.destination,
               b.booking_id, b.class_tier, b.seat_preference
        FROM passengers p
        JOIN bookings b ON p.passenger_id = b.passenger_id
        WHERE p.passenger_id = %s
        """,
        (passenger_id,),
    )
    return cursor.fetchall()


# ---------------------------------------------------------------
# UPDATE: seat preference (by passenger ID)
# ---------------------------------------------------------------
def update_seat_preference(passenger_id, new_seat):
    passenger_id = _valid_id(passenger_id, "Passenger ID")
    new_seat = (new_seat or "").strip()
    if not new_seat:
        raise ValueError("Seat preference cannot be empty, for example 'Window'.")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        before = _get_bookings(cursor, passenger_id)
        if not before:
            return {"success": False,
                    "message": f"No booking found for passenger ID {passenger_id}."}

        cursor.execute(
            "UPDATE bookings SET seat_preference = %s WHERE passenger_id = %s",
            (new_seat, passenger_id),
        )
        changed = cursor.rowcount
        conn.commit()

        after = _get_bookings(cursor, passenger_id)
        return {"success": True,
                "message": f"Seat preference updated ({changed} row changed).",
                "before": before, "after": after}
    except mysql.connector.Error:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


# ---------------------------------------------------------------
# UPDATE: destination (by passenger ID)
# ---------------------------------------------------------------
def update_destination(passenger_id, new_destination):
    passenger_id = _valid_id(passenger_id, "Passenger ID")
    new_destination = (new_destination or "").strip()
    if not new_destination:
        raise ValueError("Destination cannot be empty, for example 'Nairobi'.")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT passenger_id, paseenger_name, destination FROM passengers WHERE passenger_id = %s",
            (passenger_id,),
        )
        before = cursor.fetchone()
        if before is None:
            return {"success": False,
                    "message": f"No passenger found with ID {passenger_id}."}

        cursor.execute(
            "UPDATE passengers SET destination = %s WHERE passenger_id = %s",
            (new_destination, passenger_id),
        )
        changed = cursor.rowcount
        conn.commit()

        cursor.execute(
            "SELECT passenger_id, passenger_name, destination FROM passengers WHERE passenger_id = %s",
            (passenger_id,),
        )
        after = cursor.fetchone()
        return {"success": True,
                "message": f"Destination updated ({changed} row changed).",
                "before": before, "after": after}
    except mysql.connector.Error:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


# ---------------------------------------------------------------
# DELETE: one booking (by booking ID). The passenger must remain.
# ---------------------------------------------------------------
def delete_booking(booking_id):
    booking_id = _valid_id(booking_id, "Booking ID")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT booking_id, passenger_id, class_tier FROM bookings WHERE booking_id = %s",
            (booking_id,),
        )
        booking = cursor.fetchone()
        if booking is None:
            return {"success": False,
                    "message": f"No booking found with ID {booking_id}."}

        # Delete from the child table only. The passenger row is not touched.
        cursor.execute("DELETE FROM bookings WHERE booking_id = %s", (booking_id,))
        removed = cursor.rowcount
        conn.commit()

        # Verify: booking gone, passenger still there
        cursor.execute("SELECT COUNT(*) AS n FROM bookings WHERE booking_id = %s", (booking_id,))
        booking_gone = cursor.fetchone()["n"] == 0
        cursor.execute(
            "SELECT passenger_id, passenger_name FROM passengers WHERE passenger_id = %s",
            (booking["passenger_id"],),
        )
        passenger = cursor.fetchone()

        return {"success": True,
                "message": f"Booking {booking_id} deleted ({removed} row removed).",
                "deleted_booking": booking,
                "booking_gone": booking_gone,
                "passenger_remains": passenger is not None,
                "passenger": passenger}
    except mysql.connector.Error:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


# ---------------------------------------------------------------
# Display and menu (called from main.py)
# ---------------------------------------------------------------
def print_result(result):
    print(f"\n{result['message']}")
    if not result["success"]:
        return
    if "before" in result:
        print("Before:", result["before"])
        print("After: ", result["after"])
    if "deleted_booking" in result:
        print("Deleted booking:", result["deleted_booking"])
        print("Booking gone from table:", result["booking_gone"])
        print("Passenger still exists:", result["passenger_remains"], result["passenger"])


def run():
    """Simple menu for the update and delete features."""
    while True:
        print("\n--- Update / Delete ---")
        print("1. Update seat preference (by passenger ID)")
        print("2. Update destination (by passenger ID)")
        print("3. Delete a booking (by booking ID)")
        print("0. Back")
        choice = input("Choose an option (e.g. 1): ").strip()

        try:
            if choice == "1":
                pid = input("Passenger ID (e.g. 1): ")
                seat = input("New seat preference (e.g. Window): ")
                print_result(update_seat_preference(pid, seat))
            elif choice == "2":
                pid = input("Passenger ID (e.g. 1): ")
                dest = input("New destination (e.g. Nairobi): ")
                print_result(update_destination(pid, dest))
            elif choice == "3":
                bid = input("Booking ID to delete (e.g. 1): ")
                print_result(delete_booking(bid))
            elif choice == "0":
                return
            else:
                print("Invalid choice. Enter 1, 2, 3 or 0.")
        except ValueError as error:
            print(f"Input error: {error}")
        except mysql.connector.Error as error:
            print(f"Database error: {error}")


if __name__ == "__main__":
    run()
    
"""Features 3 and 4: update a booking and delete a booking."""
from db import get_connection

UPDATE_SQL = """
    UPDATE bookings
    SET seat_preference = %s
    WHERE booking_id = %s
"""
DELETE_SQL = "DELETE FROM bookings WHERE booking_id = %s"


def update_seat_preference(booking_id, new_seat):
    """Change a booking's seat preference by ID."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(UPDATE_SQL, (new_seat, booking_id))
        conn.commit()
        changed = cur.rowcount
    finally:
        conn.close()
    print(f"Updated {changed} booking(s)." if changed else "Booking not found (or value unchanged).")
    return changed


def delete_booking(booking_id):
    """Delete one booking by ID. The passenger row stays; no cascade is used."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(DELETE_SQL, (booking_id,))
        conn.commit()
        deleted = cur.rowcount
    finally:
        conn.close()
    print(f"Deleted {deleted} booking(s)." if deleted else "Booking not found.")
    return deleted

