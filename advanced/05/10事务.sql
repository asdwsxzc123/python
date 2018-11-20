-- 事务,订单和银行系统
-- 一个操作序列,这些操作要么执行,要么不执行
-- 四大特效(ACID)
-- 原子性,(atomicty), 一个事务必须被视为一个不可分割的最小工作单元,整个事务中的所又操作要么全部提交成功,要么全部失败回滚,对于事务来说,不能只执行其中一部分操作
-- 一致性(consistency), 数据库总是从一个一致性的状态转换到另一个一致性的状态
-- 隔离性(isolation), 一个事务所做的修改在最终提交之前,对其他事务是不可见的.
-- 持久性(durability) 一旦事务提交,则其所做的修改永久报保存在数据库

-- 1. 检查支票账户的月高于或者等于200元
-- 2. 从支票账户余额中减去200元
-- 3. 在储蓄账户中增加200元
-- 上述三个步骤必须打包在一个事务中,任何一个步骤失败,必须回滚所有的步骤

-- python默认开启了事务,所以需要commit
-- 开启事务 或begin
start TRANSACTION;
select balance from checking where customer_id =1000;
update checking set balance = balance - 200 where customer_id= 1000
update savings set balance = balance + 200 where customer_id = 1001
-- 提交
commit

-- 回滚
rollback