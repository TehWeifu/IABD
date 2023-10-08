-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: sql_remember
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Pieces`
--

DROP TABLE IF EXISTS `Pieces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pieces` (
  `Code` int NOT NULL,
  `NAME` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pieces`
--

LOCK TABLES `Pieces` WRITE;
/*!40000 ALTER TABLE `Pieces` DISABLE KEYS */;
INSERT INTO `Pieces` VALUES (1,'Sprocket'),(2,'Screw'),(3,'Nut'),(4,'Bolt');
/*!40000 ALTER TABLE `Pieces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Providers`
--

DROP TABLE IF EXISTS `Providers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Providers` (
  `Code` varchar(20) NOT NULL,
  `NAME` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Providers`
--

LOCK TABLES `Providers` WRITE;
/*!40000 ALTER TABLE `Providers` DISABLE KEYS */;
INSERT INTO `Providers` VALUES ('HAL','Clarke Enterprises'),('RBT','Susan Calvin Corp.'),('TNBC','Skellington Supplies');
/*!40000 ALTER TABLE `Providers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Provides`
--

DROP TABLE IF EXISTS `Provides`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Provides` (
  `Piece` int NOT NULL,
  `Provider` varchar(20) NOT NULL,
  `Price` int DEFAULT NULL,
  PRIMARY KEY (`Piece`,`Provider`),
  KEY `piece` (`Piece`),
  KEY `provider` (`Provider`),
  CONSTRAINT `Provides_ibfk_1` FOREIGN KEY (`Piece`) REFERENCES `Pieces` (`Code`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Provides_ibfk_2` FOREIGN KEY (`Provider`) REFERENCES `Providers` (`Code`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Provides`
--

LOCK TABLES `Provides` WRITE;
/*!40000 ALTER TABLE `Provides` DISABLE KEYS */;
INSERT INTO `Provides` VALUES (1,'HAL',11),(1,'RBT',16),(1,'TNBC',8),(2,'HAL',21),(2,'RBT',16),(2,'TNBC',15),(3,'RBT',51),(3,'TNBC',46),(4,'HAL',6);
/*!40000 ALTER TABLE `Provides` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-08 12:35:10