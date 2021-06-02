#!/bin/bash
cat >> /etc/init.d/frp << EOF
#!/bin/bash
#/ chkconfig: 345 85 15
#要执行的命令 
nohup /etc/frp/frpc  -c /etc/frp/frpc.ini &
EOF
chmod +x /etc/init.d/frp
chkconfig --add frp
chkconfig frp on
