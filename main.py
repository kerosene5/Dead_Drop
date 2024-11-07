from scapy.all import *

def encode(message):
    if len(message) != 3:
        raise ValueError("Message must be exactly 3 characters long.")
    return [ord(char) for char in message]


def send_packets(target_ip, source_ip, source_mac, message):
    #MAC with encoded message
    custom_mac = [int(x, 16) for x in source_mac.split(':')[:-3]] + encode(message)
    arp_packet = Ether(src=':'.join(format(x, '02x') for x in custom_mac), dst="ff:ff:ff:ff:ff:ff") / ARP(op=1,pdst=target_ip,psrc=source_ip)

    #sending packets to simulate network traffic
    for _ in range(4):
        #TCP packet
        sendp(Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=f"192.168.1.{random.randint(11, 254)}",
                                                  dst=f"192.168.1.{random.randint(11, 254)}") / TCP(
            sport=random.randint(1024, 65535), dport=random.randint(1024, 65535)), verbose=False)

        #UDP packet
        sendp(IP(src=f"192.168.1.{random.randint(11, 254)}", dst=f"192.168.1.{random.randint(11, 254)}") / UDP(
            sport=random.randint(1024, 65535), dport=random.randint(1024, 65535)), verbose=False)

        #ICMP packet
        sendp(IP(src=f"192.168.1.{random.randint(11, 254)}", dst=f"192.168.1.{random.randint(11, 254)}") / ICMP(),
              verbose=False)

        time.sleep(1)

    #ARP request
    sendp(arp_packet, verbose=True)
    print(f"Sent ARP request from {':'.join(format(x, '02x') for x in custom_mac)} ({source_ip}) to {target_ip}")

    #sending packets after
    for _ in range(5):
        sendp(Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=f"192.168.1.{random.randint(11, 254)}",
                                                  dst=f"192.168.1.{random.randint(11, 254)}") / TCP(
            sport=random.randint(1024, 65535), dport=random.randint(1024, 65535)), verbose=False)
        time.sleep(1)


if __name__ == "__main__":
    target_ip = "192.168.1.1"
    source_ip = "192.168.1.100"
    source_mac = "00:11:22:33:44:55"
    message = input("Enter a 3-character message to encode: ")

    try:
        send_packets(target_ip, source_ip, source_mac, message)
    except ValueError as e:
        print(e)
