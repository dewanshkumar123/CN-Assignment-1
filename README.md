# README - CS 331: Computer Networks Assignment 1

## Overview
This repository contains the implementation and report for CS 331: Computer Networks Assignment 1. The assignment involves analyzing a PCAP file, developing a packet sniffer, replaying network traffic, and answering various questions based on captured data.

## Repository Contents
- `23_22110038_22110071.pdf`: Compiled report.
- `sniffer.py`: Packet sniffer script for analyzing network packets.
- `test_script.sh`: Bash script to test the sniffer by running `tcpreplay` and `sniffer.py` simultaneously.
- `README.md`: This file, providing an overview and execution instructions.
- `unique_flows.txt`:  unique source-destination pairs (source IP:port and destination IP:port) in the captured data.
- `source_flow_count.txt`: dictionary where the key is the IP address and the value is the total flows for that IP address as the source.
- `destination_flow_count.txt`: dictionary where the key is the IP address and the value is the total flows for that IP address as the destination.

## Execution Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/dewanshkumar123/CN-Assignment-1
cd CN-Assignment-1
```
* Add the required pcap file (5.pcap) in the cloned folder (CN-Assignment-1).
  
  PS: Link to the pcap files: https://drive.google.com/drive/folders/1n84jGddZ38fDjy9jKH3qw3J_H0SaKThu

### 2. Install Dependencies
Ensure you have Python 3.x installed. Install the required Python packages and `tcpreplay`:
```bash
sudo apt update
sudo apt install tcpreplay
sudo apt install python3-scapy python3-matplotlib
```

### 3. Run the Test Script
The `test_script.sh` script will run `tcpreplay` and `sniffer.py` simultaneously. Ensure you are using Ubuntu or a compatible Linux distribution.

```bash
bash test_script.sh
```

## Authors
- Team No. - 23
- Aryan Sahu (22110038), Dewansh Kumar(22110071)
