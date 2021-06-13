#!/bin/bash
二进制日志恢复数据库
reset master;	重置二进制日志
flush logs;		添加二进制日志
vim /etc/my.cnf
log_bin=mysqlbin
mysql> show master status;
| File            | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
| mysqlbin.000001 |    12061 |              |                  |                   |

#---------------------------------------------------------------------------------------
查看二进制日志内容
mysqlbinlog mysqlbin.000001 > 1.sql;vim 1.sql
#假设100的pos是删除数据的命令99以前的内容恢复和101以后的
mysqlbinlog --stop-position=99   mysqlbin.000001 |mysql -uroot -pPwd@123456
mysqlbinlog --start-position=101 mysqlbin.000001 |mysql -uroot -pPwd@123456
#报错 Can t find record in 
vim /etc/my.cnf
slave-skip-errors=1032
#报错主键冲突mysql-uroot-p加-f
