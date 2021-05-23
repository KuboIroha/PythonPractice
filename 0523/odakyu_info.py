#coding:utf-8

from bs4 import BeautifulSoup
import urllib.request as req

#htmlを取得
Ourl = "https://www.odakyu.jp/cgi-bin/user/emg/emergency_bbs.pl"
res = req.urlopen(Ourl)
print('接続中です、少々お待ちください。')

#HTMLを解析
soup = BeautifulSoup(res, "html.parser")

#小田急公式ページからclass = ttl_daiya_blueの情報を取得
info = soup.select_one(".ttl_daiya_blue").string
print( info )
