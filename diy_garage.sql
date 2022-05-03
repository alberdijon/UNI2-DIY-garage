-- phpMyAdmin SQL Dump
-- version 5.0.4deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 29-04-2022 a las 07:06:16
-- Versión del servidor: 10.5.15-MariaDB-0+deb11u1
-- Versión de PHP: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `diy_garage`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cabin-client`
--

CREATE TABLE `cabin-client` (
  `Cabin_ID` int(10) NOT NULL,
  `Client_DNI` varchar(10) NOT NULL,
  `Hour` time(6) NOT NULL,
  `Date` date NOT NULL,
  `Total` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cabins`
--

CREATE TABLE `cabins` (
  `ID` int(10) NOT NULL,
  `€xh` int(10) NOT NULL,
  `Type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cabins`
--

INSERT INTO `cabins` (`ID`, `€xh`, `Type`) VALUES
(1, 30, 'Jumbo'),
(2, 30, 'Jumbo'),
(3, 30, 'Jumbo'),
(4, 20, 'Normal'),
(5, 20, 'Normal'),
(6, 20, 'Normal');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `client`
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
-- Volcado de datos para la tabla `client`
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
('Sara', 'Gimenez', 627218596, 'Sara@gmail.com', '78483927S', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `job`
--

CREATE TABLE `job` (
  `ID` int(5) NOT NULL,
  `Name` text NOT NULL,
  `€xh` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `job`
--

INSERT INTO `job` (`ID`, `Name`, `€xh`) VALUES
(1, 'Customer Support', 7),
(2, 'Mechanic', 8),
(3, 'Cleaner', 6),
(4, 'Supervisor', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `job-worker`
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
-- Estructura de tabla para la tabla `product`
--

CREATE TABLE `product` (
  `ID` int(5) NOT NULL,
  `Brand` varchar(10) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Price` int(10) NOT NULL,
  `Stock` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `shop`
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
-- Estructura de tabla para la tabla `vehicle`
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
-- Volcado de datos para la tabla `vehicle`
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
-- Estructura de tabla para la tabla `worker`
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
-- Volcado de datos para la tabla `worker`
--

INSERT INTO `worker` (`ID`, `Name`, `Surname`, `E_mail`, `Telf`, `DNI`) VALUES
(1, 'Peru', 'Agirrezabala', 'P.Agirrezabala@gmail.com', 697517586, '58460080Z'),
(2, 'Markel', 'Rodriguez', 'M.Rodriguez@gmail.com', 115310991, '36299213S'),
(3, 'Jon', 'Arana', 'J.Arana@gmail.com', 822357050, '39738366R'),
(4, 'Erlantz', 'Garate', 'E.Garate@gmail.com', 366128876, '79564529P'),
(5, 'Ander', 'Garrido', 'A.Garrido@gmail.com', 476018017, '17232078H'),
(6, 'Jonathan', 'Figueiroa', 'J.Figueiroa@gmail.com', 864009804, '13944592Z'),
(7, 'Hugo', 'Mayo', 'H.Mayo@gmail.com', 785407285, '87621842F'),
(8, 'Nestor', 'Azpilikueta', 'N.Azpilikueta@gmail.com', 406008809, '31597088X'),
(9, 'Ane', 'Garate', 'A.Garate@gmail.com', 273683564, '93721373F'),
(10, 'Leire', 'Unzurrunzaga', 'L.Unzurrunzaga@gmail.com', 519059888, '27575395M');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cabin-client`
--
ALTER TABLE `cabin-client`
  ADD PRIMARY KEY (`Cabin_ID`,`Client_DNI`,`Hour`,`Date`),
  ADD KEY `FK_Client-DNI` (`Client_DNI`);

--
-- Indices de la tabla `cabins`
--
ALTER TABLE `cabins`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`DNI`),
  ADD UNIQUE KEY `E-mail` (`E_mail`),
  ADD UNIQUE KEY `Telf` (`Telf`);

--
-- Indices de la tabla `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `job-worker`
--
ALTER TABLE `job-worker`
  ADD PRIMARY KEY (`Worker_ID`,`Work_ID`,`Day`),
  ADD KEY `Work-ID` (`Work_ID`);

--
-- Indices de la tabla `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `shop`
--
ALTER TABLE `shop`
  ADD PRIMARY KEY (`Client_DNI`,`Product_ID`,`Date`,`Hour`),
  ADD KEY `FK_Product-ID` (`Product_ID`);

--
-- Indices de la tabla `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`Enrollment`);

--
-- Indices de la tabla `worker`
--
ALTER TABLE `worker`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `E-mail` (`E_mail`),
  ADD UNIQUE KEY `Telf` (`Telf`),
  ADD UNIQUE KEY `DNI` (`DNI`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cabin-client`
--
ALTER TABLE `cabin-client`
  ADD CONSTRAINT `FK_Cabin-ID` FOREIGN KEY (`Cabin_ID`) REFERENCES `cabins` (`ID`),
  ADD CONSTRAINT `FK_Client-DNI` FOREIGN KEY (`Client_DNI`) REFERENCES `client` (`DNI`);

--
-- Filtros para la tabla `job-worker`
--
ALTER TABLE `job-worker`
  ADD CONSTRAINT `job-worker_ibfk_1` FOREIGN KEY (`Work_ID`) REFERENCES `job` (`ID`),
  ADD CONSTRAINT `job-worker_ibfk_2` FOREIGN KEY (`Worker_ID`) REFERENCES `worker` (`ID`);

--
-- Filtros para la tabla `shop`
--
ALTER TABLE `shop`
  ADD CONSTRAINT `FK_Product-ID` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`ID`),
  ADD CONSTRAINT `shop_ibfk_1` FOREIGN KEY (`Client_DNI`) REFERENCES `client` (`DNI`);

--
-- Filtros para la tabla `vehicle`
--
ALTER TABLE `vehicle`
  ADD CONSTRAINT `vehicle_ibfk_1` FOREIGN KEY (`Client_DNI`) REFERENCES `client` (`DNI`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
