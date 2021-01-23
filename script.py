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
    soup =  BeautifulSoup(html, 'html.parser')
    
    p_tags=soup.find_all('p')
    p_string=""
    temp=""
    
    print(p_string)
    if len(p_tags) >1:
        for i in p_tags[0:-1]:
            temp=str(i)
            while 'strong' in temp:
                i.strong.unwrap()
                temp=str(i)
            
            p_string+=temp + '\n'
    else:
        p_string=re.sub('\<.+?\>', '', str(p_tags[0]))

    email= re.compile('(data-cfemail\=)\"(.+?)\"')
    email_match=re.search(email,p_string)
        
    p_string=re.sub('\<.+?\>', '', p_string)

    email_protected=re.compile('\[email\s+protected\]')


    if 'email' in p_string:
        print('found cf-email, decrypting')
        email_protected=re.compile('\[email\s+protected\]')
        p_string= re.sub(email_protected, decodeEmail(email_match[2]), p_string)
    
   
    li = soup.find_all('li')
    prop=""
    li_re= re.compile('(<li>)(\w.+)(<\/li>)')
    for string in li:
        
        s1=str(string)
        
        if re.match(li_re, s1):
            g=re.match(li_re,s1)
            prop+=(g.group(2)) + ', '    
    
    
    goal=""
    if len(p_tags) >1:
        listtostr=' '.join(i.string.rstrip() for i in p_tags[-1])
        getridnew=re.compile('\n')
        goal = re.sub(getridnew, '', listtostr)
    print('-----------------' +'bandit' + '-----------------')
    print()
    print(p_string)
    print(prop)
    print("------------- command you need to solve this level -------------")
    print(goal)
    return p_string, prop, goal

def main():
    f = open('bandit.txt', 'a')

    for i in range(0,35):
        url= 'https://overthewire.org/wargames/bandit/bandit' +str(i) + '.html'
        html = getHTMLText(url)
        print('bandit ' + str(i))
        p_string, prop, goal=regexeverything(html)
        f.write('-----------------Bandit Level {}-----------------'.format(str(i)) + '\n')
        f.write(p_string + '\n')
        f.write(prop)
        f.write('\n')
        f.write('========****** command you need to solve this level ******========' + '\n')
        f.write(goal + '\n\n\n')
    f.close()     

    
main()