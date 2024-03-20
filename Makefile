profile: /etc/profile
	source $^
	source ~/.source
start:
	lsnrctl start
	sleep 3
	netstat -ntlp
stop:
	lsnrctl stop
	sleep 3
	netstat -ntlp
status:
	lsnrctl status
