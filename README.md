fail2ban-fastapi
----------
  
Fail2Ban operates by monitoring log files (e.g. `/var/log/auth.log`, `/var/log/apache/access.log`, etc.) for selected entries and running scripts based on them. Most commonly this is used to block selected IP addresses that may belong to hosts that are trying to breach the system's security.

**What is fail2ban-fastapi?**  
Frontend (vuejs) and backend (fastapi). FastAPI reads it's data from the socket files created by Fail2ban.

![Fail2ban-FastAPI Demo](https://i.imgur.com/7sQhGeh.gif)

## Install Fail2ban-FastAPI

Clone rep, create virtualenv and install requirements.
```bash
$ git clone git@github.com:sboily/fail2ban-fastapi.git
$ mkvirtualenv --python=/usr/bin/python3 fail2ban-fastapi
$ pip install -r requirements.txt
```

Start FastAPI backend.
```bash
$ cd api
$ python main.py
```

Start vuejs frontend.
```bash
$ npm install
$ npm run dev
```

You can also use a docker for the front
```bash
$ docker build --tag fail2ban-front
$ docker run -d -publish 8990:8990 --rm --name fail2ban-front fail2ban-front
```


FastAPI backend can be access at `http://localhost:8999`.  
Frontend access at `http://localhost:8990`.
