import requests
from PostUser import UserID,email
URL="https://gorest.co.in/public-api/users/"+format(UserID)
Authorization="Bearer b783017958dc0f2d92b611e2735d1508661bc3beb332c7a10fb8eeedd7fd2112"
ContentType="application/json"
Accept="application/json"
headersitems = {'Content-Type':ContentType,
                'Accept':Accept}
responsedata=requests.get(url=URL,headers=headersitems)
temp=responsedata.json()
print(responsedata.headers)
print(responsedata.json())
#jsondata=responsedata.text
#print(jsondata.__contains__('"id":"'+str(UserID)+'"'))
#print(jsondata.__contains__('"status":"Active"'))
#print(jsondata.__contains__('"gender":"Female"'))
#print(jsondata.__contains__('"name":"Test Name"'))
#print(jsondata.__contains__('"email":"'+email+'"'))
#print(jsondata.__contains__("200"))
if temp['code']==200: print("Response code is pass")
if temp['data']['id']==format(UserID):print("UserID is pass")
if temp['data']['name']== 'Test Name':
    print("Name is pass")
if temp['data']['email']==email:print("Email is pass")
if temp['data']['gender']=='Female':print("Gender is pass")
if temp['data']['status']=='Active':print("Status is pass")
print("The get operation is successful in fetching the data")
print(responsedata.headers['Content-Type'])
head=responsedata.headers['Content-Type'].split(";")
print(responsedata.headers['Date'])
if ContentType in head: print("Header ContentType is a Pass")
else:print("Header ContentType is a fail")