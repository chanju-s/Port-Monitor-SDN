# Port Status Monitoring Tool (SDN - Mininet + POX)

## Objective
Monitor and log switch port status changes using SDN.

## Features
- Detect port UP/DOWN events
- Log changes to file
- Generate alerts
- Performance testing (ping, iperf)

## Setup
1. Install Mininet
2. Clone POX
3. Run controller:
   ./pox.py log.level --DEBUG openflow.of_01 port_monitor

4. Run Mininet:
   sudo mn --topo single,3 --controller remote

## Testing
- Normal: ping + iperf works
- Failure: link down → traffic stops

## Output
See screenshots folder for results
