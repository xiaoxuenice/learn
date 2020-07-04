--permanent 								# 永久开放
--timeout=60 								# 时间开放
--zone=									# 设置的域noaddthen默认
--add --remove --query						        # 添加与取消与查询

firewall-cmd --list-all							# 查看默认区域配置

firewall-cmd --get-default-zone						# 查看默认的域

firewall-cmd --get-active-zones   					# 查看全部的域

firewall-cmd --set-default-zone=drop					# 设置默认区域

firewall-cmd --zone=public --add-interface=ens38 --permanent  		# 根据域绑定网卡

firewall-cmd --zone=public --list-ports  				# 查看开放的端口

firewall-cmd --zone=public --list-rich-rules 	        		# 查看添加的规则

firewall-cmd --zone=public --add-protocol=icmp  --permanent		#开放协议 

firewall-cmd --add-service=ssh    --permanent				#开放服务

firewall-cmd --zone=public --add-port=80/tcp --permanent    		# 开放单个端口

firewall-cmd --zone=public --add-port=8388-8389/tcp --permanent    	# 开放端口范围

firewall-cmd --permanent  --add-rich-rule='rule family="ipv4" source address="192.168.1.1" port protocol="tcp" port="22" accept'       					# 根据ip开放端口

firewall-cmd --permanent  --add-rich-rule='rule family="ipv4" source address="192.168.1.1" port protocol="tcp" port="22" reject'	  				# 根据ip拒绝端口

firewall-cmd --permanent  --add-rich-rule="rule family="ipv4" source address="192.168.1.1"  accept"									# 根据ip接受所有端口

firewall-cmd --add-masquerade --permanent				#启用区域伪装		
firewall-cmd --permanent  --add-forward-port=port=8080:proto=tcp:toaddr=172.16.0.2:toport=80
										#端口转发

firewall-cmd --permanent  --add-rich-rule='rule family=ipv4 source address=192.168.1.0/24 masquerade'					#启用富规则区域伪装
firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=192.168.1.0/24 forward-port port=22  protocol=tcp to-addr=192.168.116.65 to-port=22'     #192访问的网段地址端口转发为172.17.0.2:8080

启用应急模式阻断所有网络连接，以防出现紧急状况			firewall-cmd --panic-on
禁用应急模式							firewall-cmd --panic-off
查询应急模式							firewall-cmd --query-panic

