import instagram_private_api
import json
import codecs
import datetime
import os

def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object

def log(uname,pword):
    with open("login_data.json") as file_data:
        cached_settings = json.load(file_data, object_hook=from_json)

    api = instagram_private_api.Client(
        uname, pword,
        settings=cached_settings)

def getCommentors(user):
    commentors = []
    for i in api.user_feed(user):
        for j in i['items']:
            for k in j['caption']['preview_comments']:
                commentors.append(k['user']['username'])
    commentor_list = list(set(commentors))
    for i in commentor_list:
        if i == user: commentor_list.remove(i)
    return commentor_list

def writeCSV(objectofinterest, filename):
    with open("output/"+filename, "a") as f:
        try:
            for i in getCommentors(objectofinterest):
                f.write(objectofinterest + "," + i + "\n")
        except:
            pass

def final():
    uname = input("Username: ")
    pword = input("Password: ")
    filename = input("Filename: ")
    log(uname,pword)
    writeCSV(uname, filename)    
    os.system(f"java -jar mpv-shot0003.jar force-atlas-2 -i output/{filename} -o {filename}.png")

final()