import requests
import json
from PostUser import UserID
URL="https://gorest.co.in/public-api/users/"+format(UserID)
Authorization="Bearer b783017958dc0f2d92b611e2735d1508661bc3beb332c7a10fb8eeedd7fd2112"
ContentType="application/json"
Accept="application/json"
headersitems = {'Authorization':Authorization,
                'Content-Type':ContentType,
                'Accept':Accept}
OutputResponse=requests.delete(url=URL,headers=headersitems)
temp=OutputResponse.json()
print(OutputResponse.json())
#jsondata=OutputResponse.text
#print(jsondata.__contains__("204"))
if temp['code']==204 :print("Respose code is pass")
if temp['data']== None:
    print("Data deletion is pass")
print("The delete operation is successful in deleting the data")
