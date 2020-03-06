import os
import time

data_path = os.path.dirname(os.path.realpath(__file__)) + "/data/"

def create_status():
    print("Running fail2ban-client status")
    filename = "jails.txt"
    data = os.popen('fail2ban-client status').read()
    file = open(data_path + filename, 'w') 
    file.write(data)
    print("Wrote to {}{}\n".format(data_path, filename))
    
def get_jails():
    f = open(data_path + "jails.txt", "r")
    l = []
    for line in f:
        l.append(line)
    jail_names = l[2].split(':')[1].strip()
    jails = jail_names.split(', ')
    return(jails)

def create_jail(jail):
    print("Running fail2ban-client status {}".format(jail))
    data = os.popen('fail2ban-client status {}'.format(jail)).read()
    print("JAILDATA: ", data)
    file = open(data_path + "jail_" + jail + ".txt", 'w') 
    file.write(data)
    print("wrote to {}jail_{}.txt\n".format(data_path, jail))

def ban_ip(ip, jail):
    print("Banning {} in jail {}".format(ip, jail))
    data = os.popen('fail2ban-client set {} banip {}'.format(jail, ip)).read()
    print(data)
    time.sleep(1.5) # takes time to refresh jail (got diff in vue frontend)
    create_jail(jail)

def unban_ip(ip, jail):
    print("Unbanning {} in jail {}".format(ip, jail))
    data = os.popen('fail2ban-client set {} unbanip {}'.format(jail, ip)).read()
    print(data)
    time.sleep(1.5) # takes time to refresh jail (got diff in vue frontend)
    create_jail(jail)

def generate_files():
    status = create_status()
    jails = get_jails()
    for jail in jails:
        create_jail(jail)

