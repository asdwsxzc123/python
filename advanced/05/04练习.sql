-- 创建 "京东" 数据库
create database jing_dong charset=utf8;

-- 使用 "京东" 数据库
use jing_dong;

-- 创建一个商品goods数据表
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
);

-- 向goods表中插入数据

insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default); 
insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default); 
insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default); 
insert into goods values(0,'x240 超极本','超级本','联想','4880',default,default); 
insert into goods values(0,'u330p 13.3英寸超极本','超级本','联想','4299',default,default); 
insert into goods values(0,'svp13226scb 触控超极本','超级本','索尼','7999',default,default); 
insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果','1998',default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果','3388',default,default); 
insert into goods values(0,'ipad mini 配备 retina 显示屏','平板电脑','苹果','2788',default,default); 
insert into goods values(0,'ideacentre c340 20英寸一体电脑 ','台式机','联想','3499',default,default); 
insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔','2899',default,default); 
insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑','台式机','苹果','9188',default,default); 
insert into goods values(0,'at7-7414lp 台式电脑 linux ）','台式机','宏碁','3699',default,default); 
insert into goods values(0,'z220sff f4f06pa工作站','服务器/工作站','惠普','4288',default,default); 
insert into goods values(0,'poweredge ii服务器','服务器/工作站','戴尔','5388',default,default); 
insert into goods values(0,'mac pro专业级台式电脑','服务器/工作站','苹果','28888',default,default); 
insert into goods values(0,'hmz-t3w 头戴显示设备','笔记本配件','索尼','6999',default,default); 
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default); 
insert into goods values(0,'x3250 m4机架式服务器','服务器/工作站','ibm','6888',default,default); 
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);

-- 显示商品品类
select distinct cate_name from goods ;
select cate_name from goods group by cate_name;

-- 所有电脑产品的平均价格,保留两位小数
select round(avg(price),2) as '平均价格' from goods ;


-- 显示每种商品的平均价格
select cate_name,round(avg(price), 2) as '平均价格' from goods group by cate_name;


-- 显示每种类型中最贵,最便宜,平均价,数量
select cate_name,max(price), min(price),round(avg(price), 2),count(*) from goods group by cate_name;

-- 查询所有价格大于平均价格的商品,安价格降序排序
select name,price from goods where price > (select round(avg(price),2) from goods) order by price desc;

-- 查询每种类型中最贵的电脑信息
select * from goods inner JOIN
(
    select 
    name,
    cate_name,
    max(price) as max_price,
    count(*)
    from goods group by cate_name
) as new_goods
on goods.cate_name=new_goods.cate_name and goods.price=new_goods.max_price 


/* 拆表 */
-- 创建商品分类表
create table if not exists goods_cates(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);

INSERT INTO goods_cates (NAME)  (SELECT cate_name FROM goods GROUP BY cate_name);

update goods  as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name= c.id;



-- 修改字段和属性
 ALTER TABLE goods CHANGE cate_name cate_id INT UNSIGNED NOT NULL, CHANGE brand_name brand_id INT UNSIGNED NOT NULL; 

-- 关联对比
ALTER TABLE goods ADD FOREIGN KEY(cate_id) REFERENCES goods_cates(id)

-- 创建新的品牌表
create table goods_brands (
    id int unsigned primary key auto_increment,
    name varchar(40) not null) select brand_name as name from goods group by brand_name;

insert into goods (name,cate_name,brand_name,price)
values('LaserJet Pro P1606dn 黑白激光打印机', 12, 4,'1849');



-- 外键, 尽量少使用外键 
create table goods(
    id int primary key auto_increment not null,
    name varchar(40) default '',
    price decimal(5,2),
    cate_id int unsigned,
    brand_id int unsigned,
    is_show bit default 1,
    is_saleoff bit default 0,
    foreign key(cate_id) references goods_cates(id),
    foreign key(brand_id) references goods_brands(id)
);

-- 删除外键
