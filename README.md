Port Status Monitoring Tool (SDN - Mininet + POX)

Objective
The objective of this project is to design and implement a Software Defined Networking (SDN) based tool to monitor switch port status in real time. The system detects when a port goes up or down, logs these changes, generates alerts, and also analyzes how such failures affect network performance in terms of latency and throughput.

---

Features

* Detect port UP/DOWN events using OpenFlow
* Log port status changes to a file (port_log.txt)
* Generate alerts when a port goes down
* Display status updates in the controller terminal
* Perform performance testing using ping and iperf

---

Tools & Technologies

* POX Controller
* Mininet
* OpenFlow Protocol
* Python

---

Setup

1. Start the POX controller
   cd ~/pox
   ./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning port_monitor

2. Start Mininet in another terminal
   sudo mn --topo single,3 --controller=remote

---

Testing & Usage

1. Verify network connectivity
   pingall
   Expected: All hosts should be reachable with 0% packet loss

2. Measure latency using ping
   h1 ping -c 3 h2
   Expected: Low latency values (few milliseconds) with successful replies

3. Measure throughput using iperf
   h1 iperf -s &
   h2 iperf -c h1
   Expected: High throughput (in Gbits/sec)

4. Simulate port failure
   h1 ifconfig h1-eth0 down
   Expected:

   * Controller detects port status change
   * Alert message is displayed
   * Network connectivity is lost

5. Verify failure impact
   h1 ping -c 3 h2
   Expected: Network unreachable or packet loss

   h2 iperf -c h1
   Expected: Connection failure or zero throughput

6. Restore network
   h1 ifconfig h1-eth0 up
   pingall
   Expected: Network connectivity is restored

---

Output

Controller Output
Displays port status changes and alerts such as:
Port 1 changed state to DOWN
ALERT: Port 1 is DOWN

Log File
Run: cat port_log.txt
Expected output:
Port 1 -> DOWN
Port 1 -> UP

Screenshots
The screenshots folder contains:

* Normal operation (ping and iperf results)
* Port failure simulation
* Alert messages
* Log file output

---

Conclusion
This project demonstrates real-time monitoring of switch ports in an SDN environment. It detects failures, logs events, generates alerts, and clearly shows how network performance is affected when a port goes down.
