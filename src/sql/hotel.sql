-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 12 Sty 2021, 19:30
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `hotel`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `countries`
--

CREATE TABLE `countries` (
  `country_ID` char(2) NOT NULL,
  `country_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `countries`
--

INSERT INTO `countries` (`country_ID`, `country_name`) VALUES
('DE', 'Germany'),
('ES', 'Spain'),
('FR', 'France'),
('GR', 'Greece'),
('PL', 'Poland');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `dining_options`
--

CREATE TABLE `dining_options` (
  `dining_option_ID` int(10) NOT NULL,
  `dining_option_type` varchar(20) NOT NULL,
  `dining_option_cost` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `dining_options`
--

INSERT INTO `dining_options` (`dining_option_ID`, `dining_option_type`, `dining_option_cost`) VALUES
(1, 'Breakfast', 17),
(2, 'Dinner', 40),
(3, 'Half board', 30),
(4, 'All inclusive', 100);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `hotels`
--

CREATE TABLE `hotels` (
  `hotel_ID` int(10) NOT NULL,
  `hotel_name` varchar(20) NOT NULL,
  `location_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `hotels`
--

INSERT INTO `hotels` (`hotel_ID`, `hotel_name`, `location_id`) VALUES
(1, 'T&M', 1),
(2, 'Hilton', 2),
(3, 'EwelMat', 3),
(4, 'Sheraton', 4),
(5, 'Mamaison Le Regina', 5),
(6, 'Descansa con nosotro', 6);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `locations`
--

CREATE TABLE `locations` (
  `location_ID` int(11) NOT NULL,
  `location_city` varchar(20) NOT NULL,
  `street_address` varchar(35) NOT NULL,
  `country_id` char(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `locations`
--

INSERT INTO `locations` (`location_ID`, `location_city`, `street_address`, `country_id`) VALUES
(1, 'Cracow', 'Kronikarza Galla 22', 'PL'),
(2, 'Warsaw', '11 Listopada 54', 'PL'),
(3, 'Berlin', 'Kaiserdamm 12', 'DE'),
(4, 'Athens', 'Liosion 165', 'GR'),
(5, 'Madrid', 'Paseo de la Castellana 54', 'ES'),
(6, 'Madrid', 'Calle de Arturo Soria 27', 'ES'),
(12, 'Paris', 'Rue Chapon 48', 'FR');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `payment_methods`
--

CREATE TABLE `payment_methods` (
  `payment_method_ID` int(10) NOT NULL,
  `payment_method` varchar(15) NOT NULL,
  `payment_method_discount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `payment_methods`
--

INSERT INTO `payment_methods` (`payment_method_ID`, `payment_method`, `payment_method_discount`) VALUES
(1, 'Cash', 1),
(2, 'Bank transfer', 0.98),
(3, 'Debit card', 0.95),
(4, 'Credit card', 0.9);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `reservations`
--

CREATE TABLE `reservations` (
  `reservation_ID` int(10) NOT NULL,
  `client_id` int(10) NOT NULL,
  `hotel_id` int(10) NOT NULL,
  `first_day` date NOT NULL,
  `last_day` date NOT NULL,
  `room_id` int(10) NOT NULL,
  `dining_option_id` int(20) NOT NULL,
  `payment_method_id` int(10) NOT NULL,
  `cost` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `reservations`
--

INSERT INTO `reservations` (`reservation_ID`, `client_id`, `hotel_id`, `first_day`, `last_day`, `room_id`, `dining_option_id`, `payment_method_id`, `cost`) VALUES
(12, 25, 6, '2020-06-13', '2020-07-11', 51, 1, 4, 5055.3),
(17, 25, 6, '2020-09-07', '2020-09-14', 51, 4, 4, 1350),
(18, 25, 4, '2020-11-09', '2020-11-13', 33, 4, 4, 810),
(19, 25, 3, '2020-12-20', '2020-12-24', 28, 4, 4, 2430),
(24, 11, 3, '2020-06-18', '2020-06-28', 28, 1, 2, 5700.66),
(38, 1, 1, '2020-12-10', '2020-12-20', 4, 3, 4, 2727);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rooms`
--

CREATE TABLE `rooms` (
  `room_ID` int(10) NOT NULL,
  `hotel_id` int(10) NOT NULL,
  `room_type_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `rooms`
--

INSERT INTO `rooms` (`room_ID`, `hotel_id`, `room_type_id`) VALUES
(1, 1, 1),
(2, 1, 1),
(3, 1, 1),
(4, 1, 2),
(5, 1, 2),
(6, 1, 3),
(7, 1, 3),
(8, 1, 4),
(9, 1, 5),
(10, 1, 5),
(11, 2, 1),
(12, 2, 1),
(13, 2, 1),
(14, 2, 2),
(15, 2, 2),
(16, 2, 3),
(17, 2, 3),
(18, 2, 4),
(19, 2, 5),
(20, 2, 5),
(21, 3, 1),
(22, 3, 1),
(23, 3, 1),
(24, 3, 2),
(25, 3, 2),
(26, 3, 3),
(27, 3, 3),
(28, 3, 4),
(29, 3, 5),
(30, 3, 5),
(31, 4, 1),
(32, 4, 1),
(33, 4, 1),
(34, 4, 2),
(35, 4, 2),
(36, 4, 3),
(37, 4, 3),
(38, 4, 4),
(39, 4, 5),
(40, 4, 5),
(41, 5, 1),
(42, 5, 1),
(43, 5, 1),
(44, 5, 2),
(45, 5, 2),
(46, 5, 3),
(47, 5, 3),
(48, 5, 4),
(49, 5, 5),
(50, 5, 5),
(51, 6, 1),
(52, 6, 1),
(53, 6, 1),
(54, 6, 2),
(55, 6, 2),
(56, 6, 3),
(57, 6, 3),
(58, 6, 4),
(59, 6, 5),
(60, 6, 5);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `room_types`
--

CREATE TABLE `room_types` (
  `room_type_ID` int(10) NOT NULL,
  `room_type` varchar(20) NOT NULL,
  `room_type_price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `room_types`
--

INSERT INTO `room_types` (`room_type_ID`, `room_type`, `room_type_price`) VALUES
(1, 'Single room', 200),
(2, 'Double room', 300),
(3, 'Triple', 400),
(4, 'Quad', 580),
(5, 'Adults + c', 370);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `user_ID` int(10) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `user_surname` varchar(25) NOT NULL,
  `user_email` varchar(30) NOT NULL,
  `user_telephone` int(9) NOT NULL,
  `user_PESEL` bigint(11) NOT NULL,
  `user_login` varchar(20) DEFAULT NULL,
  `user_password` varchar(20) NOT NULL,
  `user_type` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`user_ID`, `user_name`, `user_surname`, `user_email`, `user_telephone`, `user_PESEL`, `user_login`, `user_password`, `user_type`) VALUES
(1, 'Anna', 'Lisowska', 'alisowska@gmail.com', 756897171, 70021957676, 'lis', 'lisowska1', 0),
(2, 'Patrick', 'Smith', 'psmith@gmail.com', 555494171, 92117630587, 'pitrick', 'smith2', 0),
(3, 'Mateusz', 'Wesoly', 'mwesoly@onet.pl', 756897171, 97060330364, 'mateuszzz', 'wesoly3', 0),
(4, 'Jan', 'Czartoryski', 'jczartoryski@wp.pl', 615094181, 68090206305, 'jan', 'czartoryski4', 0),
(5, 'Izabela', 'Kluzowska', 'ikluzowska@wp.pl', 505171969, 98111003406, 'izabela', 'kluzowska5', 0),
(6, 'Agata', 'Rymarczewska', 'arymarczewska@gmail.com', 888528648, 72061825013, 'agata', 'rymarczewska6', 0),
(7, 'Dominika', 'Szydelko', 'dszydelko@gmail.com', 794744171, 86070118405, 'dominika', 'szydelko7', 0),
(8, 'Milena', 'Pilipczewska', 'mpilipczewska@onet.pl', 896035171, 86050601208, 'milena', 'pilipczewska8', 0),
(9, 'Mirosław', 'Niemily', 'wniemily@gmail.com', 735980151, 67022705307, 'wiktor', 'niemily9', 0),
(10, 'Pawel', 'Grad', 'pgrad@wp.pl', 666937858, 86082905307, 'pawel', 'grad10', 0),
(11, 'Anna', 'Nowak', 'anowak@gmail.com', 756897171, 70021957676, 'annan', 'nowak11', 0),
(23, 'Mateusz', 'Witkowski', 'www@gmail.com', 123123, 98050201230, 'admin', 'zaq1@WSX', 1),
(25, 'Katarzyna', 'Olkowska', 'kate@gamil.com', 123123123, 99020305220, 'kate99', 'kate123', 0),
(27, 'tyci', 'woronko', 'tyci@gmail.com', 123456789, 99010101330, 'tyci', 'zaq1@WSX', 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`country_ID`);

--
-- Indeksy dla tabeli `dining_options`
--
ALTER TABLE `dining_options`
  ADD PRIMARY KEY (`dining_option_ID`);

--
-- Indeksy dla tabeli `hotels`
--
ALTER TABLE `hotels`
  ADD PRIMARY KEY (`hotel_ID`),
  ADD UNIQUE KEY `hotel_name` (`hotel_name`),
  ADD KEY `hotels_locations_fk` (`location_id`);

--
-- Indeksy dla tabeli `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`location_ID`),
  ADD KEY `locations_countries_fk` (`country_id`);

--
-- Indeksy dla tabeli `payment_methods`
--
ALTER TABLE `payment_methods`
  ADD PRIMARY KEY (`payment_method_ID`);

--
-- Indeksy dla tabeli `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`reservation_ID`),
  ADD KEY `reservation_clients_fk` (`client_id`),
  ADD KEY `reservation_hotel_fk` (`hotel_id`),
  ADD KEY `reservation_dining_options_fk` (`dining_option_id`),
  ADD KEY `reservation_rooms_fk` (`room_id`),
  ADD KEY `reservations_payment_methods_fk` (`payment_method_id`);

--
-- Indeksy dla tabeli `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`room_ID`),
  ADD KEY `rooms_room_type_fk` (`room_type_id`),
  ADD KEY `rooms_hotels_fk` (`hotel_id`);

--
-- Indeksy dla tabeli `room_types`
--
ALTER TABLE `room_types`
  ADD PRIMARY KEY (`room_type_ID`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `dining_options`
--
ALTER TABLE `dining_options`
  MODIFY `dining_option_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT dla tabeli `hotels`
--
ALTER TABLE `hotels`
  MODIFY `hotel_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT dla tabeli `locations`
--
ALTER TABLE `locations`
  MODIFY `location_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT dla tabeli `payment_methods`
--
ALTER TABLE `payment_methods`
  MODIFY `payment_method_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT dla tabeli `reservations`
--
ALTER TABLE `reservations`
  MODIFY `reservation_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT dla tabeli `rooms`
--
ALTER TABLE `rooms`
  MODIFY `room_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT dla tabeli `room_types`
--
ALTER TABLE `room_types`
  MODIFY `room_type_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT dla tabeli `users`
--
ALTER TABLE `users`
  MODIFY `user_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `hotels`
--
ALTER TABLE `hotels`
  ADD CONSTRAINT `hotels_locations_fk` FOREIGN KEY (`location_id`) REFERENCES `locations` (`location_ID`);

--
-- Ograniczenia dla tabeli `locations`
--
ALTER TABLE `locations`
  ADD CONSTRAINT `locations_countries_fk` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_ID`);

--
-- Ograniczenia dla tabeli `reservations`
--
ALTER TABLE `reservations`
  ADD CONSTRAINT `reservation_dining_options_fk` FOREIGN KEY (`dining_option_id`) REFERENCES `dining_options` (`dining_option_ID`),
  ADD CONSTRAINT `reservations_hotels_fk` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`hotel_ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `reservations_payment_methods_fk` FOREIGN KEY (`payment_method_id`) REFERENCES `payment_methods` (`payment_method_ID`),
  ADD CONSTRAINT `reservations_rooms_fk` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`room_ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `reservations_users_fk` FOREIGN KEY (`client_id`) REFERENCES `users` (`user_ID`) ON DELETE CASCADE;

--
-- Ograniczenia dla tabeli `rooms`
--
ALTER TABLE `rooms`
  ADD CONSTRAINT `rooms_hotels_fk` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`hotel_ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `rooms_room_type_fk` FOREIGN KEY (`room_type_id`) REFERENCES `room_types` (`room_type_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
