# 필요한 라이브러리
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# 대상 사이트의 URL
url = "https://comic.naver.com/webtoon/weekday"

# csv 파일에 입력하기
filename = "네이버_웹툰_인기_순위.csv"
f = open("../data/" + filename, "a", encoding="utf-8-sig")
writer = csv.writer(f)
# 시간을 적기
t = [["시간", str(datetime.now())]]
writer.writerow(t)
# 컬럼 속성명 주기
columns_name = ["순위", "웹툰명"]
writer.writerow(columns_name)

# 웹 서머에 요청
res = requests.get(url)
res.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(res.text, "lxml")
# asideBoxRank 라는 class 의 ol을 가져온다
cartoonBox = soup.find('ol', attrs={"class":"asideBoxRank"})
# 그 안의 a 태그를 모두 가져온다
cartoons = cartoonBox.find_all('a')

i = 1
# 제목을 가져와서 출력하기
for cartoon in cartoons:
    title = cartoon.get('title')
    print(f"{str(i)}위: {title}")
    writer.writerow([str(i), title])
    i += 1

writer.writerow("")
f.close()