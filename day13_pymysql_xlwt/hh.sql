/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.1.49-community : Database - xlsx
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`xlsx` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `xlsx`;

/*Table structure for table `xl` */

DROP TABLE IF EXISTS `xl`;

CREATE TABLE `xl` (
  `name` varchar(20) COLLATE utf8_czech_ci DEFAULT NULL,
  `pass` varchar(20) COLLATE utf8_czech_ci DEFAULT NULL,
  `guo` varchar(20) COLLATE utf8_czech_ci DEFAULT NULL,
  `sheng` varchar(20) COLLATE utf8_czech_ci DEFAULT NULL,
  `lu` varchar(20) COLLATE utf8_czech_ci DEFAULT NULL,
  `jie` varchar(20) COLLATE utf8_czech_ci DEFAULT NULL,
  `gong` varchar(20) COLLATE utf8_czech_ci DEFAULT NULL,
  `xuhao` varchar(2) COLLATE utf8_czech_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

/*Data for the table `xl` */

insert  into `xl`(`name`,`pass`,`guo`,`sheng`,`lu`,`jie`,`gong`,`xuhao`) values ('贾生','123456','USA','纽约省','桃源路','s001','3000','1'),('贾生','123457','USA','纽约省','桃源路','s002','3000','2'),('贾生','123458','USA','纽约省','桃源路','s003','3000','3'),('贾生','123459','USA','纽约省','桃源路','s004','3000','4'),('贾生','123460','USA','纽约省','桃源路','s005','3000','5'),('贾生','123461','USA','纽约省','桃源路','s006','3000','6'),('贾生','123462','USA','纽约省','桃源路','s007','3000','7'),('贾生','123463','USA','纽约省','桃源路','s008','3000','8'),('贾生','123464','USA','纽约省','桃源路','s009','3000','9'),('贾生','123465','USA','纽约省','桃源路','s010','3000','10'),('贾生','123466','USA','纽约省','桃源路','s011','3000','11'),('贾生','123467','USA','纽约省','桃源路','s012','3000','12'),('贾生','123468','USA','纽约省','桃源路','s013','3000','13'),('贾生','123469','USA','纽约省','桃源路','s014','3000','14'),('贾生','123470','USA','纽约省','桃源路','s015','3000','15'),('贾生','123471','USA','纽约省','桃源路','s016','3000','16'),('贾生','123472','USA','纽约省','桃源路','s017','3000','17'),('贾生','123473','USA','纽约省','桃源路','s018','3000','18'),('贾生','123474','USA','纽约省','桃源路','s019','3000','19'),('贾生','123475','USA','纽约省','桃源路','s020','3000','20'),('贾生','123476','USA','纽约省','桃源路','s021','3000','21'),('贾生','123477','USA','纽约省','桃源路','s022','3000','22'),('贾生','123478','USA','纽约省','桃源路','s023','3000','23'),('贾生','123479','USA','纽约省','桃源路','s024','3000','24'),('贾生','123480','USA','纽约省','桃源路','s025','3000','25');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
