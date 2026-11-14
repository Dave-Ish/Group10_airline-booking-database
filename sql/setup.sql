CREATE DATABASE IF NOT EXISTS airline_db;
USE airline_db;

DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS passengers;

CREATE TABLE passengers (
    passenger_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    current_location VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    travel_date DATE NOT NULL
);

CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    passenger_id INT NOT NULL,
    class_tier ENUM('Economy', 'Business', 'First') NOT NULL,
    seat_preference VARCHAR(50),
    lounge_pass_code VARCHAR(50),
    suite_number VARCHAR(20),
    chauffeur_service BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_passenger
        FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id)
        ON DELETE RESTRICT
);