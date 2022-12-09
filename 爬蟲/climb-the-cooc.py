import requests
from bs4 import BeautifulSoup
def themon(year):
    if year%4 != 0:
        return 28
    elif year%100 != 0:
        return 29
    elif year%400 != 0:
        return 28
    else:
        return 29

headers = {
    "cookie": "_ga=GA1.3.1320770536.1668952848; new-session=False; logged-in-state=redirected; _gat_tracker0=1; _gat_tracker1=1; _gat_tracker2=1; session=V2-1-c2cd4fda-60cb-416b-b581-772d9b4e678e.MjAyNzMxMQ.1670595502854.hT4cd1cRtnovixIAUvd9IJwl8-U",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36"
    }
response = requests.get(
    "https://ono.tp.edu.tw/api/courses/1378055/homework-activities?conditions=%7B%22itemsSortBy%22:%7B%22predicate%22:%22module%22,%22reverse%22:false%7D%7D&page=1&page_size=20&reloadPage=false",headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.prettify()
text = str(text)

text = text.split(',')
mon = [31,29,31,30,31,30,31,31,30,31,30,31]
for i in text:
    i = i.split(':',1)
    if i[0] == "\"deadline\"":
        i[1] = i[1].strip('\"')
        txt = i[1].split(':')
        day = txt[0].split('-')
        hour = int(day[2].split('T')[1])
        month = int(day[1])
        year = int(day[0])
        day =  int(day[2].split('T')[0])
        second = int(txt[1])
        hour += 8
        if hour >= 24:
            hour -= 24
            day += 1
            if month == 2:
                mon[1] = themon(year)
            if day >= mon[month-1]:
                day -= mon[month-1]
                month += 1
                if month >= 12:
                    month -= 12
                    year += 1
        print(str(year)+'/'+str(month)+'/'+str(day)+'-'+str(hour)+':'+str(second))
    if i[0] == "\"title\"":
        i[1] = i[1].strip( '\"' )
        print(i[1].encode('utf-8').decode('unicode_escape'))


