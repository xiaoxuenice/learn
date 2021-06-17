#!/bin/bash
yum -y install vsftpd
cat << EOF > /etc/vsftpd/vsftpd.conf
anonymous_enable=YES
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
nopriv_user=nobody
ascii_upload_enable=YES
ascii_download_enable=YES
chroot_local_user=YES
chroot_list_enable=NO
local_root=/var/ftp
chroot_list_file=/etc/vsftpd/chroot_list
listen=NO
listen_ipv6=YES
pam_service_name=vsftpd
userlist_enable=YES
userlist_deny=NO
userlist_file=/etc/vsftpd/user_list
tcp_wrappers=YES
EOF
chmod a-w /var/ftp
mkdir /var/ftp/xiaoxue
useradd -d /var/ftp/xiaoxue xiaoxue
chmod -R 777 /var/ftp/xiaoxue
chown -R xiaoxue:xiaoxue xiaoxue
echo > /etc/vsftpd/ftpusers
echo xiaoxue > /etc/vsftpd/user_list 
systemctl restart vsftpd
firewall-cmd --zone=public --add-port=20/tcp --permanent
firewall-cmd --zone=public --add-port=21/tcp --permanent
firewall-cmd --zone=public --add-port=22/tcp --permanent
firewall-cmd --zone=public --add-port=30000-35000/tcp --permanent
firewall-cmd --zone=public --add-port=20/udp --permanent
firewall-cmd --zone=public --add-port=21/udp --permanent
firewall-cmd --zone=public --add-port=30000-35000/udp --permanent
firewall-cmd --reload
echo 请输入用户密码:
passwd xiaoxue
