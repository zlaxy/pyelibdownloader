#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wget, os

print ("pyElibDownloader")
promptprefix = ("Enter prefix of download URL (default [http://elib.shpl.ru/pages/]): ")
prefix = input (promptprefix)
if prefix == "":
    prefix = ("http://elib.shpl.ru/pages/")
promptpostfix = ("Enter postfix of download URL (default [/zooms/7]): ")
postfix = input (promptpostfix)
if postfix == "":
    postfix = ("/zooms/7")
promptextension = ("Enter files extension (default [jpg]): ")
extension = input (promptextension)
if extension == "":
    extension = ("jpg")
promptdir = ("Enter directory name: ")
dir = ""
while dir == "":
    dir = input (promptdir)
promptfirstindex = ("Enter first index: ")
firstindex = ""
while firstindex == "":
    firstindex = input (promptfirstindex)
promptlastindex = ("Enter last index: ")
lastindex = ""
while lastindex == "":
    lastindex = input (promptlastindex)
print ("Starting donwload...")
try:
    os.stat(dir)
except:
    os.mkdir(dir)
os.chdir(dir)
index = int(firstindex)
lastindex = int(lastindex)
while index <= lastindex:
    filename = str(index) + "." + extension
    url = prefix + str(index) + postfix
    try:
      wget.download(url,out=filename)
    except:
      print ("...skipped...")
    index = index + 1
print ("Donwload finished.")
