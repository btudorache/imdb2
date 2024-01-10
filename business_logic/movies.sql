-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Jan 10, 2024 at 09:44 PM
-- Server version: 8.0.31
-- PHP Version: 8.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `movies`
--

-- --------------------------------------------------------

--
-- Table structure for table `COMMENTS`
--

CREATE TABLE `COMMENTS` (
  `id` bigint NOT NULL,
  `comment` varchar(256) NOT NULL,
  `id_user` bigint NOT NULL,
  `id_movie` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `FAVORITE`
--

CREATE TABLE `FAVORITE` (
  `id` bigint NOT NULL,
  `id_user` bigint NOT NULL,
  `id_movie` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `MOVIES`
--

CREATE TABLE `MOVIES` (
  `id` bigint NOT NULL,
  `title` varchar(100) NOT NULL,
  `year` int NOT NULL,
  `genre` varchar(20) NOT NULL,
  `director` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `MOVIES`
--

INSERT INTO `MOVIES` (`id`, `title`, `year`, `genre`, `director`) VALUES
(1, 'un filme', 1900, 'drama', 'jmekeru');

-- --------------------------------------------------------

--
-- Table structure for table `SCORES`
--

CREATE TABLE `SCORES` (
  `id` bigint NOT NULL,
  `score` int NOT NULL,
  `id_movie` bigint NOT NULL,
  `id_user` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `COMMENTS`
--
ALTER TABLE `COMMENTS`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `FAVORITE`
--
ALTER TABLE `FAVORITE`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `MOVIES`
--
ALTER TABLE `MOVIES`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SCORES`
--
ALTER TABLE `SCORES`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `COMMENTS`
--
ALTER TABLE `COMMENTS`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FAVORITE`
--
ALTER TABLE `FAVORITE`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `MOVIES`
--
ALTER TABLE `MOVIES`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `SCORES`
--
ALTER TABLE `SCORES`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
