1.列表：只读的，不可修改的
a.index(2)
a.index(2,a.index(2)+1)
2.元祖：不可修改
列表和元祖可以互相转换。
list(a)
tuple(a)
3.开发替换小程序
#！__*__ coding:utf-8 __*__
import sys,os

if len(sys.argv) <= 1:
	print "usage:./file_replace.py old_text new_text filename"
old_text,new_text = sys.argv[1],sys.argv[2]

file_name = sys.argv[3]

f = file(file_name,'rb')
new_file = file('.%s.bak' % file_name,'rb')
for line in f.xreadlines():
	print line.replace(old_text,new_text)
f.close()
new_file.close()


if '--bak' in sys.argv
	os.rename(file_name,'.%s.bak2' %file_name)
	os.rename('.%s.bak' %file_name,file_name)
else:
	os.rename('.%s.bak' %file_name,file_name)
	输入：: '|' ‘|’：’
	diff new_file old_file.bak
# if '--bak' in sys.argv:
	# bak_file = '%s.bak' % file_name
# else:
	# bak_file = None
# if bak_file is not None
	# os.
字典
 
