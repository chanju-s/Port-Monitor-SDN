# Port Status Monitoring Tool (SDN - Mininet + POX)

Objective

The objective of this project is to design and implement a Software Defined Networking (SDN) based tool to monitor switch port status in real time. The system detects port state changes (UP/DOWN), logs these events, generates alerts for failures, and analyzes the impact of port failures on network performance using latency and throughput measurements.

Features
Detect port UP/DOWN events using OpenFlow
Log port status changes to a file (port_log.txt)
Generate real-time alerts for port failures
Display status updates in the controller terminal
Perform performance analysis using ping (latency) and iperf (throughput)

Tools & Technologies
POX Controller
Mininet
OpenFlow Protocol
Python

Setup
Start the POX controller
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning port_monitor
Start Mininet in another terminal
sudo mn --topo single,3 --controller=remote
Testing & Usage

Verify network connectivity
pingall

Expected result: All hosts should be reachable with 0% packet loss.

Measure latency using ping
h1 ping -c 3 h2

Expected result: Low latency values (in milliseconds) with successful replies.

Measure throughput using iperf
h1 iperf -s &
h2 iperf -c h1

Expected result: High bandwidth (in Gbits/sec) indicating proper network performance.

Simulate port failure
h1 ifconfig h1-eth0 down

Expected behavior:

Controller detects port status change
Alert message is displayed
Network connectivity is disrupted

Verify failure impact

Ping test:
h1 ping -c 3 h2
Expected: Network unreachable or packet loss

Throughput test:
h2 iperf -c h1
Expected: Connection failure or zero throughput

Restore network
h1 ifconfig h1-eth0 up
pingall

Expected result: Connectivity is restored and network functions normally again.

Output
Controller Output
Displays port status changes and alert messages such as:
Port 1 changed state to DOWN
ALERT: Port 1 is DOWN

Log File
Run: cat port_log.txt

Expected output:
Port 1 -> DOWN
Port 1 -> UP

Screenshots
The screenshots folder includes:
Normal operation (ping and iperf results)
Port failure simulation
Alert messages in controller
Log file output

Conclusion
This project demonstrates real-time monitoring of switch ports in an SDN environment. It successfully detects failures, logs events, generates alerts, and shows the impact of port failures on network performance. 

---
