-- 准备工作
create database python_test charset=utf8;

use python_test;
-- 显示当前使用的数据
select database();

-- 创建表
create table students (
  id int unsigned PRIMARY key auto_increment not null,
  name VARCHAR(20) default '',
  age tinyint unsigned default 0,
  height decimal(5,2),
  gender enum('男','女','中性','保密') default '保密',
  cls_id int unsigned default 0,
  is_delete bit default 0
);

create table classes(
  id int unsigned auto_increment PRIMARY key not null,
  name varchar(30) not null
);

insert into students values 
(0, '小明', 18, 180.00,2,4,0),
(0, '小月月', 18, 180.00,2,5,0),
(0, '彭于晏', 29, 185.00,1,2,0),
(0, '刘德华', 59, 175.00,1,1,0),
(0, '黄蓉', 38, 150.00,2,1,0),
(0, '凤姐', 28, 180.00,4,1,0),
(0, '王祖贤', 18, 172.00,1,1,1),
(0, '黄小蓉', 36, 180.00,2,1,0),
(0, '周杰伦', 18, 181.00,2,1,0),
(0, '陈坤', 27, 180.00,2,1,0),
(0, '刘亦菲', 25, 166.00,2,1,0),
(0, '金星', 40, 162.00,3,1,0),
(0, '京香', 33, 180.00,2,1,0),
(0, '郭靖', 12, 170.00,1,1,0),
(0, '周杰', 13, 176.00,2,1,0);

insert into classes values 
(0, 'python1班'),
(0, 'python2班'),
(0, 'python3班');


-- 查询
-- 所有
--  select * from 表名

-- 指定字段
-- select 列1,列2 from 表名

-- 字段as起别名
-- select 字段 as 名字 .. from 表名

-- select 表名字段 from 表名
  select students.name, students.age from students 
-- 给表起别名
  --  select 别名.字段 .. from 表名 as 别名
  select st.name, st.age from students as st
  -- 使用了别名后不能使用原来的名字

-- 消除重复行(去重)
-- distinct 字段
select distinct gender from students;



-- 条件查询
-- >, <, >=, <=, =, !=
select * from students where age > 18 and age < 32
select * from students where age = 18

-- 年龄不是小于或者等于18,并且是女性
select * from student where (not age <= 18)  and gender= 2;



-- 模糊查询
--  like 
-- %替换1个或多个
-- _替换一个
-- 查询名称中以 小 开始的名字
select name from students where name like '小%';
select name from students where name like '%小%';

-- 查询有两个字段
select name from students where name like '__'
-- 查询两个以上
select name from students where name like '__%'

-- rlike 正则
-- 查询以 周开始的名称
select name from students where name rlike '^周.*';
select name from students where name rlike '^周.*伦$';



-- 范围查询
--  in(1,3,8)表示一个非连续的范围内
-- 查询两年在18,34的
select name,age from students where age = 18 or age=34;
select name,age from students where age in (12,18,34);

-- not in 不非连续的范围内
-- between... and ..表示在一个连续的范围
select name ,age from students where age BETWEEN 18 and 34;

-- not between .. and .. 表示一个不再连续范围啮的
select name ,age from students where age not BETWEEN 18 and 34;
select name ,age from students where not age BETWEEN 18 and 34;



-- 空判断
-- is null 
select * from students where height is null;
-- is not null



/* 排序 */
-- order by 
-- asc 从小到大 默认
-- desc 从大到小
select * from students where (age between 18 and 30) and gender = 1 order by age;

select * from students where (age between 18 and 30) and gender = 1 order by age desc, id desc;



/* 聚合函数 */
-- count
select count(*) from students where gender=1;
select count(*) as 男性人数 from students where gender = 1;

-- max
select max(height) from students where gender = 1;

-- min
select min(height) from students where gender = 1;

-- avg
select avg(age) from students;
select sum(age)/count(*) from students;

-- round 
-- 保留两位小数
select round(sum(age)/count(*), 2) as 平均值 from students;



/* 分组 */
--  group by
-- 按照性别分组,查询所有的性别
select gender,count(*) from students group by gender;

-- group_concat(name,age)
select gender,group_concat(name, "_", age) from students where gender=1 group by gender;

-- having 可以过滤
select gender,group_concat(name,age) from students group by gender having avg(age)>30;

select gender ,group_concat(name) from students group by gender HAVING count(*) > 2;



/* 分页 */
-- limit是放在最后的
-- limit start, count
select * from students limit 2;
select * from students limit 5, 2;

-- select * from student limit n-1, count



/* 连接查询 */
-- inner join .. on
select * from students inner join classes where students.cls_id = classes.id

-- 按照要求显示姓名和搬家
select students.*,classes.name from students inner join classes on students.cls_id=classes.id;

-- 取别名
select s.*,c.name from students as s inner join classes as c on s.cls_id=c.id;

-- 以班级排序并有课程的
-- 内连接
select c.name, s.* from students as s inner join classes as c on s.cls_id = c.id order by c.name asc;

-- 左连接,以students的表为基准,找不到的为null
select * from students as s left join classes as c on s.cls_id = c.id ;

-- 右连接,以classes为基准,找不到为null(基本没用)
select * from students as s right join classes as c on s.cls_id = c.id;



/* 自关联 */

create table areas(
  aid int primary key,
  atitle varchar(20),
  pid int
)
-- 先查山东pid,然后根据pid查
select aid from areas where atitle='山东省';
select * from areas where pid=370200;

-- 一次查出来
select province.name from areas as province inner join areas as city  on city.pid =province.aid having province.atitle = '山东省'

/* 子查询 */
--  标量子查询,先执行子查询,在执行复查下
select * from students where height = (select max(height) from students);
