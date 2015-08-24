#! /usr/bin/env python
import os
import sys
import platform
from scapy.all import *			
class discover_linux():
	def ipv6_neigh(self):
		os.system('ip -6 neigh show')
	def dhcp_discover(self):
		conf.checkIpaddr = False
		f,h = get_if_raw_hwaddr(conf.iface)
		dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=h)/DHCP(options=[("message-type","discover"),"end"])
		ans, unans = srp(dhcp_discover,multi=true)
class discover_windows():
	def ipv6_neigh(self):
		os.system('netsh interface ipv6 show neighbor')
	def dhcp_discover(self):
		conf.checkIpaddr = False
		f,h = get_if_raw_hwaddr(conf.iface)
		dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=h)/DHCP(options=[("message-type","discover"),"end"])
		ans, unans = srp(dhcp_discover,multi=true)
		
class sniff6():
	def packets(self, number, interfaz):
		a = sniff(iface = interfaz, filter = "ip6", count = int(number), prn = lambda x : x.sprintf("dir ipv6 salida --> %IPv6.src%\n" "dir ipv6 destino --> %IPv6.dst%"))

		
