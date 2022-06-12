-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Crime Reports
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2020 AND street = "Chamberlin Street";

-- Interviews
SELECT * FROM interviews WHERE year = 2020 AND day = 28 AND month = 7 AND transcript LIKE "%courthouse%";

-- Security Logs
SELECT * FROM courthouse_security_logs WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25);

-- Transactions
SELECT * FROM atm_transactions WHERE year = 2020 AND day = 28 AND month = 7 AND atm_location = "Fifer Street" AND transaction_type = "withdraw";

SELECT * FROM phone_calls WHERE year = 2020 AND day = 28 AND month = 7 AND duration <= 60;

SELECT * FROM airports WHERE city="Fiftyville";

SELECT * FROM flights WHERE year = 2020 AND day = 29 AND month = 7 AND origin_airport_id = (
    SELECT id FROM airports WHERE city="Fiftyville"
    ) 
    ORDER BY hour LIMIT 1;

SELECT * FROM passengers WHERE flight_id = (
    SELECT id FROM flights WHERE year = 2020 AND day = 29 AND month = 7 AND origin_airport_id = (
        SELECT id FROM airports WHERE city="Fiftyville"
        ) 
    ORDER BY hour LIMIT 1
    );

SELECT * FROM bank_accounts WHERE account_number IN (
    SELECT account_number FROM atm_transactions WHERE year = 2020 AND 
    day = 28 AND month = 7 AND 
    atm_location = "Fifer Street" AND 
    transaction_type = "withdraw"
);
