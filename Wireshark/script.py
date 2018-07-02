import pyshark
import sys

cap = pyshark.FileCapture(sys.argv[1])

ips = []

for pkt in cap:
    try:
        if (pkt.ip.src not in ips):
            ips.append(pkt.ip.src)
    except:
        pass

print(ips)
