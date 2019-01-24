/*
Navicat MySQL Data Transfer

Source Server         : localDB
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : code_learning

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2019-01-24 18:07:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for business_news
-- ----------------------------
DROP TABLE IF EXISTS `business_news`;
CREATE TABLE `business_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_title` varchar(500) DEFAULT NULL,
  `author_name` varchar(255) DEFAULT NULL,
  `author_photo` varchar(255) DEFAULT NULL,
  `release_time` varchar(255) DEFAULT NULL,
  `article_content` text,
  `news_links` varchar(2000) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `from_source` varchar(255) DEFAULT NULL COMMENT '数据来源',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=725 DEFAULT CHARSET=utf8;
