"""Feature 2: receipt using an INNER JOIN of passengers and bookings."""
from db import get_connection

SQL = """
    SELECT p.name, b.destination, b.class_tier,
           b.lounge_pass_code, b.suite_number, b.chauffeur_service
    FROM bookings AS b
    INNER JOIN passengers AS p ON p.passenger_id = b.passenger_id
    WHERE b.booking_id = %s
"""


def print_receipt(booking_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(SQL, (booking_id,))
        row = cur.fetchone()
    finally:
        conn.close()
    if row is None:
        print(f"No booking with ID {booking_id}.")
        return None
    name, dest, tier, lounge, suite, chauffeur = row
    print("----- TICKET RECEIPT -----")
    print(f"Passenger:   {name}")
    print(f"Destination: {dest}")
    print(f"Tier:        {tier}")
    # Perks that do not apply are stored as NULL and simply skipped.
    if lounge is not None:
        print(f"Lounge pass: {lounge}")
    if suite is not None:
        print(f"Suite:       {suite}")
    if chauffeur is not None:
        print(f"Chauffeur:   {'Yes' if chauffeur else 'No'}")
    print("--------------------------")
    return row
