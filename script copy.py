import requests
from bs4 import BeautifulSoup
import re
def getHTMLText(url):
    try:
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16)^k)

    return de

def regexeverything(html):
    
    
    
    ugly_ass= re.compile('<p>+[\n|\w\s|\W]+<\/div>')
    temp = re.search(ugly_ass, html)
    #print(temp[0])
    
    get_rid_div=re.compile('<div[\s|\S|\w]+<\/div>')
    p_string=temp[0]


    p_string= re.sub(get_rid_div, '', p_string)

    

    
    

    email= re.compile('(data-cfemail\=)\"(.+?)\"')
    email_match=re.search(email,temp[0])
    

    email_protected=re.compile('\[email&#160;protected\]')

    if 'email' in p_string:
        print('found cf-email, decrypting')
        email_protected=re.compile('\[email&#160;protected\]')
        p_string= re.sub(email_protected, decodeEmail(email_match[2]), p_string)
    
   
    return p_string

def main():
    f = open('bandit_markup.txt', 'a')

    for i in range(0,35):
        url= 'https://overthewire.org/wargames/bandit/bandit' +str(i) + '.html'
        html = getHTMLText(url)
        f.write('Bandit Level ' + str(i)+'\n\n')
        f.write('<div>')
        p_string=regexeverything(html)
        f.write(p_string)
        f.write('\n')



    f.close()     

    
main()