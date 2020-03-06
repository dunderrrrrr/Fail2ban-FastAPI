fail2ban-fastapi
----------
  
Fail2Ban operates by monitoring log files (e.g. `/var/log/auth.log`, `/var/log/apache/access.log`, etc.) for selected entries and running scripts based on them. Most commonly this is used to block selected IP addresses that may belong to hosts that are trying to breach the system's security.

**What is fail2ban-fastapi?**  
Frontend (vuejs) and backend (fastapi). FastAPI reads it's data from files created by this script (since Fail2ban's internal sqlite database is not human readable). The script user must have permissions to execute `$ fail2ban-client` to generate this data.
```
.
├── api
│   └── data/
│       └── jails.txt
│       └── jail_<jailname>.txt
│       └── jail_<jailname>.txt
```

![Fail2ban-FastAPI Demo](https://i.imgur.com/7sQhGeh.gif)

## Installation

### Fail2ban Setup

First of all, the script needs to be able to run `fail2ban-client` command. This is usually done with root permissions. To solve this, you need to create a new (non-root) user and run fail2ban as this user. 

```bash
$ sudo apt install fail2ban
$ sudo adduser fail2ban
```

Set `User` to "fail2ban" in the [Service] section in `/lib/systemd/system/fail2ban.service`
```text
...
[Service]
User=fail2ban
...
```

Change permissions of `/var/run/fail2ban`.
```bash
$ sudo chown -R fail2ban:root /var/run/fail2ban
```

Verify permissions with `sudo ls -la /var/run/fail2ban/`. Make sure fail2ban user can read and write to this location.

Depending on your jails, the fail2ban user needs to be able read your logfiles (ex. `/var/log/auth.log`). An example configuration can be found in [jail.local.sample](./jail.local.sample).  
  
So change permisions of your logfiles.
```bash
$ sudo chown fail2ban:root /var/log/auth.log
```

Now you should be all set to reload `systemctl daemon` and restart fail2ban.

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl restart fail2ban.service
```

Check status of fail2ban.service to make sure we're all set and you have no errors.

## Install Fail2ban-FastAPI

Clone rep, create virtualenv and install requirements.
```bash
$ git clone git@github.com:dunderrrrrr/fail2ban-fastapi.git
$ mkvirtualenv --python=/usr/bin/python3 fail2ban-fastapi
$ pip install -r requirements.txt
```

Before starting FastAPI backend we'll need to generate some Fail2ban data. This will only be necessary once when setting up Fail2ban-FastAPI for the first time on.
```bash
$ cd api/
$ python first_init.py
```

Start FastAPI backend.
```bash
$ python main.py
```

Start vuejs frontend.
```bash
$ npm install
$ npm run dev
```

FastAPI backend can be access at `http://localhost:8000`.  
Frontend access at `http://localhost:8080`.