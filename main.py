import webbrowser
import json
import os
from urllib import request

# Get json first
url = "http://raw.fastgit.org/ALKALiKong233/toolbox-json/master/dipper.json"
request.urlretrieve(url,"dipper.json")

# Parse json
with open ("dipper.json","r") as jsons:
    configs = json.load(jsons)

# Main code
print("[E]退出")
print("[A]下载 ROM ( Recovery 版)")
print("[B]下载 TWRP")
choice = "0"
while choice != "E":
    choice = input("请输入功能对应字母\n")
    if ( choice == "A" ):
        webbrowser.open_new(configs['rom'])
    elif ( choice == "B" ):
        webbrowser.open_new(configs['twrp'])
    elif ( choice == "E" ):
        break


