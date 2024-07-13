#! /usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
    pkt.show()
pkt=sniff(iface='br-c912b7f540a9', filter='net 10.9.0.0/24', prn=print_pkt)