#!/bin/bash
cat >> /etc/init.d/rsync << EOF
#!/bin/bash
# chkconfig: 345 85 15
case \$1 in
start)
nohup /bin/sh /test/rsync-inotify.sh &
;;
reload)
ps -ef|grep inotify|awk '{print $2}'|xargs  kill
nohup /bin/sh /test/rsync-inotify.sh &
;;
stop)
ps -ef|grep inotify|awk '{print $2}'|xargs  kill
;;
restart)
ps -ef|grep inotify|awk '{print $2}'|xargs  kill
nohup /bin/sh /test/rsync-inotify.sh &
;;
*)
echo "what do you want to do?"
;;
esac
chmod +x /etc/init.d/rsync
chkconfig --add rsync
chkconfig rsync on
systemctl daemon-reload
