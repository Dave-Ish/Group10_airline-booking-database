def get_ticket_receipts(connections): # func that fetches the receipt for passenger with bookings
    cursor = connection.cursor(dictionary=True)

