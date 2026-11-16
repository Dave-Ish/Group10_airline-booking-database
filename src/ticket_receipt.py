from db import get_connection


SQL = """
    SELECT
        b.booking_id,
        p.passenger_name,
        p.current_location,
        b.destination,
        b.travel_date,
        b.class_tier,
        b.seat_preference,
        b.lounge_pass_code,
        b.suite_number,
        b.chauffeur_service
    FROM passengers AS p
    INNER JOIN bookings AS b
        ON p.passenger_id = b.passenger_id
    WHERE b.booking_id = %s
"""


def print_receipt(booking_id):
    """Find and display the receipt for one booking."""
    conn = get_connection()

    try:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(SQL, (booking_id,))
            receipt = cursor.fetchone()
        finally:
            cursor.close()
    finally:
        conn.close()

    if receipt is None:
        print(f"No booking with ID {booking_id}.")
        return

    print("\n--- Ticket Receipt ---")
    print(f"Booking number:  {receipt['booking_id']}")
    print(f"Passenger:       {receipt['passenger_name']}")
    print(f"Location:        {receipt['current_location']}")
    print(f"Destination:     {receipt['destination']}")
    print(f"Travel date:     {receipt['travel_date']}")
    print(f"Class:           {receipt['class_tier']}")
    print(f"Seat preference: {receipt['seat_preference']}")
    print(f"Lounge pass:     {receipt['lounge_pass_code'] or 'N/A'}")
    print(f"Suite:           {receipt['suite_number'] or 'N/A'}")

    chauffeur = receipt["chauffeur_service"]
    print(f"Chauffeur:       {'Yes' if chauffeur else 'No'}")
