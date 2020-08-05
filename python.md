#########################################-----------------         随机验证码           ---------##############################
import random
def get_code(xx):
   a='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   b=''
   for i in range(xx):
        c=random.randint(0,61)
        b+=a[c]
   return b   
   
#########################################-----------------         ssh                  ---------##############################

import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #允许不在/root/.ssh/known_hosts连接
ssh.connect(hostname="192.168.116.200",port=22,username='root',password='xiaoxue')
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

#######################################-----------------         ssh 密钥认证           ---------##############################
#公钥打包exe程序需要添加 --key id_rsa参数  pyinstaller -F -w --key id_rsa .py
import paramiko
transport = paramiko.Transport(("192.168.116.200",22))
private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
transport.connect(username='root',pkey=private_key)
ssh=paramiko.SSHClient()
ssh._transport=transport
stdin,stdout,stderr=ssh.exec_command("ls /")


######################################---------------         scp上传下载               ---------##############################
from scp import SCPClient
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
ssh.connect(hostname="192.168.116.200",port=22,username='root',pkey=private_key)
scp=SCPClient(ssh.get_transport(),socket_timeout=15.0)
scp.put('a.tar.gz',"/xue/")						#scp上传
scp.get("/xue/b.tar.gz","./")					#scp下载


######################################---------------         time获取时间              ---------##############################

time.strftime("%Y_%m_%d_%H:%M:%S",time.localtime(time.time()))

#####################################-----------------        json编码解码              ---------##############################

import json
js={"name":"张三","age"=26}            
json.dumps(js)          #json编码
json.loads(js)          #json解码

with open("a.js",'w') as f :             #保存为文件   
      json.dump(js,f)                    #json编码
         
with open('a.js','r') as f:              #读取文件
     js=json.load(f)                     #json解码


#####################################-----------------        弹出提示对话框,判断有文件    ---------###########################
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
#####################################-----------------        mysql数据库操作连接               ---------######################
def insert(ip,time,arg):
  mydb = mysql.connector.connect(
    host="192.168.116.200",
    user="root",
    passwd="Pwd@123456",
    database="python"
  )
  a = mydb.cursor()
  try:
    a.execute("insert into shell(ip,time,message) values(%s,%s,%s);",(ip,time,arg))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def select():
  mydb = mysql.connector.connect(
    host="192.168.116.200",
    user="root",
    passwd="Pwd@123456",
    database="python"
  )
  a = mydb.cursor()
  a.execute("select concat(ip,time, message)  from shell  ;")
  return (a.fetchall())
#############################################################################################################################


















