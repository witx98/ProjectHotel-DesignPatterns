#ZARZĄDZANIE KONTAMI UŻYTKOWNIKÓW

#1. Pobranie danych potrzenych do logowania wszystkich użytkowników.
SELECT user_login, user_password, user_ID, user_type FROM `users`

#2. Utworzenie konta użytkownika
INSERT INTO users (user_name, user_surname, user_email, user_telephone, user_PESEL,user_login, user_password, user_type)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

#ZARZĄDZANIE REZERWACJAMI

#3. Pobranie inforamcji o id, nazwie i lokalizacji wszystkich hotelów w celu wylistowania.
SELECT hotels.hotel_ID, hotels.hotel_name, countries.country_ID, locations.location_city
FROM `hotels`
INNER JOIN `locations` on locations.location_ID=hotels.location_id
INNER JOIN `countries` on countries.country_ID=locations.country_id ORDER by locations.country_id

#4. Pobranie szczegółowych informacji o pojedynczym hotelu.
SELECT hotels.hotel_ID, hotels.hotel_name, countries.country_name,
locations.location_city, locations.street_address
FROM `hotels`
INNER JOIN `locations` on locations.location_ID=hotels.location_id
INNER JOIN `countries` on countries.country_ID=locations.country_id
WHERE hotels.hotel_ID = %s

#5. Pobranie inforamcji o rodzajach pokoi dostępnych w danym hotelu, uporządkowanych względem id typu pokoju.
SELECT room_types.room_type_ID, room_types.room_type, room_types.room_type_price
FROM `room_types`
INNER JOIN `rooms` ON room_types.room_type_ID=rooms.room_type_id
WHERE rooms.hotel_id = %s
GROUP by room_types.room_type
ORDER by room_types.room_type_ID

#6. Pobranie inforamcji o wszystkich dostępnych rodzajach pokoi, uporządkowanych względem id typu pokoju.
SELECT room_types.room_type_ID, room_types.room_type, room_types.room_type_price
FROM `room_types`
ORDER by room_types.room_type_ID

#7. Pobranie wszystkich dostępnych pokoi danego hotelu, uporządkowanych względem id typu pokoju.
SELECT rooms.room_ID, room_types.room_type, room_types.room_type_price
FROM `room_types`
INNER JOIN `rooms` ON room_types.room_type_ID=rooms.room_type_id
WHERE rooms.hotel_id = %s
ORDER by room_types.room_type_ID

#8. Wybranie wszystkich inforamcji o dostępnych opcjach wyżywienia, uporządkowanych względem id.
SELECT dining_option_ID, dining_option_type, dining_option_cost
FROM `dining_options`
ORDER BY dining_option_ID

#9. Wybranie wszystkich inforamcji o dostępnych sposobach płatności, uporządkowanych względem id.
SELECT payment_method_ID, payment_method, payment_method_discount
FROM `payment_methods`
ORDER BY payment_method_ID

#10. Utworznie rezerwacji na podstawie wyborów klienta,
INSERT INTO reservations (client_id, hotel_id, first_day, last_day, room_id, dining_option_id, payment_method_id, cost)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

#11. Połączenie tabel w celu pobrania wszystkich możliwych informacji dotyczących każdej utworzonej rezerwacji, uporządkowanie względem id.
SELECT reservations.reservation_ID, users.user_name, users.user_surname, hotels.hotel_name, reservations.first_day,
reservations.last_day, rooms.room_ID, room_types.room_type, dining_options.dining_option_type,
payment_methods.payment_method, reservations.cost
FROM `reservations`
INNER JOIN `users` ON reservations.client_id=users.user_ID
INNER JOIN `hotels` ON reservations.hotel_id=hotels.hotel_ID
INNER JOIN `rooms` ON reservations.room_id=rooms.room_ID
INNER JOIN `room_types` ON rooms.room_type_id=room_types.room_type_ID
INNER JOIN `dining_options` ON reservations.dining_option_id=dining_options.dining_option_ID
INNER JOIN `payment_methods` ON reservations.payment_method_id=payment_methods.payment_method_ID
ORDER BY reservations.reservation_ID

