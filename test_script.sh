#!/bin/bash

# Set the network interface (change eth0 to your appropriate interface)
INTERFACE="eth0" #change according to device or VM
PCAP_FILE="5.pcap" # Give path/name of the pcap file to replay

# Run tcpreplay in the background
echo "Replaying PCAP file using tcpreplay..."
tcpreplay -p 500 --intf1=$INTERFACE $PCAP_FILE &

# Run the sniffer script
echo "Starting packet sniffer..."
python3 sniffer.py 

# Wait for all background processes to finish
wait
echo "Test script completed."
