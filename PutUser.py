import requests
import json
import random
from PostUser import UserID
URL="https://gorest.co.in/public-api/users/"+format(UserID)
Authorization="Bearer b783017958dc0f2d92b611e2735d1508661bc3beb332c7a10fb8eeedd7fd2112"
ContentType="application/json"
Accept="application/json"
headersitems = {'Authorization':Authorization,
                'Content-Type':ContentType,
                'Accept':Accept}
email=format(random.randint(1000,10000))+"testname@mail.com"
data='{"name":"TestName", "gender":"Male", "email":"'+email+'", "status":"Active"}'
OutputResponse=requests.put(url=URL,headers=headersitems,data=data)
temp=OutputResponse.json()
print(OutputResponse.json())
#jsondata=OutputResponse.text
#print(jsondata.__contains__('"status":"Active"'))
#print(jsondata.__contains__('"gender":"Female"'))
#print(jsondata.__contains__('"name":"Test Name"'))
#print(jsondata.__contains__('"email":"'+email+'"'))
#print(jsondata.__contains__("200"))
if temp['code']==200: print("Response code is pass")
if temp['data']['id']==format(UserID):print("UserID is pass")
if temp['data']['name']== 'TestName':
    print("Name is pass")
if temp['data']['email']==email:print("Email is pass")
if temp['data']['gender']=='Male':print("Gender is pass")
if temp['data']['status']=='Active':print("Status is pass")
print("The put operation is successful in editing the data")
