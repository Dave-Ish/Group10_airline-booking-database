-- Fictional sample data only.
USE airline_db;

INSERT INTO passengers (name, current_location) VALUES
    ('Amina Uwase',   'Kigali'),
    ('Daniel Okoye',  'Lagos'),
    ('Sofia Marino',  'Nairobi'),
    ('Jean Habimana', 'Kigali');

INSERT INTO bookings
    (passenger_id, destination, travel_date, seat_preference, class_tier,
     lounge_pass_code, suite_number, chauffeur_service)
VALUES
    (1, 'Nairobi',  '2026-12-05', 'Window', 'Economy',  NULL,       NULL, NULL),
    (2, 'London',   '2026-12-10', 'Aisle',  'Business', 'LNG-2210', NULL, NULL),
    (3, 'Dubai',    '2026-12-18', 'Window', 'First',    'LNG-9001', 3,    TRUE),
    (4, 'Brussels', '2027-01-04', 'Aisle',  'Business', 'LNG-2245', NULL, NULL);
