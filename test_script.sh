#!/bin/bash

# Set the network interface (change eth0 to your appropriate interface)
INTERFACE="eth0"
PCAP_FILE="5.pcap"

# Run tcpreplay in the background
echo "Replaying PCAP file using tcpreplay..."
tcpreplay -p 500 --intf1=$INTERFACE $PCAP_FILE &

# Run the sniffer script
echo "Starting packet sniffer..."
python sniffer.py $PCAP_FILE

# Wait for all background processes to finish
wait
echo "Test script completed."
