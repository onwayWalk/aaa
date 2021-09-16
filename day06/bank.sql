/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.1.49-community : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `uuser` */

DROP TABLE IF EXISTS `uuser`;

CREATE TABLE `uuser` (
  `account` int(11) NOT NULL DEFAULT '0',
  `password` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `addr` varchar(100) NOT NULL,
  `balance` int(11) DEFAULT NULL,
  `bankn` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `uuser` */

insert  into `uuser`(`account`,`password`,`name`,`addr`,`balance`,`bankn`) values (1,2,'1','1',100,'悄悄银行'),(2,2,'2','2',0,'悄悄银行'),(3,3,'3','3',0,'悄悄银行'),(5,5,'5','5',0,'悄悄银行'),(11,11,'11','11',0,'悄悄银行'),(102,123,'王五','安徽省',800,'悄悄银行'),(123,123,'123','123',123,'悄悄银行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
