create table orders 
(
	id int unsigned primary key auto_increment not null,
    order_date_time TIMESTAMP not null,
	customer_id int unsigned not null
)
