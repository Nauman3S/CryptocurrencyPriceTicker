import urllib.request
import json
import random
import json
import base64
import time
from datetime import datetime
import paho.mqtt.client as mqtt
MASTER_KILL_SWITCH=0

msgV=""
topicV=""
hastagValue='temp'
getDataFreq=30#seconds
tickerValue='BTC'
currency='USD'
def getFormatedFloat(s):
    val=float(s)

    formatted_float = "{:.2f}".format(val)
    return str(formatted_float)
def getCryptoData(ticker,curr):

    url='https://api.nomics.com/v1/currencies/ticker?key=449415bb572251fc1bff2887f0302627b0ca4f6c&ids='+ticker+'&convert='+curr
    url=url.replace(' ',"")
    f = urllib.request.urlopen(url)
    res=f.read()
    res=res.decode('utf-8')
    res=res.replace('[','')
    res=res.replace(']','')
   # print(res)

    val=json.loads(res)
    #print(val['name'])
    #print(val['price'])
    return val['name'] +' '+val['price']

def getMultiCryptoData(ticker,curr):

    url='https://api.nomics.com/v1/currencies/ticker?key=449415bb572251fc1bff2887f0302627b0ca4f6c&ids='+ticker+'&convert='+curr
    url=url.replace(' ',"")
    f = urllib.request.urlopen(url)
    res=f.read()
    res=res.decode('utf-8')
    # res=res.replace('[','')
    # res=res.replace(']','')
    #print(res)

    val=json.loads(res)
    #print(ticker.count(','))
    finalPlaod=""
    for i in range(0,ticker.count(',')+1):
        finalPlaod=finalPlaod+val[i]['name']+' '+getFormatedFloat(val[i]['price'])+' '

  
    finalPlaod=finalPlaod[:-1]
    return finalPlaod
# print(getMultiCryptoData('ADA,BTC','AUD'))
# exit(0)


def on_connect(client, userdata, rc):
    #print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("CPT-data/#")
    client.subscribe("CPT/config/currency")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global getDataFreq,tickerValue,currency
    global msgV,topicV, hastagValue
    #print(msg.topic+" "+str(msg.payload))
    topicV=str(msg.topic)
    msgV=str((msg.payload).decode('utf-8'))

    if('CPT' in topicV):
    
        tickerValue=msgV
        hastagValue=msgV
    if('currency' in topicV):
        currency=msgV
        
    
clientID_prefix=""
for i in range(0,6):
    clientID_prefix=clientID_prefix + str(random.randint(0,99999))


client = mqtt.Client("C1"+clientID_prefix)
#client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("CPT-data/#")
client.subscribe("CPT/config/currency")



client.loop_start()
lastTweet=''
oldtime = time.time()

while 1:
    
    # lastTweet=getTweet()
    try:
        if time.time() - oldtime >getDataFreq:
            getDataFreq=random.randint(0,50)
            oldtime=time.time()
            if(',' in tickerValue):
                multiCoinPayload=getMultiCryptoData(tickerValue,currency)
                
                client.publish('CPT/device/price',multiCoinPayload)  
                multiCoinPayload=""
            else:
                client.publish('CPT/device/price',getCryptoData(tickerValue,currency))  
    except Exception as e:
        print('Err', e)

