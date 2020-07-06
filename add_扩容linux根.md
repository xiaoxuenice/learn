linux根扩容

1，添加硬盘,分区，改lvm类型
fdisk /dev/sdb
n 回车 回车 回车
t   8e   w

2，格式化
mkfs.xfs /dev/sdb1
mkfs.ext4 /dev/sdb1
lsblk

3，创建pv物理卷
pvcreate /dev/sdb1

4，添加到系统所在的centos卷组
vgdisplay
vgextend centos /dev/sdb1

5，扩充根所在的逻辑卷
lvextend -l +100%FREE /dev/centos/root

6，格式化，根据类型（xfs，ext4）
xfs_growfs /dev/centos/root
resize2fs /dev/centos/root

7，查看
df -Th

