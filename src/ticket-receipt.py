def get_ticket_receipts(connections): # func that fetches the receipt for passenger with bookings
    cursor = connections.cursor(dictionary=True)

    try:
        cursor.execute(
            """SELECT 
                 b.booking_id,
                 p.name, 
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
            ON p.passenger_id = b.booking_id
            ORDER b.booking_id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()