"""Feature 1: list Business and First bookings (Economy excluded)."""
from db import get_connection

SQL = """
    SELECT booking_id, passenger_id, destination, travel_date, class_tier
    FROM bookings
    WHERE class_tier IN ('Business', 'First')
    ORDER BY class_tier, booking_id
"""


def list_premium_bookings():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(SQL)
        rows = cur.fetchall()
    finally:
        conn.close()
    print(f"{'Booking':<8}{'Passenger':<10}{'Destination':<13}{'Date':<12}Tier")
    for b_id, p_id, dest, date, tier in rows:
        print(f"{b_id:<8}{p_id:<10}{dest:<13}{str(date):<12}{tier}")
    return rows
