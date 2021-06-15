#!/bin/bash
server {
	listen 80;
        listen 443 ssl;
        listen 888 ssl;
        server_name www.aaaa.net aaaa.net wap.aaaa.net m.aaaa.net agent.aaaa.net;
#limit_conn  one  100;
#limit_conn perserver 1000;
#limit_req   zone=allips  burst=5  nodelay;
        if ($scheme = http ) {
        return 301 https://$host$request_uri;
        }
        if ($server_port = 443 ){
        rewrite ^/(.*) https://$host:888$1 break;
        }

        
	ssl_certificate_key STAR.aaaa.net.key;
        ssl_certificate STAR.aaaa.net.crt;
        ssl_protocols             TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers               ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM;
        ssl_prefer_server_ciphers on;
	
	charset		utf-8;
	if ($scheme = http ) {
		return 301 https://$host$request_uri;
        }  
 
        location / {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header REMOTE-HOST $remote_addr;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_pass  http://www_server;
        }
        location ~ .*\.(jpg|jpeg|gif|png|swf|css|js|txt|htc|ico)?$ {
            proxy_cache cache_one;
            proxy_cache_key $host$uri$is_args$args;
            add_header Cache "$upstream_cache_status";
            proxy_cache_valid 200 304 30m;
            proxy_cache_valid 404 500 502 503 504 3s;
            proxy_cache_valid any 1h;
            expires 2h;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header REMOTE-HOST $remote_addr;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_pass  http://www_server;
        }
    }
