/*
 Navicat Premium Data Transfer

 Source Server         : 本地：3306
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : localhost:3306
 Source Schema         : food_db

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 07/08/2022 01:41:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app_access_log
-- ----------------------------
DROP TABLE IF EXISTS `app_access_log`;
CREATE TABLE `app_access_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` bigint NOT NULL DEFAULT 0 COMMENT 'uid',
  `referer_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'get和post参数',
  `ua` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '访问ua',
  `ip` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '访问ip',
  `note` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT 'json格式备注字段',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_uid`(`uid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户访问记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of app_access_log
-- ----------------------------

-- ----------------------------
-- Table structure for app_error_log
-- ----------------------------
DROP TABLE IF EXISTS `app_error_log`;
CREATE TABLE `app_error_log`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `referer_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'get和post参数',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '日志内容',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = 'app错误日表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of app_error_log
-- ----------------------------
INSERT INTO `app_error_log` VALUES (1, 'http://127.0.0.1:8999/stat/index', 'http://127.0.0.1:8999/chart/finance', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 22:28:25');
INSERT INTO `app_error_log` VALUES (2, 'http://127.0.0.1:8999/stat/index', 'http://127.0.0.1:8999/chart/finance', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 22:28:27');
INSERT INTO `app_error_log` VALUES (3, 'http://127.0.0.1:8999/stat/share', 'http://127.0.0.1:8999/chart/share', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 22:28:29');
INSERT INTO `app_error_log` VALUES (4, 'http://127.0.0.1:8999/stat/index', 'http://127.0.0.1:8999/chart/finance', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 22:28:30');
INSERT INTO `app_error_log` VALUES (5, 'http://127.0.0.1:8999/', 'http://127.0.0.1:8999/chart/dashboard', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 22:28:35');
INSERT INTO `app_error_log` VALUES (6, 'http://127.0.0.1:8999/', 'http://127.0.0.1:8999/chart/finance', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 22:28:35');
INSERT INTO `app_error_log` VALUES (7, 'http://127.0.0.1:8999/stat/index', 'http://127.0.0.1:8999/chart/finance', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 22:28:36');
INSERT INTO `app_error_log` VALUES (8, 'http://127.0.0.1:8999/member/index', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:08:44');
INSERT INTO `app_error_log` VALUES (9, 'http://127.0.0.1:8999/member/index', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:08:46');
INSERT INTO `app_error_log` VALUES (10, 'http://127.0.0.1:8999/member/index', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:08:53');
INSERT INTO `app_error_log` VALUES (11, 'http://127.0.0.1:8999/member/index', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:08:58');
INSERT INTO `app_error_log` VALUES (12, 'http://127.0.0.1:8999/member/index', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:10:41');
INSERT INTO `app_error_log` VALUES (13, 'http://127.0.0.1:8999/member/index', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:29:53');
INSERT INTO `app_error_log` VALUES (14, 'http://127.0.0.1:8999/member/index', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:29:55');
INSERT INTO `app_error_log` VALUES (15, '', 'http://127.0.0.1:8999/static/bootstrap/bootstrap.min.css.map', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:30:01');
INSERT INTO `app_error_log` VALUES (16, '', 'http://127.0.0.1:8999/static/upload/https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:30:35');
INSERT INTO `app_error_log` VALUES (17, '', 'http://127.0.0.1:8999/static/bootstrap/bootstrap.min.css.map', '{}', '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.', '2022-08-06 23:32:43');

-- ----------------------------
-- Table structure for food
-- ----------------------------
DROP TABLE IF EXISTS `food`;
CREATE TABLE `food`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `cat_id` int NOT NULL DEFAULT 0 COMMENT '分类id',
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '书籍名称',
  `price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '售卖金额',
  `main_image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '主图',
  `summary` varchar(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '描述',
  `stock` int NOT NULL DEFAULT 0 COMMENT '库存量',
  `tags` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT 'tag关键字，以\",\"连接',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态 1：有效 0：无效',
  `month_count` int NOT NULL DEFAULT 0 COMMENT '月销售数量',
  `total_count` int NOT NULL DEFAULT 0 COMMENT '总销售量',
  `view_count` int NOT NULL DEFAULT 0 COMMENT '总浏览次数',
  `comment_count` int NOT NULL DEFAULT 0 COMMENT '总评论量',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后插入时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '食品表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of food
-- ----------------------------
INSERT INTO `food` VALUES (1, 1, '白切鸡', 25.00, '20220803/fabac9036908452e85d22360c0938091.jpg', '<p><span style=\"color: rgb(247, 49, 49); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">白切鸡</span><span style=\"color: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">一般指</span><span style=\"color: rgb(247, 49, 49); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">白斩鸡</span><span style=\"color: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">。&nbsp;</span><span style=\"color: rgb(247, 49, 49); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">白斩鸡</span><span style=\"color: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">又叫</span><span style=\"color: rgb(247, 49, 49); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">白切鸡</span><span style=\"color: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 13px; background-color: rgb(255, 255, 255);\">，是一道中华民族特色菜肴，是一道经典的粤菜，后来在南方菜系中普遍存在。</span></p>', 99, '鲜美,多汁,嫩', 1, 0, 0, 0, 0, '2022-08-03 20:08:20', '2022-08-03 16:41:27');
INSERT INTO `food` VALUES (2, 2, '番茄炒鸡蛋', 15.00, '20220803/7d90f2ae63fb4520ad4159d35be705cb.jpg', '<p><img src=\"http://127.0.0.1:8999/static/upload/20220803/b8673351bf68449f94a9f74505420d00.jpg\"/></p><p>超级好吃的番茄炒鸡蛋</p><p><img src=\"http://127.0.0.1:8999/static/upload/20220803/0a159c0d40b14e4cba9f76e6f5850c61.jpg\"/></p>', 99, '好吃', 1, 0, 0, 0, 0, '2022-08-04 17:53:21', '2022-08-03 20:18:13');

-- ----------------------------
-- Table structure for food_cat
-- ----------------------------
DROP TABLE IF EXISTS `food_cat`;
CREATE TABLE `food_cat`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '类别名称',
  `weight` tinyint NOT NULL DEFAULT 1 COMMENT '权重',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态 1：有效 0：无效',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_name`(`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '食品分类' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of food_cat
-- ----------------------------
INSERT INTO `food_cat` VALUES (1, '粤菜', 1, 1, '2022-08-03 00:26:13', '2022-08-03 00:26:13');
INSERT INTO `food_cat` VALUES (2, '湘菜', 1, 1, '2022-08-03 00:26:23', '2022-08-03 00:26:23');

-- ----------------------------
-- Table structure for food_sale_change_log
-- ----------------------------
DROP TABLE IF EXISTS `food_sale_change_log`;
CREATE TABLE `food_sale_change_log`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `food_id` int NOT NULL DEFAULT 0 COMMENT '商品id',
  `quantity` int NOT NULL DEFAULT 0 COMMENT '售卖数量',
  `price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '售卖金额',
  `member_id` int NOT NULL DEFAULT 0 COMMENT '会员id',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '售卖时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_food_id_id`(`food_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '商品销售情况' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of food_sale_change_log
-- ----------------------------

-- ----------------------------
-- Table structure for food_stock_change_log
-- ----------------------------
DROP TABLE IF EXISTS `food_stock_change_log`;
CREATE TABLE `food_stock_change_log`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `food_id` int NOT NULL COMMENT '商品id',
  `unit` int NOT NULL DEFAULT 0 COMMENT '变更多少',
  `total_stock` int NOT NULL DEFAULT 0 COMMENT '变更之后总量',
  `note` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '备注字段',
  `created_time` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_food_id`(`food_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '数据库存变更表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of food_stock_change_log
-- ----------------------------
INSERT INTO `food_stock_change_log` VALUES (1, 1, 100, 100, '后台修改', '2022-08-03 16:41:27');
INSERT INTO `food_stock_change_log` VALUES (2, 1, 1, 101, '后台修改', '2022-08-03 19:55:03');
INSERT INTO `food_stock_change_log` VALUES (3, 1, -1, 100, '后台修改', '2022-08-03 19:55:48');
INSERT INTO `food_stock_change_log` VALUES (4, 1, -1, 99, '后台修改', '2022-08-03 20:08:20');
INSERT INTO `food_stock_change_log` VALUES (5, 2, 100, 100, '后台修改', '2022-08-03 20:18:13');
INSERT INTO `food_stock_change_log` VALUES (6, 2, 0, 100, '后台修改', '2022-08-03 20:21:14');
INSERT INTO `food_stock_change_log` VALUES (7, 2, 0, 100, '后台修改', '2022-08-03 21:20:28');
INSERT INTO `food_stock_change_log` VALUES (8, 2, 0, 100, '后台修改', '2022-08-03 23:13:44');
INSERT INTO `food_stock_change_log` VALUES (9, 2, 0, 100, '后台修改', '2022-08-03 23:16:05');
INSERT INTO `food_stock_change_log` VALUES (10, 2, 0, 100, '后台修改', '2022-08-03 23:17:29');
INSERT INTO `food_stock_change_log` VALUES (11, 2, 0, 100, '后台修改', '2022-08-03 23:17:36');
INSERT INTO `food_stock_change_log` VALUES (12, 2, 0, 100, '后台修改', '2022-08-04 17:53:21');
INSERT INTO `food_stock_change_log` VALUES (13, 2, -1, 99, '在线购买', '2022-08-06 23:10:18');

-- ----------------------------
-- Table structure for images
-- ----------------------------
DROP TABLE IF EXISTS `images`;
CREATE TABLE `images`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `file_key` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '文件名',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of images
-- ----------------------------
INSERT INTO `images` VALUES (1, '20220803/1f7283769f324a1db8f9b2e4d9697eb1.jpg', '2022-08-03 00:25:40');
INSERT INTO `images` VALUES (2, '20220803/fabac9036908452e85d22360c0938091.jpg', '2022-08-03 15:54:30');
INSERT INTO `images` VALUES (3, '20220803/9cbac43f237740078a5854b520f23132.jpg', '2022-08-03 18:49:24');
INSERT INTO `images` VALUES (4, '20220803/dee58f3870ef43d99c1c41f88b1280fb.jpg', '2022-08-03 18:49:35');
INSERT INTO `images` VALUES (5, '20220803/5a43356578be4c38b11cfc0c9d79b0bf.jpg', '2022-08-03 18:49:45');
INSERT INTO `images` VALUES (6, '20220803/afccbb48370a4f2a881f63c7c460d811.jpg', '2022-08-03 18:49:53');
INSERT INTO `images` VALUES (7, '20220803/8377f10d10e244c48052dab404d07b85.jpg', '2022-08-03 18:58:11');
INSERT INTO `images` VALUES (8, '20220803/10ed4daddf3d46f1a756b883a8c075d8.jpg', '2022-08-03 18:59:54');
INSERT INTO `images` VALUES (9, '20220803/515828d3cfe9422285c9fa7a5a6a852b.jpg', '2022-08-03 19:07:33');
INSERT INTO `images` VALUES (10, '20220803/c8092ae410194dde9f086bff24e9fedf.jpg', '2022-08-03 19:07:40');
INSERT INTO `images` VALUES (11, '20220803/171ba4a813aa408a89c8a760211b6891.jpg', '2022-08-03 19:10:08');
INSERT INTO `images` VALUES (12, '20220803/de2b8142e632465c9633df00cd2f1c0b.jpg', '2022-08-03 19:10:15');
INSERT INTO `images` VALUES (13, '20220803/8cd437246494433f8490da8346832996.jpg', '2022-08-03 19:11:27');
INSERT INTO `images` VALUES (14, '20220803/44abf5609dc0472fa04c35537a893f45.jpg', '2022-08-03 19:12:59');
INSERT INTO `images` VALUES (15, '20220803/4db35c1292684ea98197bb52b29153e4.jpg', '2022-08-03 19:13:07');
INSERT INTO `images` VALUES (16, '20220803/3d7392d5948c438baedb8b9046d8eff3.jpg', '2022-08-03 20:16:17');
INSERT INTO `images` VALUES (17, '20220803/7d90f2ae63fb4520ad4159d35be705cb.jpg', '2022-08-03 20:18:00');
INSERT INTO `images` VALUES (18, '20220803/17987459730f43d0a3648f23e4ff36b4.jpg', '2022-08-03 21:19:50');
INSERT INTO `images` VALUES (19, '20220803/0a159c0d40b14e4cba9f76e6f5850c61.jpg', '2022-08-03 21:20:25');
INSERT INTO `images` VALUES (20, '20220803/871bb798c5d343f3b6483926006abe27.jpg', '2022-08-03 21:23:07');
INSERT INTO `images` VALUES (21, '20220803/56303e2afa6c4998a64c4517af05692e.jpg', '2022-08-03 21:23:44');
INSERT INTO `images` VALUES (22, '20220803/40f5483d3e254dae8dd19fe008fe17cc.jpg', '2022-08-03 23:13:41');
INSERT INTO `images` VALUES (23, '20220803/b8673351bf68449f94a9f74505420d00.jpg', '2022-08-03 23:16:02');
INSERT INTO `images` VALUES (24, '20220803/ee7cbacbfe9d42b0b106521f426ce8ef.jpg', '2022-08-03 23:25:10');
INSERT INTO `images` VALUES (25, '20220804/4c1d5db09b954df397b846cbd6307dfb.jpg', '2022-08-04 09:21:31');
INSERT INTO `images` VALUES (26, '20220804/c1a42a948bfb4ad7bc44419c31225826.jpg', '2022-08-04 09:22:28');
INSERT INTO `images` VALUES (27, '20220804/6f19ecaedfbc4d89af18ab10cc3a4a9f.jpg', '2022-08-04 09:22:46');
INSERT INTO `images` VALUES (28, '20220804/0746b4836d944db5a46d65a5c2c34253.jpg', '2022-08-04 09:24:20');
INSERT INTO `images` VALUES (29, '20220804/5228c8c860ea43c4ad44df16fed35aaa.jpg', '2022-08-04 09:25:27');
INSERT INTO `images` VALUES (30, '20220804/a4717d9761b944d7bb436d6721b51bc7.jpg', '2022-08-04 09:25:37');
INSERT INTO `images` VALUES (31, '20220804/0291353ffde74c5998e30f4d003e3229.jpg', '2022-08-04 09:28:41');
INSERT INTO `images` VALUES (32, '20220804/d4203fa3f85245fdb7e2ce1a2ce5ed94.jpg', '2022-08-04 09:30:12');
INSERT INTO `images` VALUES (33, '20220804/12d6a9dd4aa3456da9c984711c3cd7e4.jpg', '2022-08-04 09:31:04');
INSERT INTO `images` VALUES (34, '20220804/7197d0c14f944537b1669104844e6583.jpg', '2022-08-04 09:31:53');
INSERT INTO `images` VALUES (35, '20220804/5002726af143413ba9eedd39a8230767.jpg', '2022-08-04 09:37:43');

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '会员名',
  `mobile` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '会员手机号码',
  `sex` tinyint(1) NOT NULL DEFAULT 0 COMMENT '性别 1：男 2：女',
  `avatar` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '会员头像',
  `salt` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '随机salt',
  `reg_ip` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '注册ip',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态 1：有效 0：无效',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '会员表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member
-- ----------------------------

-- ----------------------------
-- Table structure for member_address
-- ----------------------------
DROP TABLE IF EXISTS `member_address`;
CREATE TABLE `member_address`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL DEFAULT 0 COMMENT '会员id',
  `nickname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '收货人姓名',
  `mobile` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '收货人手机号码',
  `province_id` int NOT NULL DEFAULT 0 COMMENT '省id',
  `province_str` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '省名称',
  `city_id` int NOT NULL DEFAULT 0 COMMENT '城市id',
  `city_str` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '市名称',
  `area_id` int NOT NULL DEFAULT 0 COMMENT '区域id',
  `area_str` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '区域名称',
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '详细地址',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '是否有效 1：有效 0：无效',
  `is_default` tinyint(1) NOT NULL DEFAULT 0 COMMENT '默认地址',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_member_id_status`(`member_id`, `status`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '会员收货地址' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member_address
-- ----------------------------

-- ----------------------------
-- Table structure for member_cart
-- ----------------------------
DROP TABLE IF EXISTS `member_cart`;
CREATE TABLE `member_cart`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL DEFAULT 0 COMMENT '会员id',
  `food_id` int NOT NULL DEFAULT 0 COMMENT '商品id',
  `quantity` int NOT NULL DEFAULT 0 COMMENT '数量',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_member_id`(`member_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '购物车' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member_cart
-- ----------------------------

-- ----------------------------
-- Table structure for member_comments
-- ----------------------------
DROP TABLE IF EXISTS `member_comments`;
CREATE TABLE `member_comments`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL DEFAULT 0 COMMENT '会员id',
  `food_ids` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '商品ids',
  `pay_order_id` int NOT NULL DEFAULT 0 COMMENT '订单id',
  `score` tinyint NOT NULL DEFAULT 0 COMMENT '评分',
  `content` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '评论内容',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_member_id`(`member_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '会员评论表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member_comments
-- ----------------------------

-- ----------------------------
-- Table structure for oauth_access_token
-- ----------------------------
DROP TABLE IF EXISTS `oauth_access_token`;
CREATE TABLE `oauth_access_token`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `access_token` varchar(600) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `expired_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '过期时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_expired_time`(`expired_time`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '微信的access_token 用户调用其他接口的' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of oauth_access_token
-- ----------------------------

-- ----------------------------
-- Table structure for oauth_member_bind
-- ----------------------------
DROP TABLE IF EXISTS `oauth_member_bind`;
CREATE TABLE `oauth_member_bind`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL DEFAULT 0 COMMENT '会员id',
  `client_type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '客户端来源类型。qq,weibo,weixin',
  `type` tinyint NOT NULL DEFAULT 0 COMMENT '类型 type 1:wechat ',
  `openid` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '第三方id',
  `unionid` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `extra` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '额外字段',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_type_openid`(`type`, `openid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '第三方登录绑定关系' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of oauth_member_bind
-- ----------------------------

-- ----------------------------
-- Table structure for pay_order
-- ----------------------------
DROP TABLE IF EXISTS `pay_order`;
CREATE TABLE `pay_order`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '随机订单号',
  `member_id` bigint NOT NULL DEFAULT 0 COMMENT '会员id',
  `total_price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '订单应付金额',
  `yun_price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '运费金额',
  `pay_price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '订单实付金额',
  `pay_sn` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '第三方流水号',
  `prepay_id` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '第三方预付id',
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '备注信息',
  `status` tinyint NOT NULL DEFAULT 0 COMMENT '1：支付完成 0 无效 -1 申请退款 -2 退款中 -9 退款成功  -8 待支付  -7 完成支付待确认',
  `express_status` tinyint NOT NULL DEFAULT 0 COMMENT '快递状态，-8 待支付 -7 已付款待发货 1：确认收货 0：失败',
  `express_address_id` int NOT NULL DEFAULT 0 COMMENT '快递地址id',
  `express_info` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '快递信息',
  `comment_status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '评论状态',
  `pay_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '付款到账时间',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最近一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_order_sn`(`order_sn`) USING BTREE,
  INDEX `idx_member_id_status`(`member_id`, `status`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '在线购买订单表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pay_order
-- ----------------------------

-- ----------------------------
-- Table structure for pay_order_callback_data
-- ----------------------------
DROP TABLE IF EXISTS `pay_order_callback_data`;
CREATE TABLE `pay_order_callback_data`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `pay_order_id` int NOT NULL DEFAULT 0 COMMENT '支付订单id',
  `pay_data` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '支付回调信息',
  `refund_data` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '退款回调信息',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `pay_order_id`(`pay_order_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pay_order_callback_data
-- ----------------------------

-- ----------------------------
-- Table structure for pay_order_item
-- ----------------------------
DROP TABLE IF EXISTS `pay_order_item`;
CREATE TABLE `pay_order_item`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `pay_order_id` int NOT NULL DEFAULT 0 COMMENT '订单id',
  `member_id` bigint NOT NULL DEFAULT 0 COMMENT '会员id',
  `quantity` int NOT NULL DEFAULT 1 COMMENT '购买数量 默认1份',
  `price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '商品总价格，售价 * 数量',
  `food_id` int NOT NULL DEFAULT 0 COMMENT '美食表id',
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '备注信息',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态：1：成功 0 失败',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最近一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_order_id`(`pay_order_id`) USING BTREE,
  INDEX `idx_food_id`(`food_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '订单详情表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pay_order_item
-- ----------------------------

-- ----------------------------
-- Table structure for queue_list
-- ----------------------------
DROP TABLE IF EXISTS `queue_list`;
CREATE TABLE `queue_list`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `queue_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '队列名字',
  `data` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '队列数据',
  `status` tinyint(1) NOT NULL DEFAULT -1 COMMENT '状态 -1 待处理 1 已处理',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '事件队列表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of queue_list
-- ----------------------------

-- ----------------------------
-- Table structure for stat_daily_food
-- ----------------------------
DROP TABLE IF EXISTS `stat_daily_food`;
CREATE TABLE `stat_daily_food`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `food_id` int NOT NULL DEFAULT 0 COMMENT '菜品id',
  `total_count` int NOT NULL DEFAULT 0 COMMENT '售卖总数量',
  `total_pay_money` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '总售卖金额',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `date_food_id`(`date`, `food_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '书籍售卖日统计' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stat_daily_food
-- ----------------------------

-- ----------------------------
-- Table structure for stat_daily_member
-- ----------------------------
DROP TABLE IF EXISTS `stat_daily_member`;
CREATE TABLE `stat_daily_member`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL COMMENT '日期',
  `member_id` int NOT NULL DEFAULT 0 COMMENT '会员id',
  `total_shared_count` int NOT NULL DEFAULT 0 COMMENT '当日分享总次数',
  `total_pay_money` decimal(10, 2) NOT NULL COMMENT '当日付款总金额',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_date_member_id`(`date`, `member_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '会员日统计' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of stat_daily_member
-- ----------------------------

-- ----------------------------
-- Table structure for stat_daily_site
-- ----------------------------
DROP TABLE IF EXISTS `stat_daily_site`;
CREATE TABLE `stat_daily_site`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL COMMENT '日期',
  `total_pay_money` decimal(10, 2) NOT NULL COMMENT '当日应收总金额',
  `total_member_count` int NOT NULL COMMENT '会员总数',
  `total_new_member_count` int NOT NULL COMMENT '当日新增会员数',
  `total_order_count` int NOT NULL COMMENT '当日订单数',
  `total_shared_count` int NOT NULL,
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_date`(`date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '全站日统计' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of stat_daily_site
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `uid` bigint NOT NULL AUTO_INCREMENT COMMENT '用户uid',
  `nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `mobile` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '手机号码',
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '邮箱地址',
  `sex` tinyint(1) NOT NULL DEFAULT 0 COMMENT '1：男 2：女 0：没填写',
  `avatar` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '头像',
  `login_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '登录用户名',
  `login_pwd` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '登录密码',
  `login_salt` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '登录密码的随机加密秘钥',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1：有效 0：无效',
  `updated_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '最后一次更新时间',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '插入时间',
  PRIMARY KEY (`uid`) USING BTREE,
  UNIQUE INDEX `login_name`(`login_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户表（管理员）' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '不掉发的羊驼', '11012345679', 'c249084156@163.com', 1, '', 'even', '816440c40b7a9d55ff9eb7b20760862c', 'cF3JfH5FJfQ8B2Ba', 1, '2021-03-15 14:08:48', '2021-03-15 14:08:48');
INSERT INTO `user` VALUES (2, 'python', '13318011750', '1136334017@qq.com', 0, '', 'python', '7771cfdbabe30d0c7c3c056a5712127f', 'qWY6phXNK7OQ47pl', 0, '2022-08-02 17:58:31', '2022-08-02 07:32:49');
INSERT INTO `user` VALUES (3, 'java', '13318011750', '1136334017@qq.com', 0, '', 'java', '02438e84031f405f3d23f84035a75ddb', 'diI36pO6vRSfI1EN', 1, '2022-08-02 11:34:47', '2022-08-02 11:34:46');
INSERT INTO `user` VALUES (4, 'c++', '13318011750', '1136334017@qq.com', 0, '', 'c++', '4c54469b5a2e6b4f4081dee301868b7e', 'XEBk0tgB7zMYlvHd', 1, '2022-08-02 17:51:00', '2022-08-02 17:50:59');

-- ----------------------------
-- Table structure for wx_share_history
-- ----------------------------
DROP TABLE IF EXISTS `wx_share_history`;
CREATE TABLE `wx_share_history`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL DEFAULT 0 COMMENT '会员id',
  `share_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '分享的页面url',
  `created_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '微信分享记录' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of wx_share_history
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
