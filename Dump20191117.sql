-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: too_superstore
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `BranchID` varchar(15) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Address` varchar(150) DEFAULT NULL,
  `PhoneNumber` varchar(10) DEFAULT NULL,
  `ManagerIDNumber` varchar(13) NOT NULL,
  `StartDate` date DEFAULT NULL,
  PRIMARY KEY (`BranchID`),
  KEY `fk_managerID` (`ManagerIDNumber`),
  CONSTRAINT `fk_managerID` FOREIGN KEY (`ManagerIDNumber`) REFERENCES `employee` (`EmployeeIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES ('0000001','branchA','18/329 blah blah','0994812552','0123456789012','2019-11-12');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract`
--

DROP TABLE IF EXISTS `contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contract` (
  `ContractID` varchar(15) NOT NULL,
  `RentablePlaceID` varchar(15) NOT NULL,
  `RentingCostPerBilling` decimal(13,2) NOT NULL,
  `BillingType` enum('daily','weekly','monthly','yearly','onetime') NOT NULL,
  `OwnerIDNumber` varchar(13) NOT NULL,
  `OwnerFirstName` varchar(45) NOT NULL,
  `OwnerLastName` varchar(45) DEFAULT NULL,
  `OwnerPhoneNumber` varchar(10) DEFAULT NULL,
  `StartDate` date NOT NULL,
  `ExpireDate` date NOT NULL,
  PRIMARY KEY (`ContractID`),
  KEY `fk_RentablePlaceID` (`RentablePlaceID`),
  CONSTRAINT `fk_RentablePlaceID` FOREIGN KEY (`RentablePlaceID`) REFERENCES `rentableplace` (`RentablePlaceID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `contract_chk_1` CHECK ((`RentingCostPerBilling` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract`
--

LOCK TABLES `contract` WRITE;
/*!40000 ALTER TABLE `contract` DISABLE KEYS */;
INSERT INTO `contract` VALUES ('c01','r01',2500.00,'weekly','1200101809392','PJ','Ponn','0891234567','2019-11-12','2019-11-13');
/*!40000 ALTER TABLE `contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EmployeeIDNumber` varchar(13) NOT NULL,
  `BranchID` varchar(15) NOT NULL,
  `BranchStartDate` date DEFAULT NULL,
  `SupervisorIDNumber` varchar(13) DEFAULT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `BirthDate` date DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `JobPosition` varchar(45) DEFAULT NULL,
  `JobType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeIDNumber`),
  KEY `fk_branchID2` (`BranchID`),
  KEY `fk_supervisor` (`SupervisorIDNumber`),
  CONSTRAINT `fk_branchID2` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_supervisor` FOREIGN KEY (`SupervisorIDNumber`) REFERENCES `employee` (`EmployeeIDNumber`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('0123456789012','0000001','2019-11-12',NULL,'Pon','Phatcharapon','2019-11-11','2019-11-12','Lead','Electrical Engineer'),('0123456789013','0000001','2019-11-12','0123456789012','Win','Pasit','2019-11-11','2019-11-12',NULL,'Computer Engineer');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `importid`
--

DROP TABLE IF EXISTS `importid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `importid` (
  `ImportID` varchar(15) NOT NULL,
  `DateTimeImport` datetime NOT NULL,
  PRIMARY KEY (`ImportID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `importid`
--

LOCK TABLES `importid` WRITE;
/*!40000 ALTER TABLE `importid` DISABLE KEYS */;
INSERT INTO `importid` VALUES ('123','2019-11-12 14:01:17');
/*!40000 ALTER TABLE `importid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `InvoiceID` varchar(15) NOT NULL,
  `OrderDate` date NOT NULL,
  `ArriveDate` date DEFAULT NULL,
  `TotalPrice` decimal(13,2) NOT NULL,
  `WarehouseID` varchar(15) NOT NULL,
  KEY `fk_WarehouseID` (`WarehouseID`),
  CONSTRAINT `fk_WarehouseID` FOREIGN KEY (`WarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `invoice_chk_1` CHECK ((`TotalPrice` >= 0)),
  CONSTRAINT `invoice_chk_2` CHECK ((`ArriveDate` > `OrderDate`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_t`
--

DROP TABLE IF EXISTS `member_t`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_t` (
  `MemberIDNumber` varchar(13) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `StartDate` date NOT NULL,
  `ExpireDate` date NOT NULL,
  `MemberPoints` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`MemberIDNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_t`
--

LOCK TABLES `member_t` WRITE;
/*!40000 ALTER TABLE `member_t` DISABLE KEYS */;
INSERT INTO `member_t` VALUES ('1200101809391','Phatcharapon','Jumruspun','2019-11-12','2019-11-12',0);
/*!40000 ALTER TABLE `member_t` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memberinvoice`
--

DROP TABLE IF EXISTS `memberinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `memberinvoice` (
  `CustomerInvoiceID` varchar(15) NOT NULL,
  `DateTimePurchased` datetime NOT NULL,
  `TotalPrice` decimal(8,2) NOT NULL,
  `MemberIDNumber` varchar(13) NOT NULL,
  `BranchID` varchar(15) NOT NULL,
  PRIMARY KEY (`CustomerInvoiceID`),
  KEY `fk_memberID` (`MemberIDNumber`),
  KEY `fk_branchID` (`BranchID`),
  CONSTRAINT `fk_branchID` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_memberID` FOREIGN KEY (`MemberIDNumber`) REFERENCES `member_t` (`MemberIDNumber`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memberinvoice`
--

LOCK TABLES `memberinvoice` WRITE;
/*!40000 ALTER TABLE `memberinvoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `memberinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nonmemberinvoice`
--

DROP TABLE IF EXISTS `nonmemberinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nonmemberinvoice` (
  `CustomerInvoiceID` varchar(15) NOT NULL,
  `DateTimePurchased` datetime NOT NULL,
  `TotalPrice` decimal(8,2) NOT NULL,
  `MemberIDNumber` varchar(13) NOT NULL,
  `BranchID` varchar(15) NOT NULL,
  PRIMARY KEY (`CustomerInvoiceID`),
  KEY `fk_branchID3` (`BranchID`),
  CONSTRAINT `fk_branchID3` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nonmemberinvoice`
--

LOCK TABLES `nonmemberinvoice` WRITE;
/*!40000 ALTER TABLE `nonmemberinvoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `nonmemberinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `ProductID` varchar(15) NOT NULL,
  `SupplierID` varchar(15) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Description` varchar(100) DEFAULT NULL,
  `Price` decimal(8,2) NOT NULL,
  PRIMARY KEY (`ProductID`),
  KEY `fk_supplierID` (`SupplierID`),
  CONSTRAINT `fk_supplierID` FOREIGN KEY (`SupplierID`) REFERENCES `supplier` (`SupplierID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `product_chk_1` CHECK ((`Price` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('00001','sup012','product of the too','blahhh',250.00);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promotion`
--

DROP TABLE IF EXISTS `promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promotion` (
  `PromotionID` varchar(15) NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `Percentage` decimal(5,2) NOT NULL,
  `MemberPointCost` int(11) DEFAULT NULL,
  PRIMARY KEY (`PromotionID`),
  CONSTRAINT `promotion_chk_1` CHECK ((`MemberPointCost` >= 0)),
  CONSTRAINT `promotion_chk_2` CHECK ((`Percentage` > 0.0)),
  CONSTRAINT `promotion_chk_3` CHECK ((`Percentage` <= 100.00))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promotion`
--

LOCK TABLES `promotion` WRITE;
/*!40000 ALTER TABLE `promotion` DISABLE KEYS */;
INSERT INTO `promotion` VALUES ('0001','2019-11-12','2019-11-12',10.00,20);
/*!40000 ALTER TABLE `promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rentableplace`
--

DROP TABLE IF EXISTS `rentableplace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rentableplace` (
  `RentablePlaceID` varchar(15) NOT NULL,
  `BranchID` varchar(15) NOT NULL,
  PRIMARY KEY (`RentablePlaceID`),
  KEY `fk_BranchID4` (`BranchID`),
  CONSTRAINT `fk_BranchID4` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rentableplace`
--

LOCK TABLES `rentableplace` WRITE;
/*!40000 ALTER TABLE `rentableplace` DISABLE KEYS */;
INSERT INTO `rentableplace` VALUES ('r01','0000001');
/*!40000 ALTER TABLE `rentableplace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `SupplierID` varchar(15) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `ContactName` varchar(45) DEFAULT NULL,
  `PhoneNumber` varchar(10) DEFAULT NULL,
  `EmailAddress` varchar(45) DEFAULT NULL,
  `Website` varchar(150) DEFAULT NULL,
  `Address` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`SupplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES ('sup012','supplierA','too','0888888888','too@gmail.com','too.com','blah blah blah');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse` (
  `WarehouseID` varchar(15) NOT NULL,
  `WarehouseName` varchar(45) NOT NULL,
  `WarehouseAddress` varchar(150) NOT NULL,
  `WarehousePhoneNumber` varchar(10) NOT NULL,
  `ManagerIDNumber` varchar(13) NOT NULL,
  `StartDate` date NOT NULL,
  PRIMARY KEY (`WarehouseID`),
  KEY `fk_ManagerID2` (`ManagerIDNumber`),
  CONSTRAINT `fk_ManagerID2` FOREIGN KEY (`ManagerIDNumber`) REFERENCES `employee` (`EmployeeIDNumber`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-17 13:27:12
