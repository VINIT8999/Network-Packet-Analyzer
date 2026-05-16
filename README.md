# Network Packet Analyzer 🔐

A simple Python-based Network Packet Analyzer built using Scapy.  
This tool captures and analyzes live network packets, displays packet details, and logs captured traffic for educational and ethical cybersecurity learning purposes.

---

# 📌 Features

- Capture live network packets
- Display Source & Destination IP addresses
- Detect protocols (TCP / UDP / ICMP)
- Extract and display payload data
- Save packet logs automatically
- Real-time packet monitoring

---

# 🛠 Technologies Used

- Python 3
- Scapy Library

---

# 📂 Project Structure

```bash
├── packet_sniffer.py
├── packet_logs.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## Step 1️⃣ Install Python

Download and install Python:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

## Step 2️⃣ Install Scapy

Open terminal or command prompt and run:

```bash
pip install scapy
```

---

## Step 3️⃣ Create Project File

Create a file named:

```bash
packet_sniffer.py
```

Paste the Python code into the file.

---

## Step 4️⃣ Run the Project

Run the script using:

```bash
python packet_sniffer.py
```

You will see:

```bash
Starting Packet Sniffer...
Press CTRL + C to stop.
```

---

# ▶️ How It Works

1. The script starts sniffing live network packets.
2. Captured packets are processed one by one.
3. Source and destination IP addresses are displayed.
4. Protocol type is identified (TCP/UDP/ICMP).
5. Payload data is extracted if available.
6. Packet logs are stored automatically in a text file.

---

# 📷 Sample Output

```bash
==============================
Packet Number : 1
Source IP      : 192.168.1.10
Destination IP : 142.250.183.78
Protocol       : TCP

Payload Data:
GET / HTTP/1.1
```

---

# 📝 Packet Logs

Captured packets are automatically saved in:

```bash
packet_logs.txt
```

Example:

```bash
Packet 1: 192.168.1.10 -> 142.250.183.78 (TCP)
```

---

# 📚 Learning Outcomes

This project helped in understanding:

- Networking Fundamentals
- Packet Analysis
- TCP/IP Protocols
- Real-Time Traffic Monitoring
- Python for Cyber Security

---

# 📌 Conclusion

The Network Packet Analyzer project provided practical experience in network monitoring and packet analysis using Python and Scapy. It helped in understanding how data travels across a network, how different protocols work, and how packet information can be captured and analyzed in real time.

This project improved knowledge of:
- Networking concepts
- TCP/IP protocols
- Packet sniffing techniques
- Python scripting for cybersecurity

Overall, this project was a great hands-on learning experience in the field of Cyber Security and Network Analysis.

---

# ⚠️ Disclaimer

This project is developed strictly for educational and ethical purposes only.  
Do not use this tool on networks without proper authorization.

---

# 🚀 Future Improvements

- GUI Interface
- Packet Filtering
- Save Packets as PCAP
- Suspicious Traffic Detection
- Real-Time Dashboard

---


Vinit Raparti  
Cyber Security Enthusiast 🔐
