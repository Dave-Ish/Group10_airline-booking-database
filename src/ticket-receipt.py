def get_ticket_receipts(connections): # func that fetches the receipt for passenger with bookings
    cursor = connections.cursor(dictionary=True)

    try:
        cursor.execute(
            """SELECT 
                 b.booking_id,
                 p.passenger_id
                 p.passenger_name, 
                 p.current_location,
                 p.destination,
                 p.travel_date,
                 b.class_tier,
                 b.seat_preference,
                 b.lounge_pass_code,
                 b.suite_number,
                 b.chauffeur_service
            FROM passengers AS p
            JOIN bookings AS b
            ON p.passenger_id = b.passenger_id
            ORDER b.booking_id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()

def display_ticket_receipts(connections):
    receipts = get_ticket_receipts(connections)
    if not receipts:
        print("No booking found")
        return

    for receipt in receipts:
        print(f"--\n Booking Number:    {receipt['booking_id']} --")
        print(f"--Passenger's name:     {receipt['passenger_name']} --")
        print(f"--Location:             {receipt['current_location']}--")
        print(f"--Destination:          {receipt['destination']}--")
        print(f"--Travel date:          {receipt['travel_date']}--")
        print(f"--Class:                {receipt['class_tier']}--")
        print(f"--Seat:                 {receipt['seat_preference']}--")
        print(f"--Launge:               {receipt['lounge_pass_code'] or 'N/A'}--")
        print(f"--Suite:                {receipt['suite_number'] or 'N/A' }--")

        Chauffeur = receipt['chauffeur_service']
        print(f"--Chauffeur:            { 'Yes' if Chauffeur else 'No'}--")
