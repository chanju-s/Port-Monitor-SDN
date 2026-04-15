from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

port_status = {}

def _handle_PortStatus(event):
    port_no = event.port
    reason = event.ofp.reason

    if reason == of.OFPPR_ADD:
        state = "ADDED"
    elif reason == of.OFPPR_DELETE:
        state = "DELETED"
    elif reason == of.OFPPR_MODIFY:
        if event.ofp.desc.state & of.OFPPS_LINK_DOWN:
            state = "DOWN"
        else:
            state = "UP"
    else:
        state = "UNKNOWN"

    port_status[port_no] = state

    log.info(f"Port {port_no} changed state to {state}")

    with open("port_log.txt", "a") as f:
        f.write(f"Port {port_no} → {state}\n")

    if state == "DOWN":
        log.warning(f"⚠️ ALERT: Port {port_no} is DOWN!")

def launch():
    log.info("Port Monitoring Tool Started")
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)
