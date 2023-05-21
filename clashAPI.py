import requests

KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQ1MmVmZjRkLWZjNmUtNGE5Yy05OGZkLThlOWZkYjA5OWI5YiIsImlhdCI6MTY4NDY4NTYxNiwic3ViIjoiZGV2ZWxvcGVyLzg5YjIwNjQ3LThjOWMtNjA4NC1iZDhjLWM2MWY1NDY3MjE2YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE3OC4xNjguMTg0LjI1NCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.1-vazXcM4DVgS6S_lKyPs7eGU5I3VyArCTh7aqBO2Bkwy5qaKi6cJ0jKcUGIkBglv16hCPqvmUTgnSpL2B0O0A"
clanTag = "%232QCRVUC99"
RAIDS = f"https://api.clashofclans.com/v1/clans/{clanTag}/capitalraidseasons?limit=1"
MEMBERS = f"https://api.clashofclans.com/v1/clans/{clanTag}/members"
CW = f"https://api.clashofclans.com/v1/clans/{clanTag}/currentwar"

cases = [['getRaidsData', RAIDS], ['getClanMembers', MEMBERS], ['getCurrentWar', CW]]

def getClashInfo(type):
    URL = ''

    for case in cases:
        if type == case[0]:
            URL = case[1]

    if URL == '':
        return None

    data = None

    response = requests.get(URL, headers={"Authorization": f"Bearer {KEY}"})
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    return data