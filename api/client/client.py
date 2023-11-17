#!/usr/bin/env python3

from csocket import CSocket

_conf = {
    "socket": "/var/run/fail2ban/socket"
}

timeout = 1
c = "show status"

client = CSocket(_conf["socket"], timeout=timeout)
ret = client.send(c)
