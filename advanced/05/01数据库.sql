-- # 数据库
-- # 1. 持久化存储
-- # 2. 读写速度极快
-- # 3. 保证数据的有效性
-- # 4. 对程序支持废除好,容易拓展

-- #RDBMS 关系型数据库

-- """ 数据库 """
-- # 退出 exit
-- # 显示时间 now()

-- # 显示数据库: show databases

-- # 使用数据库: use 数据库名

-- # 创建数据库: create database 数据库名 charset=utf8

-- # 查看当前数据库: show 

-- # 删除数据库: drop database 数据库名 

-- """ 表操作 """
-- # 显示表: show tables

-- # 创建表: create table 数据表名称 (字段 类型 约束[,字段 类型 约束])
-- # create table xxx(id int primary key not null auto, name varchar(30));
-- create table students(
--   id int unsigned not null auto_increment primary key,
--   name varchar(30),
--   age tinyint unsigned default 0,
--   hight decimal(5,2),
--   gender enum('男','女') default '保密',
--   cls_id int unsigned
-- )

-- insert into students values(0, '老王', 18,199,'男',0)

-- # 获取表详情: desc 表名


-- # 修改表-添加字段
-- # alter table 表名 add 列名 类型
-- alter table students add birthday datetiem;

-- -- # alter table 表名 modify 列名 类型及约束
-- alter table students modify birthday date;

-- -- 修改字段名
-- alter table students change birthday birth date default '2000-10-11';

-- -- 删除表字段
-- alter table students drop birth;


/* 增删改查 */
-- 增
-- 0, null, default
insert into classes values(0, '菜鸟班')

-- 部分插入
insert into classes (name,gender) values('小乔',2)


-- 查
select * from classes

-- 改
-- update 表名 set 列1=值,列2=值 ... where 条件:
update students set age=22,gender=1 where id =3;

-- 删
-- delete from 表名 where 条件:
