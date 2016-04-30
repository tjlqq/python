#!usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
retry_limit = 3
retry_count =0
accout_file = 'accouts.txt'
lock_file = 'accout_lock.txt'
while retry_count < retry_limit:
	username = raw_input('\033[32;1mUsername:\033[0m]]')
	lock_check = file(lock_file)
	for line in lock_check.readlines():
		if username in line
			sys.exit('\033[31;1mPassword:\033[0m]]' % username)
	password = raw_input('\033[32;1mPassword:\033[0m')
	f = file(accout_file,'rb')
	math_flag = False
	for line in f.readlines():
		user,passwd =line.strip('\n').split()
		if username == user and password == passwd:
			print 'Match',username
			math_flag = True
			break
	f.close()
	if math_flag == False
		print 'User unmathed!'
		retry_count +=1
	else:
		print "Welcome login OldBoy Learing system!"
else:
	print 'Your accout is locked!'
	f = file(lock_file,'rb')
	f.write(username)
	f.close