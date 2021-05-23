import requests

res = requests.request('get', 'https://www.odakyu.jp/cgi-bin/user/emg/emergency_bbs.pl')
print(res.text)