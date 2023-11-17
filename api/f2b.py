import os
import time

from client.client import send_cmd


def get_jails():
    print("Get jails list")
    jails = send_cmd("status")
    return(jails['details']['jail_list'])

def get_jail(jail):
    print(f"Get jail {jail}")
    jails = send_cmd(f"status {jail}")
    return(jails)

def ban_ip(ip, jail):
    print(f"Banning {ip} in jail {jail}")
    return send_cmd(f'set {jail} banip {ip}')

def unban_ip(ip, jail):
    print(f"Unbanning {ip} in jail {jail}")
    return send_cmd(f'set {jail} unbanip {ip}')
