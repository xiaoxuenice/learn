nginx禁止ip登陆，添加一个server就ok了
    server {
        listen 80 default;
        server_name _;
        return 403;

    }

