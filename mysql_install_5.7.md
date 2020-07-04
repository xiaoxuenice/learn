sudo rpm -ivh https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
sudo yum -y install mysql-community-server
systemctl start mysqld
mysqltmppwd=`cat /var/log/mysqld.log | grep -i 'temporary password'`
mysql  -uroot -p"${mysqltmppwd: -12}"  --connect-expired-password  -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'Pwd@123456';"
mysql  -uroot -p"Pwd@123456"  --connect-expired-password  -e "grant all privileges on *.* to 'root' @'%' identified by 'Pwd@123456';"
echo "###########################-----done----##################################"

