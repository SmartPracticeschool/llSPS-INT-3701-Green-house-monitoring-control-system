import time
import sys
import ibmiotf.application
import ibmiotf.device
import requests

contactnumber="6361853126"

organization ="yh8ahx"
deviceType ="Rasperypi"
deviceId ="1234"
authMethod ="use-token-auth"
authToken ="12345678"

url="www.fast2sms.com/dev/bulk"

def myCommandCallback(cmd):
    i=(cmd.data["T"])
    j=(cmd.data["H"])
    k=(cmd.data["M"])

    if(i<=40):
        print("Temparature is",i,"(optimal)")
    else:
        print("Temparature exeeded 40. Text alert message sent to mobile")

    querystring = {"authorization":"vRciF0IXYqEGQM4oCKAdazZS1VLNgrs9lfOB8D65xUwnPm2t3HlcLsQ8PAyST47Xj6fDwKnrqC9FEida"}

    headers = {
        'cache control':"no-cache"
        }
    response = requests.request("GET",url,headers=headers,params=querystring)

    print(response.text)
    print("Text message has been about Temparature reaching above threshold value. \nexiting python code")
    exit(0)


    if(j<=90):
        print("Humidity is",j,"(optimal)")
    else:
        print("Humidity exeeded 90. Text alert message sent to mobile")

    querystring = {"authorization":"vRciF0IXYqEGQM4oCKAdazZS1VLNgrs9lfOB8D65xUwnPm2t3HlcLsQ8PAyST47Xj6fDwKnrqC9FEida"}

    headers = {
        'cache control':"no-cache"
        }
    response = requests.request("GET",url,headers=headers,params=querystring)

    print(response.text)
    print("Text message has been about Humidity reaching above threshold value. \nexiting python code")
    exit(0)


    if(k<=25):
        print("moisture",k,"(optimal)")
    else:
        print("moisture exeeded 25. Text alert message sent to mobile")

    querystring = {"authorization":"vRciF0IXYqEGQM4oCKAdazZS1VLNgrs9lfOB8D65xUwnPm2t3HlcLsQ8PAyST47Xj6fDwKnrqC9FEida"}

    headers = {
        'cache control':"no-cache"
        }
    response = requests.request("GET",url,headers=headers,params=querystring)

    print(response.text)
    print("Text message has been about Humidity reaching above threshold value. \nexiting python code")
    exit(0)

    
        
            
