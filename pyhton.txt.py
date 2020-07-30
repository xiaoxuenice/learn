#########################################-----------------         ssh               ---------##############

import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #允许不在/root/.ssh/known_hosts连接
ssh.connect(hostname="192.168.116.200",port=22,username='root',password='xiaoxue')
stdin,stdout,stderr=ssh.exec_command("ls /")


	
a,b=stdout.read(),stderr.read() 		 #获取结果   
result= a if a else b       
result.decode()        


try:
    ssh.get_transport().is_active()		#判断是否连接
    print("连接正常")
except Exception as f:
    print("断开连接")
ssh.close() 	

#######################################-----------------         ssh 密钥认证      ---------###############

import paramiko
transport = paramiko.Transport(("192.168.116.200",22))
private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
transport.connect(username='root',pkey=private_key)
ssh=paramiko.SSHClient()
ssh._transport=transport
stdin,stdout,stderr=ssh.exec_command("ls /")

a,b=stdout.read(),stderr.read()   #获取结果 
result= a if a else b       
result.decode()  

try:
    ssh.get_transport().is_active()		#判断是否连接
    print("连接正常") 
except Exception as f:
    print("断开连接")  
ssh.close() 


######################################-----------------         time时间获取      ---------###############

time.strftime("%Y_%m_%d_%H:%M:%S",time.localtime(time.time()))

#####################################-----------------         json  编码解码     ---------###############

import json
js={"name":"张三","age"=26}            

with open("a.js",'w+') as f :            #保存为文件   
      json.dump(js,f)                    #json编码
      
      
with open('a.js','r') as f:              #读取文件
     js=json.load(f)                     #json解码





















