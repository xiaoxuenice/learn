#!/bin/bash
#下载地址
https://github.com/acmesh-official/acme.sh/wiki/%E8%AF%B4%E6%98%8E
acme.sh --issue -d taobao.com -d www.taobao.com --webroot /usr/share/nginx/html/taobao.com
ln -s /root/.acme.sh/taobao.com/taobao.com.cer /usr/local/nginx/conf/
ln -s /root/.acme.sh/taobao.com/taobao.com.key /usr/local/nginx/conf/
