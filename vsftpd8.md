#!/bin/bash
yum -y install vsftpd
sed -i '4 s/shells/nologin/g' /etc/pam.d/vsftpd
cat << EOF > /etc/vsftpd/vsftpd.conf
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
anon_upload_enable=YES
anon_mkdir_write_enable=YES
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
chown_uploads=YES
xferlog_std_format=YES
async_abor_enable=YES
ascii_upload_enable=YES
ascii_download_enable=YES
ftpd_banner=Welcome to blah FTP service.
chroot_local_user=YES
listen=NO
listen_ipv6=YES
pam_service_name=vsftpd
userlist_enable=YES
allow_writeable_chroot=YES
listen_address=0.0.0.0
userlist_enable=YES
userlist_deny=NO
EOF
chmod a-w /var/ftp
mkdir /var/ftp/xiaoxue
useradd -d /var/ftp/xiaoxue xiaoxue
chmod -R 755 /var/ftp/xiaoxue
chown -R xiaoxue:xiaoxue /var/ftp/xiaoxue
echo > /etc/vsftpd/ftpusers
echo xiaoxue > /etc/vsftpd/user_list 
systemctl restart vsftpd
firewall-cmd --zone=public --add-port=21/tcp --permanent
firewall-cmd --reload
echo 请输入用户密码:
passwd xiaoxue
