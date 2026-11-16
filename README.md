# airline-booking-database

A small Python + MySQL program for passenger bookings. The SQL queries live inside the Python modules; MySQL setup and sample data are plain `.sql` scripts. All names and data are fictional.

## Requirements
- Python 3.9+
- MySQL 8 running locally
- `pip install -r requirements.txt` (mysql-connector-python)

## Setup (works from a clean database)
```bash
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

mysql -u <your_user> -p < sql/setup.sql    # drops and recreates airline_db + both tables
mysql -u <your_user> -p < sql/seed.sql     # 4 passengers, 4 bookings (Economy, Business, First)

cp .env.example .env                       # then fill in your own values (never commit .env)
```
Set the variables from `.env` in your shell (`DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`), for example on macOS/Linux:
```bash
export DB_USER=your_user DB_PASSWORD=your_password
```

## Run
```bash
cd src
python main.py
```

| Menu option | Feature | File |
|---|---|---|
| 1 | List Business/First bookings (Economy excluded) | `src/tier_report.py` |
| 2 | Ticket receipt using `INNER JOIN` (name, destination, tier, perks) | `src/ticket_receipt.py` |
| 3 | Update a booking's seat preference by ID | `src/booking_actions.py` |
| 4 | Delete a booking by ID (passenger stays) | `src/booking_actions.py` |

## Design
- `passengers(passenger_id PK, name, current_location)`
- `bookings(booking_id PK, passenger_id FK, destination, travel_date DATE, seat_preference, class_tier, lounge_pass_code, suite_number, chauffeur_service)`
- Integer IDs; perks that do not apply are `NULL`; no `ON DELETE CASCADE`.
- Deleting a booking leaves its passenger row intact. Deleting a passenger who still has bookings is blocked by the foreign key.

## Demo script
1. Run `setup.sql` and `seed.sql`, then `python main.py`.
2. Option 1: Business/First only. Option 2 with IDs 1, 2, 3: Economy, Business, First receipts.
3. Option 3 with ID 2: change the seat. Option 2 or a MySQL query shows the change.
4. Option 4 with ID 3, then `SELECT * FROM passengers;` shows Sofia Marino is still there.
