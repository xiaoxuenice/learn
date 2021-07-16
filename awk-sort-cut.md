#!/bin/bash
######## 	grep
grep -r aaa 递归查找包含aaa
grep -rl aaa 递归查找包含aaa的文件
-i  忽略大小写
-e  正则
-o  只显示匹配的部分
-l 列出符合内容的文件
-n 显示列号
-v 翻转查找
-c 统计行数

[] 里面用 -o -a 外面用 and or
if判断
If  [
-z     字符串为空 
-n 		字符串不为空
-e 		有目录和文件夹
-f		文件
-d		目录
-a 		and
-o 		or
]
############      awk
awk 'NR==2{print}' a.txt |awk '{print $3}'
awk 'NR==2''{print $NF}' a.txt
打印第二行的第三个，和打印第二行的最后一个。

###########       sort
sort -t= -k2n a.txt
以=分隔符截取，按照第二列排序。

sed

sed   '/aaa/,+5 s/2020/9999/g' a.txt
更改匹配到aaa的内容以下5行的2020改为9999

