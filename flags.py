import bs4
import requests

def getHTMLText(url):
    try:
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def cooking_soup(html_source):
    
    soup = bs4.BeautifulSoup(html_source, 'html.parser')
    
    code_tags=soup.find_all('code')
    h1_tags= soup.find_all('h1')
    p_string=""
    temp=""
    print(code_tags)
    print(h1_tags)

def main():
    url = 'https://agsyndro.me/bandit-challenges-overthewire/'
    html_source = getHTMLText(url)
    cooking_soup(html_source)


main()