from client.connect import send_cmd

def get_jaildata(jail):
    data = {}
    f = send_cmd(f"status {jail}")
    detail = f['details']
    data['fail_current'] = detail['filter']['currently_failed']
    data['fail_total'] = detail['filter']['total_failed']
    data['bans_current'] = detail['actions']['currently_banned']
    data['bans_total'] = detail['actions']['total_banned']
    data['log_file'] = detail['filter']['file_list']
    data['bans_iplist'] = detail['actions']['banned_ip_list']
    return(data)

def summary(obj_jails, jailnums):
    tot_bans_current = []
    tot_bans_total = []
    for k,v in obj_jails['jail'].items():
        tot_bans_current.append(int(v['bans_current']))
        tot_bans_total.append(int(v['bans_total']))   
    obj_jails['sum'] = {}
    obj_jails['sum']['jail_nums'] = int(jailnums)
    obj_jails['sum']['total_bans_current'] = sum(tot_bans_current)
    obj_jails['sum']['total_bans_total'] = sum(tot_bans_total)   
    return(obj_jails)

def main():
    obj_jails = {}
    f = send_cmd("status")
    jailnums = f['details']['number_of_jail']
    jail_names = f['details']['jail_list']
    obj_jails['jail'] = {} 
    for jail in jail_names:
        jail_data = get_jaildata(jail)
        obj_jails['jail'][jail] = {
            "jail_name": jail,
            "fails_current": jail_data['fail_current'],
            "fails_total": jail_data['fail_total'],
            "bans_current": jail_data['bans_current'],
            "bans_total": jail_data['bans_total'],
            "log_file": jail_data['log_file'],
            "bans_iplist": jail_data['bans_iplist']
        }
    data = summary(obj_jails, jailnums)
    return(data)

def get_jail(jail):
    f = send_cmd("status")
    jail_names = f['details']['jail_list']
    if jail in jail_names:
        obj_jail = {
            jail: {}
        }
        f = send_cmd(f"status {jail}")
        detail = f['details']
        obj_jail[jail] = {
            "fails_current": detail['filter']['currently_failed'],
            "fails_total": detail['filter']['total_failed'],
            "bans_current": detail['actions']['currently_banned'],
            "bans_total": detail['actions']['total_banned'],
            "log_file": detail['filter']['file_list'],
            "bans_iplist": detail['actions']['banned_ip_list']
        }
        return(obj_jail)
    else:
        return {"error": 404, "msg": "Jail name '{}' not found".format(jail)}

def ban_ip(ip, jail):
    print(f"Banning {ip} in jail {jail}")
    return send_cmd(f'set {jail} banip {ip}')

def unban_ip(ip, jail):
    print(f"Unbanning {ip} in jail {jail}")
    return send_cmd(f'set {jail} unbanip {ip}')
