-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Сен 25 2020 г., 09:45
-- Версия сервера: 10.4.14-MariaDB
-- Версия PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `kpo`
--

-- --------------------------------------------------------

--
-- Структура таблицы `schedule`
--

CREATE TABLE `schedule` (
  `ID` int(5) NOT NULL,
  `Teacher` int(5) NOT NULL,
  `Subject` int(5) NOT NULL,
  `Day` varchar(10) NOT NULL,
  `Auditorium` varchar(10) NOT NULL,
  `Quantity` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `schedule`
--

INSERT INTO `schedule` (`ID`, `Teacher`, `Subject`, `Day`, `Auditorium`, `Quantity`) VALUES
(1, 83, 21, 'Thursday', 'A-329', 19),
(2, 26, 29, 'Monday', 'B-170', 27),
(3, 49, 39, 'Sunday', 'B-123', 14),
(4, 91, 71, 'Saturday', 'A-329', 27),
(5, 48, 23, 'Monday', 'B-150', 20),
(6, 44, 74, 'Thursday', 'B-150', 10),
(7, 56, 66, 'Friday', 'A-325', 13),
(8, 90, 88, 'Monday', 'A-329', 23),
(9, 95, 88, 'Tuesday', 'B-170', 28),
(10, 52, 21, 'Monday', 'A-329', 16),
(11, 19, 63, 'Tuesday', 'B-123', 8),
(12, 26, 16, 'Monday', 'A-330', 9),
(13, 87, 15, 'Saturday', 'A-329', 11),
(14, 34, 12, 'Monday', 'A-328', 23),
(15, 15, 4, 'Wednesday', 'A-328', 6),
(16, 44, 2, 'Saturday', 'A-329', 27),
(17, 73, 73, 'Thursday', 'A-328', 15),
(18, 89, 3, 'Wednesday', 'A-325', 5),
(19, 41, 50, 'Friday', 'A-328', 23),
(20, 36, 81, 'Sunday', 'B-170', 11),
(21, 27, 46, 'Thursday', 'B-150', 26),
(22, 10, 57, 'Saturday', 'A-330', 8),
(23, 90, 91, 'Tuesday', 'B-170', 13),
(24, 13, 50, 'Sunday', 'B-160', 22),
(25, 82, 79, 'Saturday', 'B-170', 29),
(26, 14, 44, 'Sunday', 'A-329', 19),
(27, 4, 35, 'Thursday', 'A-327', 14),
(28, 2, 76, 'Tuesday', 'B-123', 17),
(29, 61, 22, 'Sunday', 'B-170', 17),
(30, 92, 97, 'Sunday', 'A-325', 26),
(31, 36, 15, 'Tuesday', 'A-330', 5),
(32, 30, 56, 'Tuesday', 'A-330', 20),
(33, 46, 2, 'Saturday', 'A-325', 25),
(34, 42, 92, 'Monday', 'A-330', 25),
(35, 1, 64, 'Wednesday', 'B-160', 25),
(36, 74, 70, 'Monday', 'A-329', 26),
(37, 32, 56, 'Sunday', 'A-325', 22),
(38, 47, 41, 'Tuesday', 'B-160', 20),
(39, 24, 53, 'Tuesday', 'A-329', 23),
(40, 22, 85, 'Friday', 'B-150', 10),
(41, 85, 60, 'Wednesday', 'A-330', 12),
(42, 81, 55, 'Sunday', 'A-326', 12),
(43, 56, 63, 'Tuesday', 'A-329', 9),
(44, 97, 72, 'Thursday', 'A-326', 9),
(45, 53, 27, 'Friday', 'A-328', 5),
(46, 87, 87, 'Tuesday', 'B-150', 22),
(47, 55, 29, 'Friday', 'A-330', 13),
(48, 36, 25, 'Monday', 'A-330', 18),
(49, 80, 90, 'Friday', 'B-150', 24),
(50, 90, 3, 'Monday', 'B-150', 12),
(51, 88, 5, 'Monday', 'A-330', 11),
(52, 56, 31, 'Friday', 'A-325', 24),
(53, 37, 64, 'Tuesday', 'A-327', 14),
(54, 66, 33, 'Friday', 'B-123', 9),
(55, 72, 99, 'Wednesday', 'A-329', 5),
(56, 42, 14, 'Saturday', 'A-326', 17),
(57, 36, 50, 'Friday', 'A-327', 15),
(58, 31, 9, 'Friday', 'A-328', 20),
(59, 56, 14, 'Wednesday', 'B-150', 17),
(60, 69, 28, 'Wednesday', 'B-170', 24),
(61, 20, 77, 'Wednesday', 'A-326', 7),
(62, 90, 93, 'Thursday', 'B-150', 27),
(63, 99, 14, 'Tuesday', 'A-329', 16),
(64, 88, 46, 'Monday', 'A-326', 27),
(65, 24, 96, 'Wednesday', 'A-330', 5),
(66, 10, 66, 'Thursday', 'B-170', 24),
(67, 1, 13, 'Monday', 'A-327', 11),
(68, 59, 54, 'Friday', 'A-325', 23),
(69, 31, 66, 'Friday', 'A-325', 28),
(70, 83, 49, 'Friday', 'A-328', 6),
(71, 62, 61, 'Tuesday', 'B-150', 24),
(72, 98, 1, 'Thursday', 'A-328', 10),
(73, 22, 22, 'Sunday', 'B-123', 11),
(74, 27, 11, 'Sunday', 'B-170', 28),
(75, 34, 7, 'Monday', 'B-160', 14),
(76, 41, 64, 'Thursday', 'A-328', 8),
(77, 35, 83, 'Wednesday', 'A-326', 18),
(78, 64, 13, 'Thursday', 'A-325', 5),
(79, 52, 51, 'Tuesday', 'B-160', 22),
(80, 34, 90, 'Sunday', 'A-327', 28),
(81, 26, 62, 'Thursday', 'B-150', 21),
(82, 14, 2, 'Saturday', 'A-325', 25),
(83, 28, 99, 'Thursday', 'B-170', 8),
(84, 26, 5, 'Sunday', 'A-329', 9),
(85, 92, 12, 'Tuesday', 'A-325', 6),
(86, 35, 4, 'Friday', 'B-123', 17),
(87, 58, 15, 'Tuesday', 'B-170', 22),
(88, 99, 47, 'Tuesday', 'A-330', 7),
(89, 50, 75, 'Sunday', 'A-330', 14),
(90, 69, 54, 'Tuesday', 'A-328', 27),
(91, 38, 78, 'Friday', 'A-329', 28),
(92, 32, 81, 'Thursday', 'A-326', 24),
(93, 84, 28, 'Friday', 'B-160', 13),
(94, 54, 42, 'Thursday', 'A-330', 18),
(95, 71, 25, 'Saturday', 'B-170', 10),
(96, 76, 10, 'Wednesday', 'B-123', 15),
(97, 29, 64, 'Wednesday', 'A-326', 6),
(98, 51, 46, 'Friday', 'B-150', 15),
(99, 24, 55, 'Sunday', 'A-325', 17),
(100, 97, 66, 'Wednesday', 'A-326', 5);

-- --------------------------------------------------------

--
-- Структура таблицы `subjects`
--

CREATE TABLE `subjects` (
  `ID` int(5) NOT NULL,
  `Name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `subjects`
--

INSERT INTO `subjects` (`ID`, `Name`) VALUES
(1, 'In'),
(2, 'sem'),
(3, 'malesuada.'),
(4, 'ante.'),
(5, 'congue.'),
(6, 'vel,'),
(7, 'turpis'),
(8, 'tellus'),
(9, 'faucibus'),
(10, 'mattis'),
(11, 'mollis'),
(12, 'arcu.'),
(13, 'eu,'),
(14, 'felis'),
(15, 'Vestibulum'),
(16, 'lacus'),
(17, 'mauris'),
(18, 'elit,'),
(19, 'aliquam'),
(20, 'parturient'),
(21, 'Nam'),
(22, 'Maecenas'),
(23, 'sit'),
(24, 'posuere'),
(25, 'augue'),
(26, 'lectus'),
(27, 'Pellentesque'),
(28, 'aliquet'),
(29, 'magna.'),
(30, 'eget'),
(31, 'purus,'),
(32, 'Donec'),
(33, 'convallis'),
(34, 'dolor'),
(35, 'nulla.'),
(36, 'malesuada'),
(37, 'molestie'),
(38, 'dis'),
(39, 'mi'),
(40, 'egestas'),
(41, 'ipsum'),
(42, 'ac'),
(43, 'lacinia.'),
(44, 'accumsan'),
(45, 'et'),
(46, 'adipiscing'),
(47, 'egestas'),
(48, 'nec,'),
(49, 'sollicitudin'),
(50, 'Sed'),
(51, 'varius'),
(52, 'velit'),
(53, 'Quisque'),
(54, 'ac'),
(55, 'elit,'),
(56, 'eget'),
(57, 'Mauris'),
(58, 'orci.'),
(59, 'Sed'),
(60, 'dapibus'),
(61, 'Pellentesque'),
(62, 'metus.'),
(63, 'pharetra.'),
(64, 'pede,'),
(65, 'feugiat.'),
(66, 'eget'),
(67, 'et,'),
(68, 'Aliquam'),
(69, 'libero'),
(70, 'Nunc'),
(71, 'lacinia'),
(72, 'ultrices'),
(73, 'Duis'),
(74, 'vitae'),
(75, 'Praesent'),
(76, 'elementum'),
(77, 'dui,'),
(78, 'Nullam'),
(79, 'eu,'),
(80, 'amet,'),
(81, 'in,'),
(82, 'nulla.'),
(83, 'metus.'),
(84, 'ligula.'),
(85, 'pellentesque'),
(86, 'nibh.'),
(87, 'dis'),
(88, 'pharetra'),
(89, 'augue'),
(90, 'turpis'),
(91, 'lorem,'),
(92, 'eu'),
(93, 'dolor.'),
(94, 'turpis.'),
(95, 'ultrices'),
(96, 'ac'),
(97, 'luctus'),
(98, 'nibh.'),
(99, 'lobortis,'),
(100, 'ipsum');

-- --------------------------------------------------------

--
-- Структура таблицы `teachers`
--

CREATE TABLE `teachers` (
  `ID` int(11) NOT NULL,
  `Surname` varchar(20) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Patronymic` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `teachers`
--

INSERT INTO `teachers` (`ID`, `Surname`, `Name`, `Patronymic`) VALUES
(1, 'Scott', 'Charde', 'Kadeem'),
(2, 'Mccormick', 'Jolene', 'Raja'),
(3, 'Stephenson', 'Kyle', 'Scott'),
(4, 'Knowles', 'Randall', 'Barrett'),
(5, 'Gomez', 'Quintessa', 'Cade'),
(6, 'Hayes', 'Chadwick', 'Martin'),
(7, 'Rosa', 'Jerry', 'Kelly'),
(8, 'Morin', 'Ivana', 'Martin'),
(9, 'Powers', 'Joelle', 'Micah'),
(10, 'Daugherty', 'Xyla', 'Garrison'),
(11, 'Mendez', 'Stephen', 'Emmanuel'),
(12, 'Dudley', 'Ariana', 'Adam'),
(13, 'Carpenter', 'Adam', 'Kieran'),
(14, 'Mcdonald', 'Macaulay', 'Gabriel'),
(15, 'Norris', 'Eric', 'Omar'),
(16, 'Chase', 'Wyatt', 'Abbot'),
(17, 'Harding', 'Amaya', 'Armand'),
(18, 'Witt', 'Hannah', 'Ezra'),
(19, 'Sosa', 'Karly', 'Plato'),
(20, 'Drake', 'Amanda', 'Ferdinand'),
(21, 'Baird', 'Dorothy', 'Bevis'),
(22, 'Morales', 'Richard', 'Gage'),
(23, 'Gregory', 'Kay', 'Blaze'),
(24, 'Stein', 'Jonah', 'Joseph'),
(25, 'House', 'Aquila', 'Xanthus'),
(26, 'Williamson', 'Ali', 'Octavius'),
(27, 'Hyde', 'Melinda', 'Wade'),
(28, 'Crane', 'Joshua', 'Rogan'),
(29, 'Fields', 'Cole', 'Cairo'),
(30, 'Hurst', 'Serina', 'Todd'),
(31, 'Figueroa', 'Phelan', 'Walker'),
(32, 'Duncan', 'Sage', 'Brenden'),
(33, 'Cook', 'Tad', 'Hoyt'),
(34, 'Kemp', 'Michelle', 'Thane'),
(35, 'Holder', 'Orli', 'Alexander'),
(36, 'Pearson', 'Gray', 'Ulysses'),
(37, 'Harvey', 'Dieter', 'Clayton'),
(38, 'Mcbride', 'Erasmus', 'Caldwell'),
(39, 'Gray', 'Alexis', 'Ulysses'),
(40, 'Bates', 'Hilary', 'Stone'),
(41, 'Hendrix', 'Cairo', 'Kevin'),
(42, 'Mcclure', 'Keaton', 'Ethan'),
(43, 'Bass', 'Mikayla', 'Jermaine'),
(44, 'Todd', 'Myles', 'Hyatt'),
(45, 'Contreras', 'Perry', 'Elmo'),
(46, 'Dale', 'Susan', 'Dale'),
(47, 'Whitehead', 'Sandra', 'Aladdin'),
(48, 'Nixon', 'Channing', 'Bruce'),
(49, 'Short', 'Emery', 'Vincent'),
(50, 'Horne', 'Xandra', 'Dante'),
(51, 'Kennedy', 'Jermaine', 'Nissim'),
(52, 'Paul', 'Rudyard', 'Randall'),
(53, 'Gilbert', 'Kasper', 'Gray'),
(54, 'Crane', 'Natalie', 'Justin'),
(55, 'Clemons', 'Adrienne', 'Hiram'),
(56, 'Bradley', 'Lucian', 'Erich'),
(57, 'Lambert', 'Suki', 'Elton'),
(58, 'Ball', 'Hop', 'Lane'),
(59, 'Farrell', 'Tad', 'Driscoll'),
(60, 'Hardin', 'Rhonda', 'Merritt'),
(61, 'Finley', 'Roth', 'Joshua'),
(62, 'Harrison', 'Hamilton', 'Fitzgerald'),
(63, 'Grimes', 'Hilda', 'Cain'),
(64, 'Barrett', 'Aretha', 'Vaughan'),
(65, 'Battle', 'Gretchen', 'Gil'),
(66, 'Kaufman', 'Sierra', 'Steel'),
(67, 'Patel', 'Imelda', 'Marvin'),
(68, 'Mills', 'Ann', 'Oliver'),
(69, 'Kelley', 'Bernard', 'Chancellor'),
(70, 'Pope', 'Hyatt', 'Moses'),
(71, 'Steele', 'Dacey', 'Wyatt'),
(72, 'Paul', 'Hashim', 'Wesley'),
(73, 'Cote', 'Amela', 'Kelly'),
(74, 'Valentine', 'Gareth', 'Sawyer'),
(75, 'Macias', 'Neville', 'Xanthus'),
(76, 'Fulton', 'Breanna', 'Uriel'),
(77, 'Brennan', 'Colin', 'Julian'),
(78, 'Stanley', 'Carissa', 'Cole'),
(79, 'Sanchez', 'Noelani', 'Ralph'),
(80, 'Mcmillan', 'Darius', 'Salvador'),
(81, 'Randolph', 'Desirae', 'Chadwick'),
(82, 'Kaufman', 'Maia', 'Nathaniel'),
(83, 'Garrison', 'Amy', 'Dieter'),
(84, 'Giles', 'Iola', 'Lane'),
(85, 'Walls', 'Shad', 'Joshua'),
(86, 'William', 'Wylie', 'Slade'),
(87, 'Russo', 'Chava', 'Elliott'),
(88, 'Rodriquez', 'Quynn', 'Arden'),
(89, 'Wolfe', 'Lavinia', 'Alden'),
(90, 'Bowers', 'Knox', 'Dalton'),
(91, 'Ferguson', 'Lillian', 'Christopher'),
(92, 'Sutton', 'Fatima', 'Ryan'),
(93, 'Acevedo', 'Brennan', 'Duncan'),
(94, 'Rush', 'Jonas', 'Kane'),
(95, 'Bernard', 'Mariam', 'Jermaine'),
(96, 'Powers', 'Cain', 'Eric'),
(97, 'Hale', 'Nomlanga', 'Arthur'),
(98, 'Velasquez', 'Eric', 'Leroy'),
(99, 'Lara', 'Channing', 'Fletcher'),
(100, 'Dennis', 'Grady', 'Omar');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `schedule`
--
ALTER TABLE `schedule`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Teacher` (`Teacher`),
  ADD KEY `Subject` (`Subject`);

--
-- Индексы таблицы `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `schedule`
--
ALTER TABLE `schedule`
  MODIFY `ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT для таблицы `subjects`
--
ALTER TABLE `subjects`
  MODIFY `ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT для таблицы `teachers`
--
ALTER TABLE `teachers`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `schedule`
--
ALTER TABLE `schedule`
  ADD CONSTRAINT `schedule_ibfk_1` FOREIGN KEY (`Teacher`) REFERENCES `teachers` (`ID`),
  ADD CONSTRAINT `schedule_ibfk_2` FOREIGN KEY (`Subject`) REFERENCES `subjects` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
