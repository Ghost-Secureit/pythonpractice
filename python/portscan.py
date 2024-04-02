import socket
import re
import random
from socketserver import TCPServer
from telnetlib import IP
from scapy.all import *


def port_scan(host, port, fragsize, results):
    try:
        #create socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set timeout for connection
        s.settimeout(1)
        #connect host and port 
        s.connect((host,port))
        #send data to prompt response 
        s.send(b'GET / HTTP/1.1\r\n\r\n')
        #receive banner 
        banner = s.recv(1024).decode('utf-8')
        
        # Craft IP packet with fragment option
        ip = IP(dst=host, flags="MF")
        # Craft TCP packet
        syn = TCPConnectPipe(dport=port, flags="S")
        # Combine fragments
        pkt = ip/syn
        # Send the packet with specified fragment size
        frag_pkt = fragment(pkt, fragsize=fragsize)

        for fragment in frag_pkt:
            response = sr1(fragment, timeout=1, verbose=False)
            if response and response.haslayer(socket.TCP_SYNCNT):
                banner = response.sprintf("%TCP.load%")
       
        #try to extrat version info from banner
        version = re.findall(r'Server: (.+)', banner)
        if version:
             result = f"[+] Port {port} is open. Banner: {banner.strip()}, Version: {version[0]}"
        else: 
            result =f"[+] Port {port} is open. Banner: {banner.strip()}"
        results.append(result)
    except Exception as e:
        pass
    finally:
        s.close()

def scan_host(host, ports, fragsize):
    print(f"Scanning host: {host}")
    results = []
    for port in ports:
        port_scan(host,port,fragsize,results)

    for result in results:
        print(result)

def main():
    host = input("enter target to scan: ")
    ports = [21,22,53,80,443,3306]
    fragsize = int(input("enter frag size: "))
    scan_host(host,ports,fragsize)

if __name__ == "__main__":
    main()