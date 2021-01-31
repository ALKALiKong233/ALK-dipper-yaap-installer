import webbrowser
import json
import os
from urllib import request
from tkinter import filedialog, Tk

# Get json first
url = "http://raw.fastgit.org/ALKALiKong233/toolbox-json/master/dipper.json"
request.urlretrieve(url,"dipper.json")

# Parse json
with open ("dipper.json","r") as jsons:
    configs = json.load(jsons)

# Main code
print("[E]退出")
print("[A]下载 ROM")
print("[B]下载 TWRP")
print("[C]通过 ADB Sideload 刷入 ROM")
print("[D]安装 Magisk")
print("[F]修复 Windows 10 中 Press Any Key to Shutdown ")
print("[G]安装 TWRP")
choice = "0"
while choice != "E":
    choice = input("请输入功能对应字母:")
    if ( choice == "A" ):
        webbrowser.open_new(configs['rom'])
    elif ( choice == "B" ):
        webbrowser.open_new(configs['twrp'])
    elif ( choice == "C" ):
        yaapzip = Tk()
        yaapzip.filename = filedialog.askopenfilename(initialdir = "C:\\",title = "选择安装包文件",filetypes = (("Zipped files","*.zip"),("all files","*.*")))
        print(yaapzip.filename)
        os.system(".\\platform-tools\\adb.exe sideload %s" % yaapzip.filename)
    elif ( choice == "D" ):
        magisk = Tk()
        magisk.filename = filedialog.askopenfilename(initialdir = "C:\\",title = "选择 Magisk 安装包",filetypes = (("Zipped files","*.zip"),("all files","*.*")))
        print(magisk.filename)
        os.system(".\\platform-tools\\adb.exe push %s /data/local/tmp/Magisk.zip" % magisk.filename)
        os.system(".\\platform-tools\\adb.exe push openrecoveryscript /cache/recovery/openrecoveryscript")
        os.system(".\\platform-tools\\adb.exe reboot recovery")
    elif ( choice == "F" ):
        os.system("fix.bat")
        print("运行完成")
    elif ( choice == "G" ):
        twrp = Tk()
        twrp.filename = filedialog.askopenfilename(initialdir = "C:\\",title = "选择 TWRP 镜像",filetypes = (("Imagine files","*.img"),("all files","*.*")))
        print(twrp.filename)
        choicee = input("是否使用 ADB 自动重启至 Fastboot 模式? (Y为是,n为否) [Y/n]:")
        if ( choicee == "Y" ):
            os.system(".\\platform-tools\\adb.exe reboot fastboot")
        else:
            pass
        os.system(".\\platform-tools\\fastboot.exe flash recovery %s" % twrp.filename)
        os.system("'.\\platform-tools\\fastboot.exe' reboot")
    elif ( choice == "E" ):
        break
