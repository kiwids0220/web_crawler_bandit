import requests


f = open('flag')
log=open('flag_log', 'a')
data={"content":"CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9",
"data":"",
"type":"static",
"challenge":-1}

cookies = {'CSRF-Token':'f773d9297bbba1c5d9843eb4a8a46cea296e1d9175b73b7e196b1dc7245efb7e',
'Cookie':'session=758420b4-664b-4049-b5f1-98940921e29a.20LmIhBK5rBJLKT8_LXGJSvWq1o', 
'Content-Type':'application/json',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}

url='http://134.122.11.63/api/v1/flags'

for i in range(55,88):
    temp = f.readline().rstrip()
    data['content']= temp
    data['challenge'] = i
    log.write(str(data) + '\n')
    #r= requests.post(url, headers=cookies, json=data)
    #log.write(str(r.text))

f.close()
log.close()
