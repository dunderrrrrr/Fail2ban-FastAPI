#!/usr/bin/env python3

import json
from .csocket import CSocket

_conf = {
    "socket": "/var/run/fail2ban/fail2ban.sock"
}

client = CSocket(_conf["socket"])

def _transform(data):
    details = {}
    for d in data:
        detail = {}
        key = d[0].lower().replace(" ", "_")
        value = d[1]
        detail[key] = value
        details.update(detail)

    return details

def parse_to_json(data):
    if isinstance(data, str) and 'pong' in data:
        return {
            'details': {
                'pong': True
            }
        }

    if isinstance(data, int):
        return {
            'details': {
                'response': data
            }
        }

    details = {}
    for d in data:
        detail = {}
        key = d[0].lower().replace(" ", "_")
        value = d[1]
        if isinstance(value, list):
            value = _transform(value)
        if isinstance(value, str) and ',' in value:
            value = value.split(", ")
        detail[key] = value
        details.update(detail)

    return {
        'details': details
    }


def send_cmd(cmd):
    c = cmd.split()
    data = client.send(c)
    if isinstance(data[1], Exception):
        data = {}
    if data:
        return parse_to_json(data[1])
