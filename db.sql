/*
SQLyog Ultimate v8.55 
MySQL - 5.1.36-community : Database - db_hotel
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_hotel` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_hotel`;

/*Table structure for table `tbl_admin` */

DROP TABLE IF EXISTS `tbl_admin`;

CREATE TABLE `tbl_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_admin` */

insert  into `tbl_admin`(`id`,`username`,`password`) values (1,'admin','1234');

/*Table structure for table `tbl_bookng` */

DROP TABLE IF EXISTS `tbl_bookng`;

CREATE TABLE `tbl_bookng` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `room_type` varchar(100) DEFAULT NULL,
  `no_of_guest` int(11) DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_out` date DEFAULT NULL,
  `is_vacated` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_bookng` */

insert  into `tbl_bookng`(`id`,`username`,`room_type`,`no_of_guest`,`check_in`,`check_out`,`is_vacated`) values (1,'saba','luxury',2,'2020-10-04','2020-10-06',0),(2,'shivu','deluxe',3,'2020-10-04','2020-10-10',0),(3,'kumar','standard',2,'2020-10-04','2020-10-20',0),(4,'saba','standard',3,'2020-10-05','2020-10-10',0),(5,'saba','AC',5,'2020-10-05','2020-10-06',0);

/*Table structure for table `tbl_room` */

DROP TABLE IF EXISTS `tbl_room`;

CREATE TABLE `tbl_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `room_type` varchar(100) DEFAULT NULL,
  `total_rooms` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_room` */

insert  into `tbl_room`(`id`,`room_type`,`total_rooms`) values (1,'luxury',50),(2,'deluxe',50),(3,'standard',50),(4,'AC',50);

/*Table structure for table `tbl_user_registration` */

DROP TABLE IF EXISTS `tbl_user_registration`;

CREATE TABLE `tbl_user_registration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_user_registration` */

insert  into `tbl_user_registration`(`id`,`username`,`email`,`password`,`mobile`,`datetime`) values (1,'saba','saba@gmail.com','1234','1234','2020-10-04 13:45:32'),(2,'shivu','shivu@gmail.com','1234','1234567890','2020-10-04 13:48:24'),(3,'liba','libarahman62747@gmail.com','7894','96385274','2020-10-05 08:16:41'),(4,'libarahman','liba@gmail.com','9874','74185296','2020-10-05 08:17:26'),(5,'raheem','raheem@gmail.com','01234','85209630','2020-10-05 08:19:28');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
