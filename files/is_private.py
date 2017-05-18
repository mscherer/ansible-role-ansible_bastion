#!/usr/bin/python
# quick script to be used with openssh for RFC1918
# ip, to avoid going in tor
import ipaddr
import sys
import socket

target = sys.argv[1]

# .onion cannot be resolved by DNS and shouldn't
if target.endswith('.onion'):
    sys.exit(0)

try:
    ad = ipaddr.IPAddress(target)
except ValueError:
    ad = ipaddr.IPAddress(socket.gethostbyname(target))

if ad.is_private or ad.is_loopback or ad.is_link_local:
    sys.exit(1)
sys.exit(0)
