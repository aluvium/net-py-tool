from scapy.all import * 
def packet_callback(packet):
    print(packet.show())
    return 0

sniff(prn=packet_callback, count=1)
