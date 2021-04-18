-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bikerschoice
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add customer',7,'add_customer'),(26,'Can change customer',7,'change_customer'),(27,'Can delete customer',7,'delete_customer'),(28,'Can view customer',7,'view_customer'),(29,'Can add product',8,'add_product'),(30,'Can change product',8,'change_product'),(31,'Can delete product',8,'delete_product'),(32,'Can view product',8,'view_product'),(33,'Can add order placed',9,'add_orderplaced'),(34,'Can change order placed',9,'change_orderplaced'),(35,'Can delete order placed',9,'delete_orderplaced'),(36,'Can view order placed',9,'view_orderplaced'),(37,'Can add cart',10,'add_cart'),(38,'Can change cart',10,'change_cart'),(39,'Can delete cart',10,'delete_cart'),(40,'Can view cart',10,'view_cart'),(41,'Can add profile',11,'add_profile'),(42,'Can change profile',11,'change_profile'),(43,'Can delete profile',11,'delete_profile'),(44,'Can view profile',11,'view_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$YUiu6179m8br$/U+lsXijCkWRjxYcaicAyrYGKmRe1CZHu9CWXhsJyU8=','2021-04-15 14:56:29.554781',0,'Suman','','','sp554540@gmail.com',1,1,'2021-04-14 09:32:26.234333'),(2,'pbkdf2_sha256$216000$wzRp05wBBJ3h$Y9Q89tKl4i8MBaZWCOYlQDFN41tjw9++PEwyMkD6pzw=','2021-04-15 03:07:32.944715',1,'psuman','','','psuman@gmail.com',1,1,'2021-04-15 03:06:33.014910'),(8,'pbkdf2_sha256$216000$eP7MEQol8ikR$DBFFnP2DpAn6iDSgDckFZmT9tkzo1T3lkM/Q2gysvsc=','2021-04-17 15:49:20.083661',1,'admin','','','admin@gmail.com',1,1,'2021-04-16 08:04:59.032942'),(9,'pbkdf2_sha256$216000$BAg53HncpvIC$a7qT82Tr9XbIR+IEfaSMxgnuhYP+wNsN7t19TJv1oxM=',NULL,0,'u','','','u@gmail.com',0,1,'2021-04-16 08:27:27.406784'),(10,'pbkdf2_sha256$216000$or77XGxQSBW7$C9sHUN4l3gvVpZlh+/BixLV7xKIWWenO142sLfrixiI=','2021-04-17 15:08:55.533372',0,'a','','','a@gmail.com',0,1,'2021-04-17 15:08:42.319581'),(11,'pbkdf2_sha256$216000$UzpnwlFUqCxt$6ylAKIqQfQWYDBp6+NRz4VrESEGwl4ycp2ir7y69X/0=','2021-04-17 15:20:36.650644',0,'Ramesh','','','Ramesh@gmail.com',0,1,'2021-04-17 15:19:29.727919');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-04-15 03:14:29.273510','2','2',2,'[{\"changed\": {\"fields\": [\"Product image\"]}}]',8,2),(2,'2021-04-17 15:03:57.294424','1','Profile object (1)',2,'[{\"changed\": {\"fields\": [\"Firstname\", \"Lastname\", \"Phone\", \"Email\", \"Profile pic\"]}}]',11,8),(3,'2021-04-17 15:05:33.666463','1','1',1,'[{\"added\": {}}]',7,8),(4,'2021-04-17 15:05:57.207613','2','2',1,'[{\"added\": {}}]',7,8),(5,'2021-04-17 15:10:17.211826','1','OrderPlaced object (1)',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',9,8);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'ecommerce','cart'),(7,'ecommerce','customer'),(9,'ecommerce','orderplaced'),(8,'ecommerce','product'),(11,'ecommerce','profile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-14 08:54:32.827816'),(2,'auth','0001_initial','2021-04-14 08:54:33.076099'),(3,'admin','0001_initial','2021-04-14 08:54:34.141224'),(4,'admin','0002_logentry_remove_auto_add','2021-04-14 08:54:34.303785'),(5,'admin','0003_logentry_add_action_flag_choices','2021-04-14 08:54:34.320740'),(6,'contenttypes','0002_remove_content_type_name','2021-04-14 08:54:34.517206'),(7,'auth','0002_alter_permission_name_max_length','2021-04-14 08:54:34.609960'),(8,'auth','0003_alter_user_email_max_length','2021-04-14 08:54:34.646858'),(9,'auth','0004_alter_user_username_opts','2021-04-14 08:54:34.657829'),(10,'auth','0005_alter_user_last_login_null','2021-04-14 08:54:34.750076'),(11,'auth','0006_require_contenttypes_0002','2021-04-14 08:54:34.755016'),(12,'auth','0007_alter_validators_add_error_messages','2021-04-14 08:54:34.768979'),(13,'auth','0008_alter_user_username_max_length','2021-04-14 08:54:34.887652'),(14,'auth','0009_alter_user_last_name_max_length','2021-04-14 08:54:34.985398'),(15,'auth','0010_alter_group_name_max_length','2021-04-14 08:54:35.014311'),(16,'auth','0011_update_proxy_permissions','2021-04-14 08:54:35.027276'),(17,'auth','0012_alter_user_first_name_max_length','2021-04-14 08:54:35.133984'),(18,'ecommerce','0001_initial','2021-04-14 08:54:35.329493'),(19,'ecommerce','0002_profile','2021-04-14 08:54:35.883976'),(20,'ecommerce','0003_auto_20210401_1529','2021-04-14 08:54:35.981200'),(21,'ecommerce','0004_auto_20210407_0748','2021-04-14 08:54:35.995164'),(22,'ecommerce','0005_auto_20210408_1039','2021-04-14 08:54:36.153830'),(23,'ecommerce','0006_auto_20210408_2130','2021-04-14 08:54:36.451509'),(24,'sessions','0001_initial','2021-04-14 08:54:36.486460'),(25,'ecommerce','0007_auto_20210416_1305','2021-04-16 07:20:46.493187'),(26,'ecommerce','0008_auto_20210416_1307','2021-04-16 07:22:34.679975'),(27,'ecommerce','0009_auto_20210416_1309','2021-04-16 07:24:23.173869'),(28,'ecommerce','0010_auto_20210416_1336','2021-04-16 07:52:01.631535');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('b7p8knwrjo3d7pac44m06584bfwbsnqp','.eJxVjEEOwiAQRe_C2hCYMlRcuu8ZyACDVA0kpV0Z765NutDtf-_9l_C0rcVvnRc_J3ERZ3H63QLFB9cdpDvVW5Ox1XWZg9wVedAup5b4eT3cv4NCvXzryIQaFTKGwHkkUlYRsM40GsfZGhxSBmcgo1MIymoXBrLgKIPVcRDvD_oMN8k:1lXnCC:6CGrv-ur-YO5Rb-txVzyNU6hFUWmADTLLRQap7vhI_Y','2021-05-01 15:49:20.088394'),('kjd0ixn78p9fcegrbvnd792uc0it2hb2','e30:1lXHmj:1FdLHMnigzkbZ5CTsHAhp51_OxTAsKVJUdYWgOIChaI','2021-04-30 06:16:57.891867');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ecommerce_cart`
--

DROP TABLE IF EXISTS `ecommerce_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ecommerce_cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `product_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_cart_product_id_5475bc3c_fk_ecommerce_product_id` (`product_id`),
  KEY `ecommerce_cart_user_id_d140a08b_fk_auth_user_id` (`user_id`),
  CONSTRAINT `ecommerce_cart_product_id_5475bc3c_fk_ecommerce_product_id` FOREIGN KEY (`product_id`) REFERENCES `ecommerce_product` (`id`),
  CONSTRAINT `ecommerce_cart_user_id_d140a08b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ecommerce_cart_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ecommerce_cart`
--

LOCK TABLES `ecommerce_cart` WRITE;
/*!40000 ALTER TABLE `ecommerce_cart` DISABLE KEYS */;
INSERT INTO `ecommerce_cart` VALUES (4,1,5,8),(5,1,4,8);
/*!40000 ALTER TABLE `ecommerce_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ecommerce_customer`
--

DROP TABLE IF EXISTS `ecommerce_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ecommerce_customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `locality` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `state` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_customer_user_id_dadc3d00_fk_auth_user_id` (`user_id`),
  CONSTRAINT `ecommerce_customer_user_id_dadc3d00_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ecommerce_customer`
--

LOCK TABLES `ecommerce_customer` WRITE;
/*!40000 ALTER TABLE `ecommerce_customer` DISABLE KEYS */;
INSERT INTO `ecommerce_customer` VALUES (1,'suman parajuli','kathmandu','kathmandu','BAGMATI',2),(2,'suman parajuli','kathmandu','kathmandu','BAGMATI',9),(3,'suman parajuli','kathmandu','kathmandu','BAGMATI',10),(4,'ram','lokanthali','kathmandu','BAGMATI',8);
/*!40000 ALTER TABLE `ecommerce_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ecommerce_orderplaced`
--

DROP TABLE IF EXISTS `ecommerce_orderplaced`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ecommerce_orderplaced` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `ordered_date` datetime(6) NOT NULL,
  `status` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `customer_id` int NOT NULL,
  `product_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_orderplace_customer_id_d44eb6d4_fk_ecommerce` (`customer_id`),
  KEY `ecommerce_orderplace_product_id_3b16e42b_fk_ecommerce` (`product_id`),
  KEY `ecommerce_orderplaced_user_id_27cc84d3_fk_auth_user_id` (`user_id`),
  CONSTRAINT `ecommerce_orderplace_customer_id_d44eb6d4_fk_ecommerce` FOREIGN KEY (`customer_id`) REFERENCES `ecommerce_customer` (`id`),
  CONSTRAINT `ecommerce_orderplace_product_id_3b16e42b_fk_ecommerce` FOREIGN KEY (`product_id`) REFERENCES `ecommerce_product` (`id`),
  CONSTRAINT `ecommerce_orderplaced_user_id_27cc84d3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ecommerce_orderplaced_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ecommerce_orderplaced`
--

LOCK TABLES `ecommerce_orderplaced` WRITE;
/*!40000 ALTER TABLE `ecommerce_orderplaced` DISABLE KEYS */;
INSERT INTO `ecommerce_orderplaced` VALUES (1,1,'2021-04-17 15:09:42.385046','Delievered',3,2,10),(2,1,'2021-04-17 15:11:33.057470','Pending',4,4,8),(3,1,'2021-04-17 15:11:33.079332','Pending',4,5,8);
/*!40000 ALTER TABLE `ecommerce_orderplaced` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ecommerce_product`
--

DROP TABLE IF EXISTS `ecommerce_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ecommerce_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `selling_price` double NOT NULL,
  `discounted_price` double NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `brand` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ecommerce_product`
--

LOCK TABLES `ecommerce_product` WRITE;
/*!40000 ALTER TABLE `ecommerce_product` DISABLE KEYS */;
INSERT INTO `ecommerce_product` VALUES (1,'AGV',36000,34500,'AGV HELMET','AGV','F','productimg/agv_IDidYU6.png'),(2,'AGV -AGV GRAPHICS',38000,37000,'AGV HELMET','AGV','F','productimg/k3-sv-e2205-top_VNKgnmW.png'),(3,'AGV PISTA',44000,43500,'AGV WITH PISTA GRAPHICS','AGV','F','productimg/pista-gp-rr-agv_AObf7Nc.png'),(4,'AGV PISTA-gp',35000,34500,'AGV GRAPHICS','AGV','F','productimg/pista-gp-rr-ece_MduJHz8.png'),(5,'AGV half face',9000,8500,'Half face helmet','AGV','H','productimg/half.png');
/*!40000 ALTER TABLE `ecommerce_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ecommerce_profile`
--

DROP TABLE IF EXISTS `ecommerce_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ecommerce_profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `username` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `profile_pic` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `ecommerce_profile_user_id_e4e7c259_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ecommerce_profile`
--

LOCK TABLES `ecommerce_profile` WRITE;
/*!40000 ALTER TABLE `ecommerce_profile` DISABLE KEYS */;
INSERT INTO `ecommerce_profile` VALUES (1,'suman','parajuli','9863473426','Suman','sp554540@gmail.com','static/userimage/agv.png','2021-04-14 09:32:28.473164',1),(7,NULL,NULL,NULL,'a','','static/userimage/usericon.png','2021-04-17 15:08:44.774240',10),(8,NULL,NULL,NULL,'Ramesh','','static/userimage/usericon.png','2021-04-17 15:19:32.125219',11);
/*!40000 ALTER TABLE `ecommerce_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-18 10:03:07
