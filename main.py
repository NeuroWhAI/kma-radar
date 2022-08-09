import os
import urllib.request
from datetime import datetime, timedelta
import time
from pathlib import Path

if not os.path.exists("img"):
    os.mkdir("img")

tm = datetime(2022, 8, 9, 20, 35) # 시작할 시간. (5분 단위로 입력.)
while True:
    tm_str = tm.strftime("%Y%m%d%H%M")
    file_path = Path(f"img/{tm_str}.png")
    if file_path.is_file():
        break
    url = f"https://www.weather.go.kr/w/cgi-bin/rdr_new/nph-rdr_sat_lgt_img_v3?tm={tm_str}&sat=ir1&rdr=lng&map=HC&size=640&zoom_level=0&zoom_x=0000000&zoom_y=0000000&fog=0"
    print(tm_str)
    try:
        urllib.request.urlretrieve(url, file_path)
    except Exception as e:
        print("Error: ", e)
        time.sleep(5)
        continue
    time.sleep(1)
    tm = tm - timedelta(minutes=5)

print("Complete.")