#11. Połączenie tabel w celu pobrania wszystki możliwych informacji dotyczących rezerwacji należących do danego klienta rezerwacji.
SELECT reservations.reservation_ID, users.user_name, users.user_surname, hotels.hotel_name,
reservations.first_day, reservations.last_day, rooms.room_ID, room_types.room_type,
dining_options.dining_option_type, payment_methods.payment_method, reservations.cost
FROM `reservations`
INNER JOIN `users` ON reservations.client_id=users.user_ID
INNER JOIN `hotels` ON reservations.hotel_id=hotels.hotel_ID
INNER JOIN `rooms` ON reservations.room_id=rooms.room_ID
INNER JOIN `room_types` ON rooms.room_type_id=room_types.room_type_ID
INNER JOIN `dining_options` ON reservations.dining_option_id=dining_options.dining_option_ID
INNER JOIN `payment_methods` ON reservations.payment_method_id=payment_methods.payment_method_ID
WHERE users.user_ID = %s
ORDER BY reservations.reservation_ID

#12. Połączenie tabel w celu pobrania wszystki możliwych informacji dotyczących pojedynczej rezerwacji należącej do danego klienta rezerwacji, potrzebynch do utorzenia obieku do modyfikacji zamówienia.
SELECT reservations.reservation_ID, reservations.client_id, reservations.hotel_id,
reservations.first_day, reservations.last_day, reservations.room_id, reservations.dining_option_id,
reservations.payment_method_id, reservations.cost, room_types.room_type_price,
dining_options.dining_option_cost, payment_methods.payment_method_discount
FROM `reservations`
INNER JOIN `rooms` ON reservations.room_id = rooms.room_ID
INNER JOIN `room_types` ON rooms.room_type_id = room_types.room_type_ID
INNER JOIN `dining_options` ON reservations.dining_option_id = dining_options.dining_option_ID
INNER JOIN `payment_methods` ON reservations.payment_method_id = payment_methods.payment_method_ID
WHERE reservation_ID = %s

#13. Przesłanie zebranych od klienta zmian w celu aktualizacji rezerwacji.
UPDATE `reservations` SET hotel_id = %s, first_day = %s, last_day = %s,
room_id = %s, dining_option_id = %s, payment_method_id = %s, cost = %s
WHERE reservation_ID = %s

#14. Usunięcie pojedynczej rezerwacji.
DELETE FROM `reservations` WHERE reservations.reservation_ID = %s

#15. Usunięcie wszystkich rezerwacji danego klienta.
DELETE FROM `reservations` WHERE reservations.client_id = %s

#TWORZENIE STATYSTYK

#16. Pobranie minimalnej, średniej i maksymalnej ceny rezerwacji w celu utworzenia statystyk.
SELECT MIN(cost) as 'minimum', MAX(cost) as 'maximum', AVG(cost) as 'average' FROM `reservations`

#17. Pobranie listy hoteli uporządkowanej względem popularności, czyli ilości rezerwacji danego hotelu.
SELECT hotels.hotel_name, locations.location_city,
COUNT(reservations.hotel_id) as 'bookings'
FROM reservations
INNER JOIN hotels ON reservations.hotel_id = hotels.hotel_ID
INNER JOIN locations ON hotels.location_id = locations.location_ID
GROUP BY hotels.hotel_ID
ORDER BY COUNT(reservations.hotel_id) DESC

#18. Pobranie listy rodzajów pokoi uporządkowanej względem najczęściej wybieranego przez klientów typu.
SELECT room_types.room_type, COUNT(reservations.room_id) as 'bookings'
FROM reservations
INNER JOIN rooms ON reservations.room_id = rooms.room_ID
INNER JOIN room_types ON rooms.room_type_id = room_types.room_type_ID
GROUP BY room_types.room_type_ID
ORDER BY COUNT(reservations.room_id) DESC

