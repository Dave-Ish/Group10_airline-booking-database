CREATE TABLE passengers (
    passenger_id     INT          NOT NULL AUTO_INCREMENT,
    passenger_name             VARCHAR(100) NOT NULL,
    current_location VARCHAR(100) NOT NULL,
    PRIMARY KEY (passenger_id)
);

CREATE TABLE bookings (
    booking_id        INT          NOT NULL AUTO_INCREMENT,
    passenger_id      INT          NOT NULL,
    destination       VARCHAR(100) NOT NULL,
    travel_date       DATE         NOT NULL,
    seat_preference   VARCHAR(30)  NOT NULL,
    class_tier        ENUM('Economy','Business','First') NOT NULL,
    lounge_pass_code  VARCHAR(20)  NULL,   -- Business/First only
    suite_number      INT          NULL,   -- First only
    chauffeur_service BOOLEAN      NULL,   -- First only
    PRIMARY KEY (booking_id),
    -- No ON DELETE CASCADE: deleting a booking never touches the passenger.
    CONSTRAINT fk_bookings_passenger
        FOREIGN KEY (passenger_id) REFERENCES passengers (passenger_id)
);

DESCRIBE passengers;
DESCRIBE bookings;
