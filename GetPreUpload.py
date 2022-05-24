#!/usr/bin/env python
# coding: utf-8
import requests
import json
import time
from time import strftime,gmtime,mktime,strptime
from . import config

def allID():
    return config.getIDs()
def allName():
    #print(config.getNames())
    return config.getNames()
def setting():
    return config.getSet()
        
def getToken():
    token_url = "https://login.microsoftonline.com/10f0f3b2-c2b5-445f-84f7-584515916a82/oauth2/token"
    token_data = setting()
    token_r = requests.post(token_url, data=token_data)
    token = token_r.json().get("access_token")
    return(token)
    
def getpostform(groupName):
    ID = allID()
    Post_json = {}
    Post_json['ids'] = ID[groupName]
    Post_json = json.dumps(Post_json)
    return(Post_json)
    
def getList(dict): 
    newdict = []
    for i in dict.keys():
        newdict.append(i)
    return newdict
def getTime(Timestr):
    newTime = strftime("%H:%M", gmtime(mktime(strptime(Timestr, "%a %b  %d %H:%M:%S %Y"))))
    return newTime
def getDate(Datestr):
    newDate = strftime("%Y-%m-%d", gmtime(mktime(strptime(Datestr, "%a %b  %d %H:%M:%S %Y"))))
    return newDate
def getDay(Datestr):
    newDate = strftime("%a", gmtime(mktime(strptime(Datestr, "%a %b  %d %H:%M:%S %Y"))))
    return newDate
    
def getGroupName():
    group = allID()
    name = getList(group)
    return(name)
    
def getDisplayname(userID):
    name = allName()
    return name[userID]
    
def getResponseData(groupName):
    post_url = 'https://graph.microsoft.com/beta/communications/getPresencesByUserId'
    token = getToken()
    headers = { 'Authorization': 'Bearer {}'.format(token)}
    postJson = getpostform(groupName)
    postJson = json.loads(postJson)
    user_response_data = json.loads(requests.post(post_url, headers=headers,json = postJson).text)
    return(user_response_data['value'])
    
def getPostform(num):
    seconds = time.time()
    local_time = time.ctime(seconds)
    days = getDay(local_time)
    timere = getTime(local_time)
    if(days != "Sun" and days != "Sat" and timere < '10:00'):
        seconds = seconds + 28800
        local_time = time.ctime(seconds)
        groupName = getGroupName()
        postform = {}
        postform["timestamp"] = local_time
        postform["groupName"] = groupName[num]
        detail = []
        Data = getResponseData(groupName[num])
        for i in Data:
            index = {}
            index["displayname"]=getDisplayname(i["id"])
            index["activity"] = i["activity"]
            detail.append(index)
        postform["records"] = detail
        return(postform)
    
def postDB():
    db_url = "https://graphapialex.azurewebsites.net/api/HttpTriggerApi?code=5aQUp8YwEb2AZJnUNQbrqQyzHNaG0ffzpgrdEMQaY7MKF2RnhOKhKQ=="
    gname = getGroupName()
    for i in range(len(gname)):
        print(i)
        post_form = getPostform(i)
        print(post_form)
        Result_upload = requests.post(db_url,json = post_form).text
    return Result_upload


