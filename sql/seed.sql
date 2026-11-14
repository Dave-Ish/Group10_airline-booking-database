-- Test IDs: use booking 104 for delete tests, passenger 1 for update tests.
USE airline_db;

INSERT INTO passengers (passenger_id, name, current_location, destination, travel_date) VALUES
(1, 'Alex Rivera',  'Chicago', 'Miami',  '2026-12-05'),
(2, 'Jordan Lee',   'Atlanta', 'London', '2026-12-10'),
(3, 'Morgan Blake', 'Seattle', 'Tokyo',  '2026-12-15'),
(4, 'Sam Carter',   'Denver',  'Paris',  '2026-12-20');

INSERT INTO bookings (booking_id, passenger_id, class_tier, seat_preference, lounge_pass_code, suite_number, chauffeur_service) VALUES
(101, 1, 'Economy',  'Window', NULL,      NULL,   NULL),
(102, 2, 'Business', 'Aisle',  'LNG-204', NULL,   NULL),
(103, 3, 'First',    'Window', 'LNG-901', 'S-12', 'Yes'),
(104, 4, 'Economy',  'Aisle',  NULL,      NULL,   NULL) 
