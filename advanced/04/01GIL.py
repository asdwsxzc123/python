# 1. 描述GIL,对多线程的影响,多线程是否比单线程性能有提升
# 方案.1换解释器,执行其他语言

# 并发的一定是多进程,
# GIL全局解释权锁,影响多线程,同一时间只能使用一个线程
# python解释器,c,java都可以作为解释器,cpython解释器有GIL锁,以前没考虑多核,历史问题,不好移除
# 使用多进程,两个cpu都占满了
# 使用多线程,两个cpu只会各站50%
# 使用cpython,最好使用多进程,但官方解释器是cpython
# 使用jpython,可以考虑多线程,没有GIL锁

# 计算密集型,多进程,占用所有资源
# IO密集型,读写,多线程,或协程(在等待的时候,利用资源)