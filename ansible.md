yum install python-pip && pip install ansible && touch /etc/ansible/hosts && touch /etc/ansible.cfg
---------------------------------------
cat /etc/ansible/hosts
[test]
192.168.1.10
---------------------------------------
ansible -k密码，-i主机路径，-m执行模块名字，-u远程用户，-a命令参数
---------------------------------------
ansible test -m ping
ansible test -m shell -a "chdir=/xue/ sed -i 's/l/b/g' a.txt " 		#切换到/xue执行sed
ansible test -m shell -a "removes=/xue/b.txt  ls"					#如果b.txt存在执行ls
ansible test -m copy -a 'src=/hello dest=/xue/hello backup=yes'		#copy文件，有源文件自动备份
ansible test -m copy -a 'content="okay" dest=/xue/test.txt mode=666'#写入文件
ansible test -m fetch -a 'src=/data/hello dest=/data'				#copy远到近
ansible test -m file -a 'path=/data/app state=directory'			#创建目录
ansible test -m file -a 'path=/data/bbb.jpg src=aaa.jpg state=link'	#创建链接文件
ansible test -m file -a 'path=/data/a state=absent'					#删除文件
ansible test -m file -a 'path=/xue/c.txt state=touch'				#创建文件
ansible test -m cron -a 'name="bp" hour=*/1 job="/usr/bin/cp a.txt a.bak &> /dev/null"'		#任务计划
ansible test -m cron -a 'name="bp" hour=*/1 job="/usr/bin/cp a.txt a.bak &> /dev/null "state=absent' #取消任务计划
ansible test -m yum -a 'name=httpd state=present' 					#latest 安装,absent 卸载
ansible test -m service -a 'name=nginx state=started enabled=true'	#enabled开机启动started，stopped，restarted，reloaded
ansible test -m script -a "/tmp/kel.sh >/tmp/kelkel.log"            #执行脚本
---------------------------yaml------------
    # ansible-playbook a.yml --syntax-check    #检查yaml文件的语法是否正确
    # ansible-playbook a.yml --list-task       #检查tasks任务
    # ansible-playbook a.yml --list-hosts      #检查生效的主机
    # ansible-playbook a.yml --start-at-task='Copy Nginx.conf'     #指定从某个task开始运行
---------------------------yaml------------
---
- hosts: test
  remote_user: root
  vars:
    - var1: var111
  tasks:
   - name:  start_firewalld
     tags:                                          # 只执行这个标签上面的任务
      - only                                        # ansible-playbook test.yml --tags="only" 
     shell: systemctl start firewalld
     ignore_errors: True                            #忽略错误，强制返回成功
     notify:										#调用han1
       - han1
     when: 											#判断当下面符合执行任务
       - ansible_distribution == "CentOS"
       - ansible_distribution_major_version == "7"
       
   - name:  stop_firewalld
     service: name=firewalld state=stopped
     notify:                                        #调用han2
       - han2
   - name: diedai                                   #迭代item里面的内容
     copy: src=/xue/{{ item }} dest=/xue/xue/
     with_items:
       - a 
       - b
   - name: diedai2
     copy: src=/xue/{{ item.name }} dest=/xue/xue/{{ item.arg }}
     with_items:
       - { name='a',arg="test1"}
       - { name='b',arg="test2"}
  handlers:            #搭配notify被调用
    - name: han1
      shell:  echo {{var1}} >> /xue/a.txt && sed -i 's/1/2/g' /xue/a.txt
    - name: han2
      copy: content="{{ansible_all_ipv4_addresses}}" dest="/xue/ip.txt"
---------------------------templates------------
vim /etc/ansible/hosts 
[test]
192.168.116.200 http_port=80 server_name=www.jd.com  #在主机定义变量
-----------
cat test.conf
{{ http_port }} {{ server_name }}  #本地文件里面定义变量名
-----------
- hosts: test
  remote_user: root
  tasks:
    - name: cp
      template: src=/xue/test.conf dest=/xue/nginx.conf #3.拷贝文件的时候自动带入值
-----------
cat nginx.conf
80  www.jd.com
---------------------------yaml------------
