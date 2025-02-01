from scapy.all import *
from time import time
from collections import defaultdict
import matplotlib.pyplot as plt
capture_duration = 1600  
interface = "eth0"     # Adjust to your network interface




##########################################     Q 1     #########################################################


# Global variables for metrics
packets = []
total_data = 0

# Callback to process each packet
def process_packet(packet):
    global total_data
    packets.append(packet)
    total_data += len(packet)

# Start capturing
print(f"Capturing packets for {capture_duration} seconds...")
start_time = time()
sniff(iface=interface, prn=process_packet, timeout=capture_duration)
end_time = time()

# Calculate metrics
duration = end_time - start_time
pps = len(packets) / duration
mbps = (total_data * 8 / duration) / 1e6

# Print results
print(f"Total packets captured: {len(packets)}")
print(f"Total data captured: {total_data} bytes")
print(f"Capture duration: {duration:.2f} seconds")
print(f"Packets-per-second (PPS): {pps:.2f}")
print(f"Bandwidth (Mbps): {mbps:.2f}")



# Metrics storage
total_data = 0
packet_sizes = []
all_flows = []
src_flow_count = defaultdict(int)
dst_flow_count = defaultdict(int)
flow_data = defaultdict(int)

# Analyze packets
for pkt in packets:
    # Update total data and packet size
    size = len(pkt)
    # print(f"size is {size}")
    total_data += size
    packet_sizes.append(size)

    # Extract flow details if IP layer exists
    if "IP" in pkt:
        src_ip = pkt["IP"].src
        dst_ip = pkt["IP"].dst
        src_port = pkt.sport if pkt.haslayer("TCP") or pkt.haslayer("UDP") else None
        dst_port = pkt.dport if pkt.haslayer("TCP") or pkt.haslayer("UDP") else None

        flow = f"{src_ip}:{src_port} -> {dst_ip}:{dst_port}"
        all_flows.append(flow)

        src_flow_count[src_ip] += 1
        dst_flow_count[dst_ip] += 1
        flow_data[flow] += size
# Q1 Display results
print(f"Total data transferred: {total_data} bytes")
print(f"Total packets transferred: {len(packets)}")
print(f"Minimum packet size: {min(packet_sizes)} bytes")
print(f"Maximum packet size: {max(packet_sizes)} bytes")
print(f"Average packet size: {sum(packet_sizes) / len(packet_sizes):.2f} bytes")


# Plot histogram of packet sizes
plt.hist(packet_sizes, bins=20, color='blue', edgecolor='black')
plt.title("Packet Size Distribution")
plt.xlabel("Packet Size (bytes)")
plt.ylabel("Frequency")

# Save the plot to a PNG file
plt.savefig("packet_size_distribution.png")

# Optionally, close the plot to free up memory
plt.close()

##########################################     Q 2     #########################################################
unique_flows = {}
for i in all_flows:
    if i not in unique_flows:
        unique_flows[i] = 1
    else:
        unique_flows[i] += 1

filename = 'unique_flows.txt'
with open(filename, "w") as file:
        for value in unique_flows:
            file.write(str(value) + "\n")

##########################################     Q 3     #########################################################
filename = 'source_flow_count.txt'
with open(filename, "w") as file:
        for value in src_flow_count:
            file.write(str(value) + " : " + str(src_flow_count[value]) + "\n")

filename = 'destination_flow_count.txt'
with open(filename, "w") as file:
        for value in dst_flow_count:
            file.write(str(value) + " : " + str(dst_flow_count[value]) + "\n")

max_flow = max(flow_data, key=flow_data.get)
print(f"\nSource-destination pair with most data transferred: {max_flow} ({flow_data[max_flow]} bytes)")






##########################################     PART - 2  CATCH ME IF YOU CAN     #########################################################

# Q1: Find the TCP packet containing the file name
file_name = None
tcp_checksum = None
source_ip = None

for packet in packets:
    if TCP in packet and Raw in packet:
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        if 'The name of file is = ' in payload:
            print(payload)
            file_name = payload.split('The name of file is = ')[1].split('>')[0]
            tcp_checksum = packet[TCP].chksum
            source_ip = packet[IP].src
            break

print(f"Q1a. File Name: {file_name}")
print(f"Q1b. TCP Checksum: {tcp_checksum}")
print(f"Q1c. Source IP Address: {source_ip}")

# Q2: Find the number of packets with that IP address
if source_ip:
    ip_packet_count = sum(1 for pkt in packets if IP in pkt and pkt[IP].src == source_ip)
    print(f"Q2. Number of packets with IP {source_ip}: {ip_packet_count}")

# Variables to store results
file_name = None
tcp_checksum = None
source_ip = None
target_ip_count = 0
localhost_port = None
localhost_packet_count = 0


# Step 3: Find localhost requests for phone company name
for packet in packets:
    if TCP in packet and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")
        if "Company of phone" in payload:
            print(payload)
            localhost_port = packet[TCP].sport  # Get port used by localhost
            break  # Stop after first match

# Step 4: Count packets from localhost (127.0.0.1)
localhost_packet_count = sum(1 for pkt in packets if IP in pkt and pkt[IP].src == "127.0.0.1")


print(f"3a. Port used by localhost: {localhost_port}")
print(f"3b. Number of packets from localhost: {localhost_packet_count}")