#19. Pobranie listy opcji wyżywienia uporządkowanej względem najczęściej wybieranej przez klientów opcji.
SELECT dining_options.dining_option_type, COUNT(reservations.dining_option_id) as 'orders'
FROM reservations
INNER JOIN dining_options ON reservations.dining_option_id = dining_options.dining_option_ID
GROUP BY reservations.dining_option_id
ORDER BY COUNT(reservations.dining_option_id) DESC

#20. Pobranie listy sposobów płatności uporządkowanej względem najczęściej wybieranej przez klientów metody.
SELECT payment_methods.payment_method, COUNT(reservations.payment_method_id) as 'orders'
FROM reservations
INNER JOIN payment_methods ON reservations.payment_method_id = payment_methods.payment_method_ID
GROUP BY reservations.payment_method_id
ORDER BY COUNT(reservations.payment_method_id) DESC

#21. Pobranie listy klientów mających więcej niż jedną rezerwację zpisaną w bazie.
SELECT users.user_name, users.user_surname, COUNT(reservations.client_id) as 'reservations'
FROM reservations
INNER JOIN users ON reservations.client_id = users.user_ID
GROUP BY reservations.client_id
HAVING COUNT(reservations.client_id) > 1
ORDER BY COUNT(reservations.client_id) DESC

#ZARZĄDZANIE HOTELAMI

#22. Podczas procesu dodawania hotelu użytkownik podaje informacje o jego położeniu, które są dodawane do tabeli jeżeli dany kraj jeszcze w niej nie istnieje.
INSERT INTO `countries` (countries.country_ID, countries.country_name)
SELECT * FROM (SELECT %s AS country_ID, %s AS country_name) AS tmp
WHERE NOT EXISTS ( SELECT country_ID FROM countries WHERE country_ID = %s ) LIMIT 1

#23. Dodanie inforamcji o dokładniej lokalizacji hotelu.
INSERT INTO `locations` (locations.location_city, locations.street_address, locations.country_id)
VALUES(%s, %s, %s)

#24. Pobranie id ostatniej utworzonej lokalizacji, na podstawie którego zostanie w którego tworzony jest nowy hotel.
SELECT MAX(locations.location_ID) AS 'location_id' FROM locations

#25. Dodanie hotelu z podaną od użytkownika nazwą i wcześniej pobranym id lokalizacji.
INSERT INTO `hotels` (hotels.hotel_name, hotels.location_id) VALUES (%s,%s)

#26. Dodanie pokoju przez użykownika o określonym rodzaju i przypisanym do wybranego hotelu.
INSERT INTO `rooms` (rooms.hotel_id, rooms.room_type_id) VALUES (%s,%s)

#27. Modyfikacja ceny danego rodzaju pokojów.
UPDATE `room_types` SET room_types.room_type_price = %s WHERE room_types.room_type_ID = %s

#28. Modyfikacja ceny danej opcji wyżywienia.
UPDATE `dining_options` SET dining_options.dining_option_cost = %s
WHERE dining_options.dining_option_ID = %s

#29. Połączenie tabel w celu usunięcia hotelu oraz wszystkich pokoi i rezerwacji z nim związanych.
DELETE `reservations`, `rooms`, `hotels`
FROM `hotels`
INNER JOIN `reservations` ON reservations.hotel_id = hotels.hotel_ID
INNER JOIN `rooms` ON rooms.hotel_id = hotels.hotel_ID
WHERE hotels.hotel_ID = %s

#30. Połączenie tabel w celu usunięcia pokoju i wszystkich rezerwacji z nim związanych.
DELETE `reservations`, `rooms`
FROM `rooms`
INNER JOIN `reservations` ON reservations.room_id = rooms.room_ID
WHERE rooms.room_ID = %s