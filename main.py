from bs4 import BeautifulSoup
import urllib.request

urlpage = 'https://github.com/pyppeteer/pyppeteer/stargazers'
page = urllib.request.urlopen(urlpage)
parsedPage = BeautifulSoup(page, 'html.parser')
arr = []


def retreiveStarPage():
    for tag in parsedPage.find_all('a', attrs={"data-hovercard-type": "user", "class": ""}):
        arr.append(tag['href'])
    return arr


while (1):
    try:
        retreiveStarPage()
        next = parsedPage.find('a', attrs={
            "rel": "nofollow", "class": "btn btn-outline BtnGroup-item"}, string="Next")['href']
        print(next)
        page = urllib.request.urlopen(next)
        parsedPage = BeautifulSoup(page, 'html.parser')
    except:
        break

print('Res', arr)
