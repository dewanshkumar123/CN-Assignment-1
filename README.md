# README - CS 331: Computer Networks Assignment 1

## Overview
This repository contains the implementation and report for CS 331: Computer Networks Assignment 1. The assignment involves analyzing a PCAP file, developing a packet sniffer, replaying network traffic, and answering various questions based on captured data.

## Repository Contents
- `assignment1.pdf`: Compiled report.
- `sniffer.py`: Packet sniffer script for analyzing network packets.
- `test_script.sh`: Bash script to test the sniffer by running `tcpreplay` and `sniffer.py` simultaneously.
- `README.md`: This file, providing an overview and execution instructions.
- `packet_size_distribution.png`: Histogram of packet sizes.

## Execution Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/dewanshkumar123/CN-Assignment-1
cd CN-Assignment-1
```

### 2. Install Dependencies
Ensure you have Python 3.x installed. Install the required Python packages and `tcpreplay`:
```bash
sudo apt update
sudo apt install tcpreplay
pip install scapy matplotlib
```

### 3. Run the Test Script
The `test_script.sh` script will run `tcpreplay` and `sniffer.py` simultaneously. Ensure you are using Ubuntu or a compatible Linux distribution.

```bash
bash test_script.sh
```

## Dependencies
- Python 3.x
- Scapy (for packet analysis):
  ```bash
  pip install scapy
  ```
- Matplotlib (for plotting):
  ```bash
  pip install matplotlib
  ```
- `tcpreplay` (for packet replaying, install via package manager):
  ```bash
  sudo apt install tcpreplay  # Linux
  ```

## Test Script (`test_script.sh`)
The `test_script.sh` script is a bash script that runs `tcpreplay` and `sniffer.py` simultaneously.


Make sure to give execute permission to the script before running it:
```bash
chmod +x test_script.sh
```

## Authors
- Team No. - 23
- Aryan Sahu (22110038), Dewansh Kumar(22110071)
