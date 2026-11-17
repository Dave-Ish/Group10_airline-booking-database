
-- Test IDs: use booking 104 for delete tests, passenger 1 for update tests.
USE airline_db;

INSERT INTO passengers (passenger_id, passenger_name, current_location, destination, travel_date) VALUES
(1, 'Alex Rivera',  'Chicago', 'Miami',  '2026-12-05'),
(2, 'Jordan Lee',   'Atlanta', 'London', '2026-12-10'),
(3, 'Morgan Blake', 'Seattle', 'Tokyo',  '2026-12-15'),
(4, 'Sam Carter',   'Denver',  'Paris',  '2026-12-20');

INSERT INTO bookings (booking_id, passenger_id, destination, travel_date, seat_preference, class_tier, lounge_pass_code, suite_number, chauffeur_service) VALUES
    (101, 1, 'Miami',  '2026-12-05', 'Window', 'Economy',  NULL,       NULL, FALSE),
    (102, 2, 'London', '2026-12-10', 'Aisle',  'Business', 'LNG-204', NULL, FALSE),
    (103, 3, 'Tokyo',  '2026-12-15', 'Window', 'First',    'LNG-901', 12,   TRUE),
    (104, 4, 'Paris',  '2026-12-20', 'Aisle',  'Economy',  NULL,       NULL, FALSE)

DESCRIBE bookings;
