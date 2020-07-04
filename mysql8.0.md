------------mysql 8.0 ------------------------------------------------------------------------

docker run -dit --name mysql -p 3333:3306 -e MYSQL_ROOT_PASSWORD=Pwd@123456 library/mysql 

create user zhangsan identified with mysql_native_password by "Pwd@123456";

grant all privileges on *.* to 'zhangsan'@'%' with grant option;

alter user wangwu identified by 'aaaa';

flush privileges;
