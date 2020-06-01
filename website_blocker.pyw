import  time
from datetime import datetime as dt

host=r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list=["youtube.com","www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(host,"r+") as file:
            content=file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")

    else:
        with open(host,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
