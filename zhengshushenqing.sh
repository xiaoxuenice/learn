#!/bin/bash
echo "======================================="
echo "更新yuming.txt里面的证书STARTING····"
echo "======================================="
echo "正在改变配置文件停止强制添加端口"
echo "======================================="
grep -rl rewrite /usr/local/nginx/dh/ |xargs sed -i  's/rewrite/#rewrite/g'
nginx -t ;if [ $? -eq 0 ] ;then nginx -s reload;fi
for i in `cat yuming.txt`;do
   /root/.acme.sh/acme.sh --issue --force -d ${i}  -d www.${i}  --webroot /usr/share/nginx/html/${i}
   if [ $? -eq 0 ];then
   \cp  /root/.acme.sh/${i}/${i}.key /usr/local/nginx/conf/${i}.key
   \cp  /root/.acme.sh/${i}/${i}.cer /usr/local/nginx/conf/${i}.crt
     echo -e  "\033[32m ${i}  更新成功 \033[0m"
   else
      echo -e "\033[31m ${i}  域名证书更新未成功 \033[0m"
   fi
done
echo "==========================="
echo "正在恢复配置文件强制添加端口"
echo "==========================="
grep -rl rewrite /usr/local/nginx/dh/ |xargs sed -i  's/#rewrite/rewrite/g'
echo "==========================="
echo "重新加载 nginx "
echo "==========================="
nginx -t ;if [ $? -eq 0 ] ;then nginx -s reload;fi
echo 'OK'
echo "==========================="
