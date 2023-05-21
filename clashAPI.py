import requests

API="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQzZjAzY2IzLWMyOWMtNDM5MS04OWMxLThhOGY3N2UwMjMyOCIsImlhdCI6MTY4NDYxMDYyOSwic3ViIjoiZGV2ZWxvcGVyLzg5YjIwNjQ3LThjOWMtNjA4NC1iZDhjLWM2MWY1NDY3MjE2YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE3OC4xNjguMTgwLjQzIl0sInR5cGUiOiJjbGllbnQifV19.GFPc0dXMmTkydAdHVwQNb9Mh31SSYn6NoeArJq_yrT0Nk2STN_xF8FYb4FgD20x7ZD-vSLlh_OIghhA0IS-MGQ"
clanTag = "%232QCRVUC99"
RAIDS = f"https://api.clashofclans.com/v1/clans/{clanTag}/capitalraidseasons?limit=1"
MEMBERS = f"https://api.clashofclans.com/v1/clans/{clanTag}/members"

cases = [['getRaidsData', RAIDS], ['getClanMembers', MEMBERS]]

def getClashInfo(type):
    URL = ''

    for case in cases:
        if type == case[0]:
            URL = case[1]

    if URL == '':
        return None

    data = None

    response = requests.get(URL, headers={"Authorization": f"Bearer {API}"})
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    return data
