#!/usr/bin/python3

import requests
import time
import jsontestIP

# define the URL we want to use
POSTURL = "http://validate.jsontest.com/"
TIMEURL = "http://date.jsontest.com"

def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces

    resp1 = requests.get(TIMEURL)

    nowtime = resp1.json()
    print(nowtime)

    myIP = str(jsontestIP.main())
    with open("./myservers.txt","r") as serverlist:
        servers = serverlist.read()
        mydata = {}
        mydata['time']= nowtime
        mydata['ip']= myIP
        mydata['mysvrs']= servers
        print(type(mydata))
        print(mydata)
        jsondata= {}
        jsondata["json"]= str(mydata)
        #print(servers)
    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=jsondata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()

