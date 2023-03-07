import sys
import datetime as dt
from progressbar import ProgressBar
from intra import ic

payload = {
    "filter[kind]":"student"
}

response = ic.pages_threaded("https://api.intra.42.fr/v2/campus/48/users", params = payload)

ids = []

for pages in response:
    ids.append(pages["id"])

login_list = []
date_list = []

pbar = ProgressBar()

today = dt.date.today()

def get_blackhole_list():
    for id in pbar(ids):
        response = ic.get("https://api.intra.42.fr/v2/users/" + str(id))

        data = response.json()

        for element in data["cursus_users"]:
            if element["blackholed_at"]: # filter out the None blackholed_at element
                date = dt.date.fromisoformat(element["blackholed_at"].split('T')[0]) #date is of format 2023-03-22T08:42:00.000Z
                if (date - today).days <= 31  and (date - today).days > 0:
                    login_list.append(element["user"]["login"])
                    date_list.append(date.strftime('%d/%m/%Y'))

def create_login_file():
    get_blackhole_list()
    std_out_cpy = sys.stdout
    with open('.logins', 'w') as f:
        sys.stdout = f
        for i in range(len(login_list)):
            print(login_list[i], date_list[i]);
        sys.stdout = std_out_cpy

create_login_file()