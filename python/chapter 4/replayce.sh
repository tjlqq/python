#!/bin/bash
#func:replace file
#author:jt
#time:2015.11.17
#qq:2220781951
t=$(date +%Y%m%d%H%M%S)
sdir=/root/replace
#echo ${sdir##*/}#get file name
for filename in 'ls $sdir'
do
path=`find /home/weinfo/tomcat/webapp/ -name $filename`
echo ${path%/*}#获取目录
newpath=${path%/*}
mv $path $path_$t.bak#备份
cp $sdir/$filename $newpath 
echo $filename
done

for shname in `find . -type f -name "*.sh"`
do 
          name=`echo "$shname" | awk -F/ '{print $2}'`          
          echo $name
done