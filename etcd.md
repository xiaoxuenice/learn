#!/bin/bash
etcd安装：（2379 端口处理客户端的请求，2380 端口用于集群各成员间的通信）
curl -L https://github.com/etcd-io/etcd/releases/download/v3.4.0/etcd-v3.4.0-linux-amd64.tar.gz -o etcd-v3.4.0-linux-amd64.tar.gz
tar xzvf etcd-v3.4.0-linux-amd64.tar.gz
cd etcd-v3.4.0-linux-amd64
cp etcd* /usr/local/bin/
etcdctl put testkey （设置键值）
etcdctl get testkey （获取键值）

