# Port Status Monitoring Tool (SDN - Mininet + POX)

## Objective

The objective of this project is to design and implement a Software Defined Networking (SDN) based tool to monitor switch port status in real time. The system detects port state changes (UP/DOWN), logs these events, generates alerts for failures, and analyzes the impact of port failures on network performance using latency and throughput measurements.

---

## Features

* Detect port UP/DOWN events using OpenFlow
* Log port status changes to a file (`port_log.txt`)
* Generate real-time alerts for port failures
* Display status updates in controller terminal
* Perform performance analysis using ping (latency) and iperf (throughput)

---

## Tools & Technologies

* POX Controller (SDN controller)
* Mininet (network emulator)
* OpenFlow Protocol
* Python (for controller logic)

---

## Setup

### 1. Start POX Controller

```bash
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning port_monitor
```

### 2. Start Mininet

```bash
sudo mn --topo single,3 --controller=remote
```

---

## Testing & Usage

### 1. Verify Network Connectivity

```bash
pingall
```

**Expected Output:**

* All hosts reachable (0% packet loss)

---

### 2. Measure Latency (Ping)

```bash
h1 ping -c 3 h2
```

**Expected Output:**

* Low latency (few milliseconds)
* Successful replies

---

### 3. Measure Throughput (iperf)

```bash
h1 iperf -s &
h2 iperf -c h1
```

**Expected Output:**

* High bandwidth (in Gbits/sec)
* Successful TCP connection

---

### 4. Simulate Port Failure

```bash
h1 ifconfig h1-eth0 down
```

**Expected Behavior:**

* Controller detects port status change
* Alert message displayed
* Connectivity lost

---

### 5. Verify Failure Impact

#### Ping Test

```bash
h1 ping -c 3 h2
```

**Expected Output:**

* Network unreachable / packet loss

#### Throughput Test

```bash
h2 iperf -c h1
```

**Expected Output:**

* Connection failure / zero throughput

---

### 6. Restore Network

```bash
h1 ifconfig h1-eth0 up
pingall
```

**Expected Output:**

* Connectivity restored

---

## Output

### 1. Controller Output

* Displays port status changes
* Shows alerts such as:

  ```
  Port 1 changed state to DOWN
  ALERT: Port 1 is DOWN!
  ```

---

### 2. Log File

```bash
cat port_log.txt
```

**Expected Output:**

```
Port 1 -> DOWN
Port 1 -> UP
```

---

### 3. Screenshots

* Normal operation (ping + iperf)
* Port failure simulation
* Alert messages
* Log file output

(All screenshots are included in the `screenshots/` folder)

---

## Conclusion

This project successfully demonstrates real-time monitoring of switch ports in an SDN environment. It detects failures, logs events, generates alerts, and clearly shows the impact of port failures on network performance.

---
