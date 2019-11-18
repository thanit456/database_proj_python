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
-- Table structure for table `bkeeps`
--

DROP TABLE IF EXISTS `bkeeps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bkeeps` (
  `ProductID` varchar(15) NOT NULL,
  `BranchID` varchar(15) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`ProductID`,`BranchID`),
  KEY `fk_bkeeps_BranchID` (`BranchID`),
  CONSTRAINT `fk_bkeeps_BranchID` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_bkeeps_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `bkeeps_chk_1` CHECK ((`Quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bkeeps`
--

LOCK TABLES `bkeeps` WRITE;
/*!40000 ALTER TABLE `bkeeps` DISABLE KEYS */;
/*!40000 ALTER TABLE `bkeeps` ENABLE KEYS */;
UNLOCK TABLES;

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
  `ManagerIDNumber` varchar(13) DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  PRIMARY KEY (`BranchID`),
  KEY `fk_managerID` (`ManagerIDNumber`),
  CONSTRAINT `fk_managerID` FOREIGN KEY (`ManagerIDNumber`) REFERENCES `employee` (`EmployeeIDNumber`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES ('0000001','branchA','18/329 blah blah','0994812552',NULL,'2019-11-12');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract1`
--

DROP TABLE IF EXISTS `contract1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contract1` (
  `ContractID` varchar(15) NOT NULL,
  `RentablePlaceID` varchar(15) NOT NULL,
  `RentingCostPerBilling` decimal(13,2) NOT NULL,
  `BillingType` enum('daily','weekly','monthly','yearly','onetime') NOT NULL,
  `OwnerIDNumber` varchar(13) NOT NULL,
  `StartDate` date NOT NULL,
  `ExpireDate` date NOT NULL,
  PRIMARY KEY (`ContractID`),
  KEY `fk_RentablePlaceID` (`RentablePlaceID`),
  KEY `OwnerIDNumber` (`OwnerIDNumber`),
  CONSTRAINT `fk_RentablePlaceID` FOREIGN KEY (`RentablePlaceID`) REFERENCES `rentableplace` (`RentablePlaceID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `contract1_chk_1` CHECK ((`RentingCostPerBilling` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract1`
--

LOCK TABLES `contract1` WRITE;
/*!40000 ALTER TABLE `contract1` DISABLE KEYS */;
/*!40000 ALTER TABLE `contract1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract2`
--

DROP TABLE IF EXISTS `contract2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contract2` (
  `OwnerIDNumber` varchar(13) NOT NULL,
  `OwnerFirstName` varchar(45) NOT NULL,
  `OwnerLastName` varchar(45) DEFAULT NULL,
  `OwnerPhoneNumber` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`OwnerIDNumber`),
  CONSTRAINT `fk_contract2` FOREIGN KEY (`OwnerIDNumber`) REFERENCES `contract1` (`OwnerIDNumber`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract2`
--

LOCK TABLES `contract2` WRITE;
/*!40000 ALTER TABLE `contract2` DISABLE KEYS */;
/*!40000 ALTER TABLE `contract2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `createinvoice1`
--

DROP TABLE IF EXISTS `createinvoice1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `createinvoice1` (
  `InvoiceID` varchar(15) NOT NULL,
  `ProductID` varchar(15) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`InvoiceID`,`ProductID`),
  KEY `fk_createInvoice_ProductID` (`ProductID`),
  CONSTRAINT `fk_createInvoice_InvoiceID` FOREIGN KEY (`InvoiceID`) REFERENCES `invoice` (`InvoiceID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_createInvoice_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `createinvoice1_chk_1` CHECK ((`Quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `createinvoice1`
--

LOCK TABLES `createinvoice1` WRITE;
/*!40000 ALTER TABLE `createinvoice1` DISABLE KEYS */;
/*!40000 ALTER TABLE `createinvoice1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `createinvoice2`
--

DROP TABLE IF EXISTS `createinvoice2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `createinvoice2` (
  `ProductID` varchar(15) NOT NULL,
  `SupplierID` varchar(15) NOT NULL,
  PRIMARY KEY (`ProductID`),
  KEY `fk_createInvoice2_SupplierID` (`SupplierID`),
  CONSTRAINT `fk_createInvoice2_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `createinvoice1` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_createInvoice2_SupplierID` FOREIGN KEY (`SupplierID`) REFERENCES `supplier` (`SupplierID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `createinvoice2`
--

LOCK TABLES `createinvoice2` WRITE;
/*!40000 ALTER TABLE `createinvoice2` DISABLE KEYS */;
/*!40000 ALTER TABLE `createinvoice2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EmployeeIDNumber` varchar(13) NOT NULL,
  `BranchID` varchar(15) DEFAULT NULL,
  `BranchStartDate` date DEFAULT NULL,
  `SupervisorIDNumber` varchar(13) DEFAULT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `BirthDate` date DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `JobPosition` varchar(45) DEFAULT NULL,
  `JobType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeIDNumber`),
  KEY `fk_supervisor` (`SupervisorIDNumber`),
  KEY `fk_branchID2` (`BranchID`),
  CONSTRAINT `fk_branchID2` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_supervisor` FOREIGN KEY (`SupervisorIDNumber`) REFERENCES `employee` (`EmployeeIDNumber`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
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
-- Table structure for table `imports`
--

DROP TABLE IF EXISTS `imports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imports` (
  `ImportID` varchar(15) NOT NULL,
  `ProductID` varchar(15) NOT NULL,
  `WarehouseID` varchar(15) NOT NULL,
  `BranchID` varchar(15) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`ImportID`,`ProductID`,`WarehouseID`,`BranchID`),
  KEY `fk_imports_ProductID` (`ProductID`),
  KEY `fk_imports_WarehouseID` (`WarehouseID`),
  KEY `fk_imports_BranchID` (`BranchID`),
  CONSTRAINT `fk_imports_BranchID` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_imports_ImportID` FOREIGN KEY (`ImportID`) REFERENCES `importid` (`ImportID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_imports_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_imports_WarehouseID` FOREIGN KEY (`WarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `imports_chk_1` CHECK ((`Quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imports`
--

LOCK TABLES `imports` WRITE;
/*!40000 ALTER TABLE `imports` DISABLE KEYS */;
/*!40000 ALTER TABLE `imports` ENABLE KEYS */;
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
  PRIMARY KEY (`InvoiceID`),
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
-- Table structure for table `mcontains`
--

DROP TABLE IF EXISTS `mcontains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mcontains` (
  `CustomerInvoiceID` varchar(15) NOT NULL,
  `ProductID` varchar(15) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`CustomerInvoiceID`,`ProductID`),
  KEY `fk_mcontains_ProductID` (`ProductID`),
  CONSTRAINT `fk_mcontains_CustomerInvoiceID` FOREIGN KEY (`CustomerInvoiceID`) REFERENCES `memberinvoice` (`CustomerInvoiceID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_mcontains_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `mcontains_chk_1` CHECK ((`Quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mcontains`
--

LOCK TABLES `mcontains` WRITE;
/*!40000 ALTER TABLE `mcontains` DISABLE KEYS */;
/*!40000 ALTER TABLE `mcontains` ENABLE KEYS */;
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
  KEY `fk_branchID3` (`BranchID`),
  CONSTRAINT `fk_branchID` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_branchID3` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_memberID` FOREIGN KEY (`MemberIDNumber`) REFERENCES `member_t` (`MemberIDNumber`) ON DELETE RESTRICT ON UPDATE CASCADE
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
-- Table structure for table `ncontains`
--

DROP TABLE IF EXISTS `ncontains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ncontains` (
  `CustomerInvoiceID` varchar(15) NOT NULL,
  `ProductID` varchar(15) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`CustomerInvoiceID`,`ProductID`),
  KEY `fk_ncontains_ProductID` (`ProductID`),
  CONSTRAINT `fk_ncontains_CustomerInvoiceID` FOREIGN KEY (`CustomerInvoiceID`) REFERENCES `nonmemberinvoice` (`CustomerInvoiceID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_ncontains_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ncontains_chk_1` CHECK ((`Quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ncontains`
--

LOCK TABLES `ncontains` WRITE;
/*!40000 ALTER TABLE `ncontains` DISABLE KEYS */;
/*!40000 ALTER TABLE `ncontains` ENABLE KEYS */;
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
  `BranchID` varchar(15) NOT NULL,
  PRIMARY KEY (`CustomerInvoiceID`),
  KEY `fk_branchID3` (`BranchID`)
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
  `ProductID` varchar(15) NOT NULL,
  PRIMARY KEY (`PromotionID`),
  KEY `fk_productID` (`ProductID`),
  CONSTRAINT `fk_productID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
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
/*!40000 ALTER TABLE `rentableplace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salesat`
--

DROP TABLE IF EXISTS `salesat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salesat` (
  `PromotionID` varchar(15) NOT NULL,
  `BranchID` varchar(15) NOT NULL,
  PRIMARY KEY (`PromotionID`,`BranchID`),
  KEY `fk_salesat_BranchID` (`BranchID`),
  CONSTRAINT `fk_salesat_BranchID` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_salesat_PromotionID` FOREIGN KEY (`PromotionID`) REFERENCES `promotion` (`PromotionID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salesat`
--

LOCK TABLES `salesat` WRITE;
/*!40000 ALTER TABLE `salesat` DISABLE KEYS */;
/*!40000 ALTER TABLE `salesat` ENABLE KEYS */;
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
  `ManagerIDNumber` varchar(13) DEFAULT NULL,
  `StartDate` date NOT NULL,
  PRIMARY KEY (`WarehouseID`),
  KEY `fk_managerID2` (`ManagerIDNumber`),
  CONSTRAINT `fk_managerID2` FOREIGN KEY (`ManagerIDNumber`) REFERENCES `employee` (`EmployeeIDNumber`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wkeeps`
--

DROP TABLE IF EXISTS `wkeeps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wkeeps` (
  `ProductID` varchar(15) NOT NULL,
  `WarehouseID` varchar(15) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`ProductID`,`WarehouseID`),
  KEY `fk_wkeeps_WarehouseID` (`WarehouseID`),
  CONSTRAINT `fk_wkeeps_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_wkeeps_WarehouseID` FOREIGN KEY (`WarehouseID`) REFERENCES `warehouse` (`WarehouseID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `wkeeps_chk_1` CHECK ((`Quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wkeeps`
--

LOCK TABLES `wkeeps` WRITE;
/*!40000 ALTER TABLE `wkeeps` DISABLE KEYS */;
/*!40000 ALTER TABLE `wkeeps` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-18 19:53:08