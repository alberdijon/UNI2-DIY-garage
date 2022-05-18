-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2022 at 11:58 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diy_garage`
--

-- --------------------------------------------------------

--
-- Table structure for table `cabins`
--

CREATE TABLE `cabins` (
  `ID` int(10) NOT NULL,
  `exh` int(10) NOT NULL,
  `Type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cabins`
--

INSERT INTO `cabins` (`ID`, `exh`, `Type`) VALUES
(1, 30, 'Jumbo'),
(2, 30, 'Jumbo'),
(3, 30, 'Jumbo'),
(4, 20, 'Normal'),
(5, 20, 'Normal'),
(6, 20, 'Normal');

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `Name` varchar(20) NOT NULL,
  `Surname` varchar(20) NOT NULL,
  `Telf` int(14) NOT NULL,
  `E_mail` varchar(40) NOT NULL,
  `DNI` varchar(10) NOT NULL,
  `Password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`Name`, `Surname`, `Telf`, `E_mail`, `DNI`, `Password`) VALUES
('Lucia', 'Sanchez', 862465609, 'Lucia@gmail.com', '14798322F', '1'),
('Brandon', 'Moreno', 107158783, 'Brandon@gmail.com', '24732734Y', '1'),
('Andres', 'Perez', 742571971, 'Andres@gmail.com', '38619590Z', '1'),
('Jose', 'Perez', 119916095, 'Jose@gmail.com', '39763789D', '1'),
('Andrea', 'Casquero', 466457167, 'Andrea@gmail.com', '47461706X', '1'),
('Unai', 'Cortes', 516921334, 'Unai@gmail.com', '50223406P', '1'),
('Leire', 'Urtubuia', 296902880, 'Leire@gmail.com', '69306470H', '1'),
('Igone', 'Aizpurua', 152408969, 'Igone@gmail.com', '70890506K', '1'),
('Ibon', 'Urrestilla', 537283090, 'Ibon@gmail.com', '74375855L', '1'),
('Sara', 'Gimenez', 627218596, 'Sara@gmail.com', '78483927S', '1'),
('Admin', 'Admin', 123, 'admin@uni2.eus', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `employee_dismissed`
--

CREATE TABLE `employee_dismissed` (
  `ID` int(5) NOT NULL,
  `Name` text NOT NULL,
  `Surname` text NOT NULL,
  `E_mail` varchar(30) NOT NULL,
  `Telf` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee_dismissed`
--

INSERT INTO `employee_dismissed` (`ID`, `Name`, `Surname`, `E_mail`, `Telf`) VALUES
(8, 'Nestor', 'Azpilikueta', 'N.Azpilikueta@gmail.com', 406008809);

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `ID` int(5) NOT NULL,
  `Name` text NOT NULL,
  `€xh` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`ID`, `Name`, `€xh`) VALUES
(1, 'Customer Support', 7),
(2, 'Mechanic', 8),
(3, 'Cleaner', 6),
(4, 'Supervisor', 10);

-- --------------------------------------------------------

--
-- Table structure for table `job-worker`
--

CREATE TABLE `job-worker` (
  `Worker_ID` int(5) NOT NULL,
  `Work_ID` int(5) NOT NULL,
  `Beginning_h` time(6) NOT NULL,
  `Ending_h` time(6) NOT NULL,
  `Day` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `ID` int(5) NOT NULL,
  `Brand` varchar(15) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Price` int(10) NOT NULL,
  `Stock` int(20) NOT NULL,
  `img` varchar(150) CHARACTER SET utf8 COLLATE utf8_spanish2_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`ID`, `Brand`, `Name`, `Price`, `Stock`, `img`) VALUES
(2, 'Michelin', 'Tires', 70, 4, NULL);

--
-- Triggers `product`
--
DELIMITER $$
CREATE TRIGGER `re_stock` BEFORE DELETE ON `product` FOR EACH ROW INSERT INTO re_stock
	VALUES (OLD.ID, OLD.Brand, OLD.Name, OLD.Price, OLD.Stock)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `Cabin_ID` int(10) NOT NULL,
  `Client_DNI` varchar(10) NOT NULL,
  `Hour` time(6) NOT NULL,
  `Date` date NOT NULL,
  `Total` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reservation`
--

INSERT INTO `reservation` (`Cabin_ID`, `Client_DNI`, `Hour`, `Date`, `Total`) VALUES
(0, 'admin', '00:00:00.000000', '0000-00-00', 0),
(1, '74375855L', '12:00:00.000000', '2022-05-19', 30),
(3, '69306470H', '20:00:00.000000', '2022-05-25', 30),
(4, '74375855L', '11:00:00.000000', '2022-05-09', 20),
(7, 'admin', '00:00:00.000000', '0000-00-00', 30);

-- --------------------------------------------------------

--
-- Table structure for table `re_stock`
--

CREATE TABLE `re_stock` (
  `ID` int(4) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Price` int(8) NOT NULL,
  `Brand` varchar(30) NOT NULL,
  `Stock` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `re_stock`
--

INSERT INTO `re_stock` (`ID`, `Name`, `Price`, `Brand`, `Stock`) VALUES
(12345, 'repsol', 0, '50', 13212);

-- --------------------------------------------------------

--
-- Table structure for table `shop`
--

CREATE TABLE `shop` (
  `Client_DNI` varchar(10) NOT NULL,
  `Product_ID` int(5) NOT NULL,
  `Amount` int(5) NOT NULL,
  `Date` date NOT NULL,
  `Hour` time(6) NOT NULL,
  `Total_price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `Enrollment` varchar(10) NOT NULL,
  `Brand` varchar(15) NOT NULL,
  `Model` varchar(15) NOT NULL,
  `Color` text NOT NULL,
  `Year` year(4) NOT NULL,
  `Fuel` text NOT NULL,
  `Client_DNI` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`Enrollment`, `Brand`, `Model`, `Color`, `Year`, `Fuel`, `Client_DNI`) VALUES
('0131BCD', 'Seat', 'Leon', 'Red', 2012, 'Diesel', '47461706X'),
('0818 WLT', 'Ford', 'Sierra', 'Navy Blue', 2003, 'Gasoline', '14798322F'),
('1966 OTQ', 'Fiat', 'Multipla', 'Red', 2006, 'Diesel', '39763789D'),
('2636 HIQ', 'Volvo', 'XC40', 'Black', 2015, 'Diesel', '50223406P'),
('2745 LYG', 'Wolskvagen', 'TDI', 'Black', 2008, 'Diesel', '74375855L'),
('3760BGX', 'Opel', 'Corsa', 'Grey', 2006, 'Diesel', '38619590Z'),
('5175SDW', 'Honda', 'Civic', 'Yellow', 2014, 'Gasoline', '24732734Y'),
('7477CQB', 'Audi', 'R8', 'White', 2020, 'Gasoline', '78483927S'),
('7520 HGK', 'Mitsubishi', 'Montero', 'Red', 2007, 'Gasoline', '69306470H'),
('7978XIQ', 'Nissan', 'Qasqhai', 'Blue', 2018, 'Gasoline', '70890506K');

-- --------------------------------------------------------

--
-- Table structure for table `worker`
--

CREATE TABLE `worker` (
  `ID` int(5) NOT NULL,
  `Name` text NOT NULL,
  `Surname` text NOT NULL,
  `E_mail` varchar(30) NOT NULL,
  `Telf` int(10) NOT NULL,
  `DNI` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `worker`
--

INSERT INTO `worker` (`ID`, `Name`, `Surname`, `E_mail`, `Telf`, `DNI`) VALUES
(1, 'Peru', 'Agirrezabala', 'P.Agirrezabala@gmail.com', 697517586, '58460080Z'),
(2, 'Markel', 'Rodriguez', 'M.Rodriguez@gmail.com', 115310991, '36299213S'),
(3, 'Jon', 'Alberdi', 'J.Alberdi@gmail.com', 822357050, '39738366R'),
(4, 'Erlantz', 'Garate', 'E.Garate@gmail.com', 366128876, '79564529P'),
(5, 'Ander', 'Garrido', 'A.Garrido@gmail.com', 476018017, '17232078H'),
(6, 'Jonathan', 'Figueiroa', 'J.Figueiroa@gmail.com', 864009804, '13944592Z'),
(7, 'Hugo', 'Mayo', 'H.Mayo@gmail.com', 785407285, '87621842F'),
(8, 'Nestor', 'Azpilikueta', 'N.azpilikueta@gmail.com', 565789809, '12345678H'),
(9, 'Ane', 'Garate', 'A.Garate@gmail.com', 273683564, '93721373F'),
(10, 'Leire', 'Unzurrunzaga', 'L.Unzurrunzaga@gmail.com', 519059888, '27575395M');

--
-- Triggers `worker`
--
DELIMITER $$
CREATE TRIGGER `employee_dismissed` BEFORE DELETE ON `worker` FOR EACH ROW INSERT INTO employee_dismissed
	VALUES (OLD.ID, OLD.Name, OLD.Surname, OLD.E_mail, OLD.Telf)
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cabins`
--
ALTER TABLE `cabins`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`DNI`),
  ADD UNIQUE KEY `E-mail` (`E_mail`),
  ADD UNIQUE KEY `Telf` (`Telf`);

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `job-worker`
--
ALTER TABLE `job-worker`
  ADD PRIMARY KEY (`Worker_ID`,`Work_ID`,`Day`),
  ADD KEY `Work-ID` (`Work_ID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`Cabin_ID`,`Client_DNI`,`Hour`,`Date`),
  ADD KEY `FK_Client-DNI` (`Client_DNI`);

--
-- Indexes for table `re_stock`
--
ALTER TABLE `re_stock`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `shop`
--
ALTER TABLE `shop`
  ADD PRIMARY KEY (`Client_DNI`,`Product_ID`,`Date`,`Hour`),
  ADD KEY `FK_Product-ID` (`Product_ID`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`Enrollment`),
  ADD KEY `vehicle_ibfk_1` (`Client_DNI`);

--
-- Indexes for table `worker`
--
ALTER TABLE `worker`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `E-mail` (`E_mail`),
  ADD UNIQUE KEY `Telf` (`Telf`),
  ADD UNIQUE KEY `DNI` (`DNI`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `job-worker`
--
ALTER TABLE `job-worker`
  ADD CONSTRAINT `job-worker_ibfk_1` FOREIGN KEY (`Work_ID`) REFERENCES `job` (`ID`),
  ADD CONSTRAINT `job-worker_ibfk_2` FOREIGN KEY (`Worker_ID`) REFERENCES `worker` (`ID`);

--
-- Constraints for table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `FK_Client-DNI` FOREIGN KEY (`Client_DNI`) REFERENCES `client` (`DNI`);

--
-- Constraints for table `shop`
--
ALTER TABLE `shop`
  ADD CONSTRAINT `shop_ibfk_1` FOREIGN KEY (`Client_DNI`) REFERENCES `client` (`DNI`),
  ADD CONSTRAINT `shop_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`ID`);

--
-- Constraints for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD CONSTRAINT `vehicle_ibfk_1` FOREIGN KEY (`Client_DNI`) REFERENCES `client` (`DNI`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
