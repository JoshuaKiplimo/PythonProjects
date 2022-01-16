import requests 
import json 


payload = { 
    "picture_url": "https://i.groupme.com/480x325.jpg.9139e83272ac73c3b8e2770dd3"
   }
j=requests.post("https://i.groupme.com/9139e83272ac73c3b8e2770dd3",params=payload)
print(j)