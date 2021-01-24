import requests





data={"name":"",
"category":"Misc",
"description":"",
"value":"1",
"state":"visible",
"type":"standard"}
cookies = {'CSRF-Token':'6bf8c1cdf9a88b3106a2d973246467a741bfbcb7cc41609863ed401aaef8ee2c',
'Cookie':'session=f3efe9db-ea4d-4c9c-b716-69dc51498002.ckQgoSDFg-r6YW3xMUiKNTbBNk4', 
'Content-Type':'application/json',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}

for i in range(21,34):
    with open('./files/bandit{}.txt'.format(str(i))) as f:
        temp=f.read()
        print(temp)
        data['description'] = temp
        data['name'] = 'Bandit{}'.format(str(i))
        if i <=15:
            data['value']= 3
        if i >15 and i < 21:
            data['value']= 4
        if i >=21 and i <= 25:
            data['value']= 5
        if i >25  and i <=30:
            data['value'] = 6
        if i >31 and i <=33:
            data['value'] = 7
        r= requests.post(
               'http://134.122.11.63/api/v1/challenges', headers=cookies, json=data)
        print(r.text)


#
#print(data)
