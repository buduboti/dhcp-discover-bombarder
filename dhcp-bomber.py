# https://stackoverflow.com/questions/25124500/sending-dhcp-discover-using-python-scapy

import socket
from scapy.all import *

def main():
    if len(sys.argv)<3:
        print " fewer arguments."
        sys.exit(1)
    else:
        tap_interface = sys.argv[1]
        src_mac_address = sys.argv[2]

    ethernet = Ether(dst='ff:ff:ff:ff:ff:ff',src=src_mac_address,type=0x800)
    ip = IP(src ='0.0.0.0',dst='255.255.255.255')
    udp =UDP (sport=68,dport=67)
    fam,hw = get_if_raw_hwaddr(tap_interface)
    bootp = BOOTP(chaddr = hw, ciaddr = '0.0.0.0',xid =  0x01020304,flags= 1)
    dhcp = DHCP(options=[("message-type","discover"),"end"])
    packet = ethernet / ip / udp / bootp / dhcp

    while True:
        for i in range(200):
            sendp(packet, iface = tap_interface)
        time.sleep(1)


if __name__ == '__main__':
    main()
