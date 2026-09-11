from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP, DNS, DNSQR, Raw

packet_count = 0

print("=" * 50)
print("       CODEALPHA - BASIC NETWORK SNIFFER")
print("=" * 50)
print("Capture des paquets réseau...")
print("Appuyez sur CTRL+C pour arrêter.")


def packet_callback(packet):
    global packet_count
    packet_count += 1

    print("-" * 50)
    print(f"Packet #{packet_count}")

    if ARP in packet:
        print("Protocol       : ARP")
        print(f"Source IP      : {packet[ARP].psrc}")
        print(f"Destination IP : {packet[ARP].pdst}")
        print(f"Source MAC     : {packet[ARP].hwsrc}")
        print(f"Destination MAC: {packet[ARP].hwdst}")
        print(f"Packet length  : {len(packet)} bytes")

    elif IP in packet:
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "IP"

        print(f"Protocol       : {protocol}")
        print(f"Packet length  : {len(packet)} bytes")

        if DNS in packet:
            print("DNS            : Oui")

            if DNSQR in packet:
                query = packet[DNSQR].qname.decode(errors="replace")
                print(f"DNS Query      : {query}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            print("Payload        :", payload[:50])

    else:
        print("Protocol       : Non-IP / non-ARP")
        print(f"Packet length  : {len(packet)} bytes")

 #Demarrage de la capture
try:
    sniff(prn=packet_callback, store=False)

except KeyboardInterrupt:
    print("\n" + "=" * 50)
    print("Capture arrêtée.")
    print(f"Nombre total de paquets : {packet_count}")
    print("=" * 50)