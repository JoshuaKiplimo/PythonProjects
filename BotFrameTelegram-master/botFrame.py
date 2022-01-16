import json #to parse Json modules into python to extrACT THE DATA 
import time
import urllib
import requests #making web requests and interacting with telegram AP
import emoji
import datetime


Classes_string = '''
{
  "SCHEDULE":[      
   {
   "08": "Enter information that you want to send to user at this given time",
   "09": "Enter information that you want to send to user at this given time",
   "10": "Enter information that you want to send to user at this given time",
   "11": "Enter information that you want to send to user at this given time",
   "12": "Enter information that you want to send to user at this given time",
   "13": "Enter information that you want to send to user at this given time",
   "14": "Enter information that you want to send to user at this given time",
   "15": "Enter information that you want to send to user at this given time",
   "16": "Enter information that you want to send to user at this given time",
   "17": "Enter information that you want to send to user at this given time",
   "18": "Enter information that you want to send to user at this given time",   
   "19": "Enter information that you want to send to user at this given time",
   "20": "Enter information that you want to send to user at this given time",
   "21": "Enter information that you want to send to user at this given time",
   "22": "Enter information that you want to send to user at this given time",
   "23": "Enter information that you want to send to user at this given time",
   "0": "Enter information that you want to send to user at this given time",
   "1": "Enter information that you want to send to user at this given time",
   "2": "Enter information that you want to send to user at this given time",
   "4": "Enter information that you want to send to user at this given time",
   "5": "Enter information that you want to send to user at this given time",
   "6": "Enter information that you want to send to user at this given time",
   "7": "Enter information that you want to send to user at this given time",
  
  ]
}
    '''
data = json.loads(Classes_string)
extract = data["SCHEDULE"][0]

"""
To extract the day of the week and hour
"""

def findtime(): 
    t = datetime.datetime.now()
    h = datetime.time()
    tdelta= datetime.timedelta(hours=4)
    
    Weekday = t.strftime("%A")    
    difference = (t - tdelta)
    hournow = difference.hour
    return(Weekday, hournow)
    
weekday, hournow = findtime()

"""
  Weather api and a function to extract data from the API 
  
"""


URL2 = "https://api.openweathermap.org/data/2.5/weather?q=Orangeburg,USA&units=imperial&APPID=30cdffc331ee3350cc4a2a433f4f195d"
json_data = requests.get(URL2).json()



def weather_data():
  
  max_temp, min_temp = json_data["main"]["temp_max"], json_data["main"]["temp_min"]  
  description, current_conditions = json_data["weather"][0]["description"], json_data["weather"][0]["main"]
  data = ("Todays maximum temperature{} will be {} degrees Farenheight, while the minimum teperature{} will be {} degrees farenheight. Current overhead conditions: {}. ".format(emoji.emojize(":thermometer:"), max_temp,emoji.emojize(":thermometer:"), min_temp, description,))

  return(data)
#function to send the weather data above
def send_weather(text, chat):
  url = URL +"sendMessage?text={}&chat_id={}".format("{}Here is today's general weather conditions...{}{}".format(emoji.emojize(":sun_behind_cloud:"),emoji.emojize(":cloud_with_rain:"),emoji.emojize(":sun_behind_small_cloud:")), chat)
  get_url(url)
  time.sleep(2)
  url = URL +"sendMessage?text={}&chat_id={}".format(weather_data(), chat)
  get_url(url)
  time.sleep(2.5)
  url = URL +"sendMessage?text={}&chat_id={}".format("Have a great day!{}".format(emoji.emojize(":cowboy_hat_face:")), chat)
  get_url(url)
  time.sleep(2)
  url = URL +"sendMessage?text={}&chat_id={}".format("Goodbye{}.To find more information send /start".format(emoji.emojize(":waving_hand:")), chat)
  get_url(url)
  

TOKEN = "#enter token here"
URL = "https://api.telegram.org/bot{}/" .format(TOKEN)



"""
Function to download URL content as string 
"""
#code citation for  line 106 - 149
#   Title: PYTHON-TEEGRAM TUTORIAL 
#   Author: Gareth, DWYER
#   Code version: 3.0
#   Availability:  https://github.com/sixhobbits/python-telegram-tutorial/blob/master/part1/echobot.py

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8");
    #print(content)
    return content;
    

def get_json_from_url(url): 
	content = get_url(url)
	js =json.loads(content)
	return(js)
