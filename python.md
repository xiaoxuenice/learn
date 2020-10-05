#############-----------------         随机验证码           ---------##############################
import random
def get_code(xx):
   a='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   b=''
   for i in range(xx):
        c=random.randint(0,61)
        b+=a[c]
   return b   

##########################-----------------         ssh 密钥认证           ---------################
#公钥打包exe程序需要添加 --key id_rsa参数  pyinstaller -F -w --key id_rsa .py
import paramiko
transport = paramiko.Transport(("192.168.116.200",22))
private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
transport.connect(username='root',pkey=private_key)
ssh=paramiko.SSHClient()
ssh._transport=transport
stdin,stdout,stderr=ssh.exec_command("ls /")
a,b=stdout.read(),stderr.read() 		 #获取执行结果   
result= a if a else b       
result.decode()        
try:
    ssh.get_transport().is_active()		#判断是否连接
    print("连接正常")
except Exception as f:
    print("断开连接")
ssh.close() 	
##########################---------------         遍历目录查找文件    ---------#############
def search(dir,fil):
    os.chdir(dir)
    it = os.listdir()
    for i in it:
        pa = os.path.join(dir,i)
        if os.path.isdir(pa):
            search(pa,fil)
            os.chdir(os.pardir)
        elif fil in pa.split("/")[-1] :
            print(pa)
###############################---------------         scp上传下载               ---------##############################
from scp import SCPClient
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
ssh.connect(hostname="192.168.116.200",port=22,username='root',pkey=private_key)
scp=SCPClient(ssh.get_transport(),socket_timeout=15.0)
scp.put('a.tar.gz',"/xue/")						#scp上传
scp.get("/xue/b.tar.gz","./")					#scp下载
#######################---------------         time获取时间              ---------##############################
time.strftime("%Y_%m_%d_%H:%M:%S",time.localtime(time.time()))
######################-----------------        json编码解码              ---------##############################
import json
js={"name":"张三","age"=26}            
json.dumps(js)          #json编码
json.loads(js)          #json解码

with open("a.js",'w') as f :             #保存为文件   
      json.dump(js,f)                    #json编码
         
with open('a.js','r') as f:              #读取文件
     js=json.load(f)                     #json解码


#####################-----------------        弹出提示对话框,判断有文件    ---------###########################
--  1   （推荐）----------------------------------------------------------------------------------------------
import easygui
easygui.msgbox("what are you doing now\n\n",'提示')
--  2   ------------------------------------------------------------------------------------------------------
import win32api,os,sys      
import win32con            
if os.path.isfile("src\\id_rsa.txt"):
    pass
else:
    win32api.MessageBox(win32con.NULL, "没有文件", "提示",win32con.MB_OK | win32con.MB_ICONINFORMATION)
    sys.exit(0)
--  3   -------------------------------------------------------------------------------------------------------
from tkinter import  messagebox
easygui.msgbox("lalala~",'提示')
easygui.ccbox("lalala~",'提示')   #True,False

--  4   -------------------------------------------------------------------------------------------------------
import tkinter
import tkinter.messagebox #弹窗库
1、提示消息框
tkinter.messagebox.showinfo('提示','人生苦短')
2、消息警告框
tkinter.messagebox.showwarning('警告','明日有大雨')
3、错误消息框
tkinter.messagebox.showerror('错误','出错了')
4、对话框
tkinter.messagebox.askokcancel('提示', '要执行此操作吗')#确定/取消，返回值true/false
tkinter.messagebox.askquestion('提示', '要执行此操作吗')#是/否，返回值yes/no
tkinter.messagebox.askyesno('提示', '要执行此操作吗')#是/否，返回值true/false
tkinter.messagebox.askretrycancel('提示', '要执行此操作吗')#重试/取消，返回值true/false
5、文件对话框
import tkinter.filedialog
a=tkinter.filedialog.asksaveasfilename()#返回文件名
print(a)
a =tkinter.filedialog.asksaveasfile()#会创建文件
print(a)
a =tkinter.filedialog.askopenfilename()#返回文件名
print(a)
a =tkinter.filedialog.askopenfile()#返回文件流对象
print(a)
a =tkinter.filedialog.askdirectory()#返回目录名
print(a)
a =tkinter.filedialog.askopenfilenames()#可以返回多个文件名
print(a)
a =tkinter.filedialog.askopenfiles()#多个文件流对象
print(a)
#################################-----------------        mysql数据库操作连接          ---------###########
create table IF NOT EXISTS ab(id int(50) primary key,name varchar(20),message varchar(100)) DEFAULT CHARSET=utf8;
mysql_ssl_rsa_setup --uid=mysql
vim /etc/my.cnf
ssl-ca=/var/lib/mysql/ca.pem
ssl-cert=/var/lib/mysql/server-cert.pem
ssl-key=/var/lib/mysql/server-key.pem
require_secure_transport = ON
bind-address = 0.0.0.0
systemctl  restart mysqld
ALTER USER 'root'@'%' require ssl;                                        #修改用户只允许ssl连接 
grant all privileges on *.* to 'root'@"%" identified by 'Pwd@123456' require ssl;    #授权时候只允许ssl
FLUSH PRIVILEGES;
show variables like '%ssl%';   #查看是否开启ssl连接
\s                              #看是否是ssl连接
alter user 'root'@'%' require x509;         #证书(pymysql不能用)
mysql -uroot -pPwd@123456 -h 192.168.116.200 --ssl-cert=/var/lib/mysql/client-cert.pem --ssl-key=/var/lib/mysql/client-key.pem --ssl-ca=/var/lib/mysql/ca.pem
###############-----------------                ssl+pymysql                 -------------------------
db = pymysql.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python",ssl={"ssl":''}})
a= db.cursor()
a.execute('insert into  user(ip,time) values("123","80:02"')) #创建写入数据
db.commit()
a.execute('select time  from {} where ip="{}";'.format(abrr,who))           #查询读取数据
print(a.fetchall())

#################################-----------------        检索文件远程发送         ---------###########

import os,easygui,paramiko
from scp import SCPClient
def SCP(Ip,file):          #上传文件
    os.chdir("C:\\Users\\Administrator\\xiaoxue")
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
    ssh.connect(hostname="192.168.116.200",port=22,username='root',pkey=private_key)
    scp=SCPClient(ssh.get_transport(),socket_timeout=15.0)
    scp.put(file, "/mnt/")
    ssh.close()
def search(dir,fil):
    os.chdir(dir)
    it = os.listdir()
    aww=[ ]
    for i in it:
        pa = os.path.join(dir,i)
        if os.path.isdir(pa):
            search(pa,fil)
            os.chdir(os.pardir)
        elif fil in pa.split("/")[-1] :
            b=repr(pa)
            SCP("192.168.116.200",pa)
search("C:\\Users\\Administrator\\Desktop","xlsx")
