from scapy.all import sniff, IP, TCP, UDP, Raw

packet_count = 0

def process_packet(packet):
    global packet_count
    packet_count += 1

    print("\n==============================")
    print(f"Packet Number : {packet_count}")

    # Check IP layer
    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        # Protocol identification
        protocols = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        proto_name = protocols.get(protocol, "Other")

        print(f"Protocol       : {proto_name}")

        # Payload extraction
        if packet.haslayer(Raw):

            payload = packet[Raw].load

            print("Payload Data:")

            try:
                print(payload.decode(errors='ignore'))

            except:
                print(payload)

        # Save logs
        with open("packet_logs.txt", "a") as file:
            file.write(
                f"Packet {packet_count}: "
                f"{src_ip} -> {dst_ip} "
                f"({proto_name})\n"
            )

print("Starting Packet Sniffer...")
print("Press CTRL + C to stop.\n")

# Start sniffing packets
sniff(prn=process_packet, store=False)