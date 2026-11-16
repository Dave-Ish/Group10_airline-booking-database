# Group 10 - Airline Booking Database

Airline booking system - Business / First Class report.

## What it does
Shows only Business and First Class bookings.
Economy bookings are excluded.

Uses JOIN between passengers and bookings:
WHERE class_tier IN ('Business', 'First')

## How to run
py create_db.py
$env:PYTHONPATH="src"; py -m src.tier_report

## Example output
Booking ID: 1 | Latonia Uwase
Route: Kigali -> Dubai | Tier: Business

Booking ID: 2 | John Doe
Route: Kigali -> London | Tier: First

## Files
- sql/ - MySQL schema + seed data
- src/db.py - SQLite connection
- src/tier_report.py - Business/First report
- create_db.py - Creates the database