"""
FUNCTION TO GET UPDATES9(new messages sent to the bot)
"""
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(update):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
        print(update_ids)
        return max(update_ids)   


    
    
    

"""
to get the most recent message and chat id sent to the user. 
"""
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1# get_last_update_id(update)
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)
    print(chat_id)
    get_last_update_id(update)

"""
Function to send the first message
Intended to be the function that starts everything off
"""
def send_message1(chat):
    print("will send hello there!")

    url = URL + "sendMessage?text={}&chat_id={}".format("Hello there!{}".format(emoji.emojize(":waving_hand:")), chat)
    get_url(url)

    
    handle_updates() #After the welcome message is sent, the next part will be activated 
  
"""
Function to send the first keyboard from which the user will pick an option for example class

"""
#function to build the first keyboard that will be sent to the user 
text, chat = get_last_chat_id_and_text(get_updates())
items =[enter data to send to keyboard]

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": False}
    return json.dumps(reply_markup) #keyboard is sent as json
    
def handle_updates():        
    keyboard = build_keyboard(items);
    send_message2(chat, keyboard)
"""
def handle_subsequent_updates1():    
    
    keyboard = build_keyboard2(week_days);
    send_message_3(message, chat, keyboard)
"""

#Function to send the second keyboard to the user 
def build_keyboard2(week_days):
    keyboard1 = [[day] for day in week_days]
    reply_markup1 = {"keyboard":keyboard1, "one_time_keyboard": True}
    return json.dumps(reply_markup1)
    

def send_message2(chat, reply_markup):
    text, chat = get_last_chat_id_and_text(get_updates())
    
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown&reply_markup={}".format("My developer specialized me to help you with the items below{}. Please choose one".format(emoji.emojize(":backhand_index_pointing_down:")), chat, reply_markup)
    get_url(url)  
    
    time.sleep(7)
    text, chat = get_last_chat_id_and_text(get_updates())
    print(text)

    handle_subsequent_updates()

"""
def send_message_3(message, chat, reply_markup1=True):
    
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown&reply_markup={}".format(message[1], chat,reply_markup1)
    #message 1 is "Which day of the week do you want to know about?"
    
    get_url(url)
    time.sleep(8)
    send_message(text, chat)
"""


#WE NOW HAVE THE LATEST INPUT FROM THE USER, WE NOW ACTIVATE THE NEXT PART

def handle_subsequent_updates():
    text, chat = get_last_chat_id_and_text(get_updates())

    
    if text =="{}Classes{}".format(emoji.emojize(":pen:"),emoji.emojize(":spiral_notepad:")):
        url = URL +"sendMessage?text={}&chat_id={}".format("Let me fetch data for your current time", chat)
        get_url(url)
        time.sleep(2)
        url = URL + "sendMessage?text={}&chat_id={}".format("{}".format(extract["{}".format(hournow)]), chat)
        get_url(url)
        time.sleep(2)
        url = URL +"sendMessage?text={}&chat_id={}".format("Let me fetch you data for the next hour ", chat)
        get_url(url) 
        time.sleep(2) 
        url = URL + "sendMessage?text={}&chat_id={}".format("{}".format(extract["{}".format(hournow +1)]), chat)
        get_url(url) 
        time.sleep(2)
        url = URL +"sendMessage?text={}&chat_id={}".format("Goodbye{}.To find more information send /start".format(emoji.emojize(":waving_hand:")), chat)
        get_url(url)
        
        
    

    if text == "Today weather{}?".format(emoji.emojize(":closed_umbrella:")):
        print("lets see how the weather will hol' up")
        send_weather(text, chat)
        
    if text == "Want to Email Instructor?{}".format(emoji.emojize(":incoming_envelope:")):
        url = URL +"sendMessage?text={}&chat_id={}".format("I do not have the capability to display websites here but you can click this link to send yor email: https://outlook.office.com/mail.send ", chat)
        get_url(url)

        time.sleep(2.5)

        url = URL +"sendMessage?chat_id={}&redirect_uri=https://outlook.office.com/mail.send".format(chat)
        get_url(url)

        time.sleep(2)
        url = URL +"sendMessage?text={}&chat_id={}".format("Goodbye{}.To find more information send /start".format(emoji.emojize(":waving_hand:")), chat)
        get_url(url)


def main():
    while True:
        
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text) == "/start":
            
            send_message1(chat)
           

                    
        time.sleep(15)
    

text, chat = get_last_chat_id_and_text(get_updates())
if __name__ == '__main__':
    main()
        
