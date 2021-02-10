import requests
import json
import random

URL = "https://gorest.co.in/public-api/users"
Authorization = "Bearer b783017958dc0f2d92b611e2735d1508661bc3beb332c7a10fb8eeedd7fd2112"
ContentType = "application/json"
Accept = "application/json"
email = format(random.randint(1000, 10000)) + "testname@mail.com"
InputData = '{"name":"Test Name", "gender":"Female", "email":"' + email + '", "status":"Active"}'


class operation:

    def __init__(self, URL, Authorization, ContentType, Accept):
        self.URL = URL
        self.Authorization = Authorization
        self.ContentType = ContentType
        self.Accept = Accept
        self.UserID=None
        self.email = format(random.randint(1000, 10000)) + "testname@mail.com"
        self.newURL=None

    def PostUser(self):
        headersitems = {'Authorization': self.Authorization,
                        'Content-Type': self.ContentType,
                        'Accept': self.Accept}
        InputData = '{"name":"Test Name", "gender":"Female", "email":"' + self.email + '", "status":"Active"}'
        responsedata = requests.post(url=self.URL, headers=headersitems, data=InputData)
        postJsonResponse = responsedata.json()
        print(postJsonResponse)
        self.UserID = postJsonResponse['data']['id']
        if postJsonResponse['code'] == 201: print("Response code is pass")
        else:
            print("Post test failed")
            exit()
        if postJsonResponse['data']['name'] == 'Test Name':
            print("Name is pass")
        if postJsonResponse['data']['email'] == self.email: print("Email is pass")
        if postJsonResponse['data']['gender'] == 'Female': print("Gender is pass")
        if postJsonResponse['data']['status'] == 'Active': print("Status is pass")
        print("The post operation is successful creating an user with ID " + format(self.UserID))

    def GetUser(self):
        headersitems = {'Content-Type': self.ContentType,
                        'Accept': self.Accept}
        self.newURL = self.URL + "/" + str(self.UserID)
        responsedata = requests.get(url=self.newURL, headers=headersitems)
        getJsonResponse = responsedata.json()
        print(responsedata.json())
        if getJsonResponse['code'] == 200: print("Response code is pass")
        else:
            print("Post test is fail")
            exit()
        if getJsonResponse['data']['id'] == self.UserID: print("UserID is pass")
        if getJsonResponse['data']['name'] == 'Test Name':
            print("Name is pass")
        if getJsonResponse['data']['email'] == self.email: print("Email is pass")
        if getJsonResponse['data']['gender'] == 'Female': print("Gender is pass")
        if getJsonResponse['data']['status'] == 'Active': print("Status is pass")
        print("The get operation is successful in fetching the data")
    def PutUser(self):
        headersitems = {'Authorization': self.Authorization,
                        'Content-Type': self.ContentType,
                        'Accept': self.Accept}
        InputData = '{"name":"Edited Test Name", "gender":"Male", "email":"edited' + self.email + '", "status":"Active"}'
        #data='{"name":"TestName", "gender":"Male", "email":"'+email+'", "status":"Active"}'
        OutputResponse=requests.put(url=self.newURL,headers=headersitems,data=InputData)
        putJsonResponse=OutputResponse.json()
        print(OutputResponse.json())
        if putJsonResponse['code']==200: print("Response code is pass")
        else:
            print("Put failed")
            exit()
        if putJsonResponse['data']['id']==format(self.UserID):print("UserID is pass")
        if putJsonResponse['data']['name']== 'Edited Test Name':
            print("Name is pass")
        if putJsonResponse['data']['email']=='edited'+self.email:print("Email is pass")
        if putJsonResponse['data']['gender']=='Male':print("Gender is pass")
        if putJsonResponse['data']['status']=='Active':print("Status is pass")
        print("The put operation is successful in editing the data")

    def DeleteUser(self):
        headersitems = {'Authorization':self.Authorization,
                        'Content-Type':self.ContentType,
                        'Accept':self.Accept}
        OutputResponse=requests.delete(url=self.newURL,headers=headersitems)
        deleteJsonRespose=OutputResponse.json()
        print(OutputResponse.json())
        if deleteJsonRespose['code']==204 :print("Respose code is pass")
        else:
            print("Delete failed")
            exit()
        if deleteJsonRespose['data']== None:
            print("Data deletion is pass")
        print("The delete operation is successful in deleting the data")

RestData = operation("https://gorest.co.in/public-api/users",
                     "Bearer b783017958dc0f2d92b611e2735d1508661bc3beb332c7a10fb8eeedd7fd2112", "application/json",
                     "application/json")
RestData.PostUser()
RestData.GetUser()
RestData.PutUser()
RestData.DeleteUser()

