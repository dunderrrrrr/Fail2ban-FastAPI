import re

data_path = 'data/'
data_format = '.txt'
files = {
    "jails": "{}jails{}".format(data_path, data_format)
}

def get_jaildata(jail, jail_path):
    data = {}
    f = open(jail_path, "r")
    l = []
    for line in f:
        l.append(line)
    data['fail_current'] = re.findall(r'\d+', l[2])[0]
    data['fail_total'] = re.findall(r'\d+', l[3])[0]
    data['bans_current'] = re.findall(r'\d+', l[6])[0]
    data['bans_total'] = re.findall(r'\d+', l[7])[0]
    data['log_file'] = l[4].split(':')[1].strip()
    data['bans_iplist'] = l[8].split(':')[1].strip().split(' ')
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
    f = open(files['jails'], "r")
    l = []
    for line in f:
        l.append(line)
    jailnums = re.findall(r'\d+', l[1])[0]
    jail_names = l[2].split(':')[1].strip()
    obj_jails['jail'] = {} 
    for jail in jail_names.split(', '):
        jail_path = data_path + 'jail_' + jail + data_format
        jail_data = get_jaildata(jail, jail_path)
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
    f = open(files['jails'], "r")
    l = []
    for line in f:
        l.append(line)   
    jail_names = l[2].split(':')[1].strip().split(', ')
    if jail in jail_names:
        obj_jail = {
            jail: {}
        }
        jail_path = data_path + 'jail_' + jail + data_format
        jail_data = get_jaildata(jail, jail_path)
        obj_jail[jail] = {
            "fails_current": jail_data['fail_current'],
            "fails_total": jail_data['fail_total'],
            "bans_current": jail_data['bans_current'],
            "bans_total": jail_data['bans_total'],
            "log_file": jail_data['log_file'],
            "bans_iplist": jail_data['bans_iplist']
        }
        return(obj_jail)
    else:
        return {"error": 404, "msg": "Jail name '{}' not found".format(jail)}