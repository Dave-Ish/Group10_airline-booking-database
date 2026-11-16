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
