-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: book_management_system
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authors` (
  `Author_ID` int NOT NULL AUTO_INCREMENT,
  `Author_First_Name` varchar(25) NOT NULL,
  `Author_Last_Name` varchar(25) NOT NULL,
  `No_Of_Books` varchar(4) NOT NULL,
  PRIMARY KEY (`Author_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Laxmi','Debkota','5'),(2,'Deuba','Sherpa','5'),(3,'Gauri','Sharma','3');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_genres`
--

DROP TABLE IF EXISTS `book_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_genres` (
  `Book_Genre_ID` int NOT NULL AUTO_INCREMENT,
  `Book_Genre_Name` varchar(25) DEFAULT NULL,
  `No_Of_Books` varchar(4) NOT NULL,
  PRIMARY KEY (`Book_Genre_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_genres`
--

LOCK TABLES `book_genres` WRITE;
/*!40000 ALTER TABLE `book_genres` DISABLE KEYS */;
INSERT INTO `book_genres` VALUES (1,'Action and Adventure','8'),(2,'Business','4'),(3,'Social Science','6'),(4,'Politics','3');
/*!40000 ALTER TABLE `book_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `ISBN` varchar(20) NOT NULL,
  `Book_Title` varchar(100) DEFAULT NULL,
  `Language` varchar(10) DEFAULT NULL,
  `Author_ID` int DEFAULT NULL,
  `Book_Genre_ID` int DEFAULT NULL,
  `Publication_Year` varchar(4) DEFAULT NULL,
  `Price` varchar(15) DEFAULT NULL,
  `No_Of_Copies` varchar(4) NOT NULL,
  PRIMARY KEY (`ISBN`),
  KEY `Author_ID` (`Author_ID`),
  KEY `Book_Genre_ID` (`Book_Genre_ID`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`Author_ID`) REFERENCES `authors` (`Author_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `books_ibfk_2` FOREIGN KEY (`Book_Genre_ID`) REFERENCES `book_genres` (`Book_Genre_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('1012456982','MadMax','English',1,2,'2015','Rs.1600','10'),('3245789651','Angle Has Fallen','English',2,3,'2019','Rs.1200','8'),('9816349292','Avenger','English',3,1,'2019','Rs.1500','10');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-30 18:08:54
