# README - CS 331: Computer Networks Assignment 1

## Overview
This repository contains the implementation and report for CS 331: Computer Networks Assignment 1. The assignment involves analyzing a PCAP file, developing a packet sniffer, replaying network traffic, and answering various questions based on captured data.

## Repository Contents
- `assignment1.tex`: LaTeX source file for the report.
- `assignment1.pdf`: Compiled report.
- `sniffer.py`: Packet sniffer script for analyzing network packets.
- `test_script.py`: Script to test the sniffer.
- `README.md`: This file, providing an overview and execution instructions.
- `packet_size_distribution.png`: Histogram of packet sizes.
- `same_vm_performance.png`: Performance analysis when replaying on the same VM.
- `different_vm_performance.png`: Performance analysis when replaying between different VMs.
- `canarabank_analysis.png`: HTTP request analysis for Canara Bank.
- `performance_metrics.png`: Screenshot of browser performance metrics.

## Execution Instructions

### 1. Running the Packet Sniffer
Ensure you have Python installed. Run the sniffer using:
```bash
python sniffer.py 5.pcap
```

### 2. Replaying the PCAP File
To replay the traffic using `tcpreplay`:
```bash
tcpreplay --intf1=eth0 5.pcap
```
Replace `eth0` with the appropriate network interface.

### 3. Running the Test Script
To validate the sniffer's functionality:
```bash
python test_script.py
```

### 4. Compiling the Report
To generate the PDF report from LaTeX:
```bash
pdflatex assignment1.tex
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
  brew install tcpreplay      # macOS
  ```

## Authors
- Team ID: 5
- Roll Numbers: 23210122, 23210023

## License
This project is for educational purposes only.
