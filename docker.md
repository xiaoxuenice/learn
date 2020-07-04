------------------------------------------------------------------安装 docker----------------------------------------------------------
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-18.03.1.ce-1.el7.centos.x86_64.rpm
yum localinstall docker-ce-18.03.1.ce-1.el7.centos.x86_64.rpm -y 
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo 

-------------------------------------------------------------------安装 jenkins---------------------------------------------------------
 wget http://mirrors.jenkins-ci.org/war/latest/jenkins.war
nohup java -jar jenkins.war --httpPort=8080 &
docker run -dit -p 80:8080 -p 50000:50000 --name jenkins -v /opt/jenkins:/var/jenkins_home --privileged=true  --restart always jenkins/jenkins

---------------------------------------------------------------------安装 gitlab------------------------------------------------------------
yum安装办法=======================
[gitlab-ce]
name=gitlab-ce
baseurl=http://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7
repo_gpgcheck=0
gpgcheck=0
enabled=1
gpgkey=https://packages.gitlab.com/gpg.key

------------------------------------------------------------------------gitlab使用docker安装办法================================================================
docker run -dit -p 2222:22 --restart=always -p 8080:8080 -p80:80 -p 8443:443 -v /home/gitlab/config:/etc/gitlab -v /home/gitlab/logs:/var/log/gitlab -v /home/gitlab/data:/var/opt/gitlab --restart always --name gitlab gitlab/gitlab-ce

vim /etc/gitlab/gitlab.rb --> external_url 'http://192.168.1.12'
git clone ssh://git@192.168.1.15:2222/python/python-project.git
上一行加ssh表示容器映射的端口是2222，非22要加ssh

------------------------------------------------------------------------docker学习记录------------------------------------------------
echo  	net.ipv4.ip_forward=1 > /usr/lib/sysctl.d/00-system.conf && systemctl restart network && systemctl restart docker 
#容器提交成为镜像的时候记住 -v 挂载的目录不会带走
#容器导出时候，再导入为镜像时候启动要加bash，且启动要进入启动nginx
docker tag nginx:latest  xuewenchang123/nginx:latest	镜像标签
docker push xuewenchang123/nginx:latest			镜像上传/下载
docker commit   [container id] [nginx:latest]		容器提交成镜像 -m"description" -a"name"
docker save -o nginx.tar nginx:latest			镜像导出 --output
docker load -i nginx.tar				镜像导入 --input
docker export [容器 id] > [nginx.tar]			容器快照导出为tar文件
cat nginx.tar | docker import - nginx:latest		容器快照/模板导入为镜像(need start container)
find / -name [container id]  vim hostconfig.json  vim config.v2.json		修改/添加容器端口
docker run --privileged -dti --name test1  centos /usr/sbin/init			ssh

-------------------------------------------------docker network -----------------------------------------
docker network create --driver  bridge networ-xue			bridge网络==默认桥接网络
docker run -dit --name test1 --network networ-xue  -p802:80 nginx	bridge网络创建容器

--------Dockerfile 1 ----(cmd/entrypoit,区别在于cmd会被run指定命令覆盖）-------
vim Dockerfile 

FROM centos:latest
MAINTAINER xiaoxue xiaoxuenice@qq.com
run  rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN yum install -y nginx openssh-server sudo net-tools
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key
RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
ADD authorized_keys /root/.ssh/authorized_keys
#同一目录下提前放置authorized_keys文件
RUN echo -e "#!/bin/sh \n/usr/sbin/sshd \n /usr/sbin/nginx -g 'daemon off;' " > /a.sh
#在配置entrypoint时候，最后一个进程要后台运行，也就是守护进程关闭，如果sshd在最后加-D
run chmod +x /a.sh
EXPOSE  80 22
#CMD ["/usr/sbin/nginx","-g","daemon off;"]
ENTRYPOINT ["/a.sh"]

docker build -t nginx:1.1 .
docker run -dit -p8080:80 -p2222:22 nginx:1.1
-----------Dockerfile 2------------------------------------------------------------
vim Dockerfile

FROM centos:latest
MAINTAINER xiaoxue xiaoxuenice@qq.com
run  rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN yum install -y nginx openssh-server sudo net-tools
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key
RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
ADD authorized_keys /root/.ssh/authorized_keys
RUN echo -e "#!/bin/sh  \nsystemctl enable nginx \nsystemctl enable sshd  " > /a.sh
run chmod +x /a.sh
run sh /a.sh
volume /usr/share/nginx/html/
user root
workdir
EXPOSE  80
#ENTRYPOINT ["/usr/sbin/nginx","-g","daemon off;"]
CMD ["init"]

docker build -t nginx:1.2 .
docker run --privileged -dit -p222:22 -p880:80 nginx:1.2 init

--------------------------------------------------------------------------------------------
