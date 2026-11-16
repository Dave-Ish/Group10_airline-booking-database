from src.db import get_connection

def main():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT b.booking_id, p.full_name, b.route, b.class_tier
        FROM bookings b
        JOIN passengers p ON b.passenger_id = p.passenger_id
        WHERE b.class_tier IN ('Business', 'First')
        ORDER BY b.booking_id
    """)
    for row in cur.fetchall():
        print(f"Booking ID: {row['booking_id']} | {row['full_name']}")
        print(f"Route: {row['route']} | Tier: {row['class_tier']}")
        print()
    conn.close()

if __name__ == "__main__":
    main()
