import requests
import json
import random
URL ="https://gorest.co.in/public-api/users"
Authorization="Bearer b783017958dc0f2d92b611e2735d1508661bc3beb332c7a10fb8eeedd7fd2112"
ContentType="application/json"
Accept="application/json"
headersitems = {'Authorization':Authorization,
        'Content-Type':ContentType,
        'Accept':Accept}
email=format(random.randint(1000,10000))+"testname@mail.com"
InputData='{"name":"Test Name", "gender":"Female", "email":"'+email+'", "status":"Active"}'
responsedata=requests.post(url=URL,headers=headersitems,data=InputData)
temp = responsedata.json()
print(temp)
#jsondata=responsedata.text
#print(jsondata.__contains__('"status":"Active"'))
#print(jsondata.__contains__('"gender":"Female"'))
#print(jsondata.__contains__('"name":"Test Name"'))
#print(jsondata.__contains__('"email":"'+email+'"'))
#print(jsondata.__contains__("201"))
UserID=temp['data']['id']
if temp['code']==201: print("Response code is pass")
if temp['data']['name']== 'Test Name':
    print("Name is pass")
if temp['data']['email']==email:print("Email is pass")
if temp['data']['gender']=='Female':print("Gender is pass")
if temp['data']['status']=='Active':print("Status is pass")
print("The post operation is successful creating an user with ID"+ format(UserID))