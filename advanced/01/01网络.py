""" # IP """
# 1. ifconfig
# # 网卡开关
# 2. sudo ifconfig ens33 down
# 3. sudo ifconfig ens33 up

# # ipv4已经枯竭
# 4. ipv4 256*256*256*256 (0-255) , 0和255不能用

# # 网络号和主机号,前面三组是标记网络,最后一个是主机 ,网络号可以不一样的,可以划分成ABCDE几种
# # 单播,多播,广播
# d类地址用于多点广播
# 第一个字节以'1110'开始,专门保留的地址

# e类保留
# 以'1111'开头,保留用,完全没用

# 5. ipv6 


""" 进程 协程"""
# 程序在运行时叫进程


""" 端口 """
# 端口就好比一个房子的门,是出入这个房间的必经之地
# 端口相当于给应用的专属id
# 65536 2的16次方

# 一个消息
# dest ip(目的ip)
# src ip(源ip)
# dest port(目标端口)
# src port(源端口)
# content(内容)

# 1. 知名端口
  # 范围0到1023
  # 80分配给http
  # 21给ftp
  # 22给虚拟机
# 2.动态端口
#   大于1024-65536

""" socket """
1. 不同电脑上的进程如何通讯
首先要解决唯一表示一个进程
在一台电脑上通过进程号(PID)来唯一
利用ip,端口,进程

2.socket
进程间的通信

3.socket通信
# Python 可以完成
import socket
# socket.socket(AddressFamily,Type)
AddressFamily: 可以选择AF_INET IPV4

1)创建TCP SOCKET(tcp套接字对象)
s = socket.socket(socket.AF_INET,socket.SOCKET_STREAM)

2) 创建UDP socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

