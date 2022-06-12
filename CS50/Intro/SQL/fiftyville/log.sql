-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Crime Reports
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2020 AND street = "Chamberlin Street";

-- Interviews
SELECT * FROM interviews WHERE year = 2020 AND day = 28 AND month = 7 AND transcript LIKE "%courthouse%";

-- Security Logs
SELECT * FROM courthouse_security_logs WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25);

-- Transactions
SELECT * FROM atm_transactions WHERE year = 2020 AND day = 28 AND month = 7 AND atm_location = "Fifer Street" AND transaction_type = "withdraw";

-- Phone Calls
SELECT * FROM phone_calls WHERE year = 2020 AND day = 28 AND month = 7 AND duration <= 60;

-- Airports
SELECT * FROM airports WHERE city="Fiftyville";

-- Earliest flight that left Fiftville the next day.
SELECT * FROM flights WHERE year = 2020 AND day = 29 AND month = 7 AND origin_airport_id = (
    SELECT id FROM airports WHERE city="Fiftyville"
    ) 
    ORDER BY hour LIMIT 1;

-- Passengers that took the above flight
SELECT * FROM passengers WHERE flight_id = (
    SELECT id FROM flights WHERE year = 2020 AND day = 29 AND month = 7 AND origin_airport_id = (
        SELECT id FROM airports WHERE city="Fiftyville"
        ) 
    ORDER BY hour LIMIT 1
    );

-- Details of bank accounts whose transactions took place on the day of theft
SELECT * FROM bank_accounts WHERE account_number IN (
    SELECT account_number FROM atm_transactions WHERE year = 2020 AND 
    day = 28 AND month = 7 AND 
    atm_location = "Fifer Street" AND 
    transaction_type = "withdraw"
);

-- Name from the people who match the data below
SELECT name FROM people WHERE 

-- People who spoke on phone on the day and time of the theft
phone_number IN (
    SELECT caller FROM phone_calls WHERE year = 2020 AND day = 28 AND month = 7 AND duration <= 60
) AND

-- People who traveled in the quickest flight on the next of the theft
passport_number IN (
    SELECT passport_number FROM passengers WHERE flight_id = (
    SELECT id FROM flights WHERE year = 2020 AND day = 29 AND month = 7 AND origin_airport_id = (
        SELECT id FROM airports WHERE city="Fiftyville"
        ) 
    ORDER BY hour LIMIT 1
    )
) AND

-- License plate of the cars that left the court house after the ten minutes of the theft 
license_plate IN (
    SELECT license_plate FROM courthouse_security_logs WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25)
) AND

-- ID of the person who performed transactions on the day of the theft
id IN (
    SELECT person_id FROM bank_accounts WHERE account_number IN (
        SELECT account_number FROM atm_transactions WHERE year = 2020 AND 
        day = 28 AND month = 7 AND 
        atm_location = "Fifer Street" AND 
        transaction_type = "withdraw"
    )
);

-- Name from the people who match the data below
SELECT name FROM people WHERE 

-- People who spoke recived phone on the day and time of the theft
phone_number IN (
    SELECT reciver FROM phone_calls WHERE year = 2020 AND day = 28 AND month = 7 AND duration <= 60
);