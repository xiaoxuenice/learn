#!/bin/bash
yum -y install libffi* libffi-devel openssl-devel   zlib-devel zlib bzip2-devel expat-devel gdbm-devel tk-devel tcl-devel readline-devel sqlite-devel libX11-devel libX11 tkinter gcc gcc-c++ 2$> /dev/null
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
if [[ $? > 0 ]];then
  echo " wget failed!!!! "
  exit 0
fi
tar zxf Python-3.7.3.tgz 
cd Python-3.7.3
mkdir /usr/local/python
./configure --with-ssl --prefix=/usr/local/python
if [[ $? > 0 ]];then
  echo " wget failed!!!! "
  exit 0
fi
make && make install
if [[ $? > 0 ]];then
  echo " make failed!!! "
  exit 0
fi
ln -s /usr/local/python/bin/* /usr/local/bin/
pip install --upgrade pip
pip install ipython
if [[ $? > 0 ]];then
  echo " no pip install ipython "
  exit 0
fi
ln -s /usr/local/python/bin/ipython* /usr/local/bin/

