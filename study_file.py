# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:41:20 2020

@author: salt_
"""

file = "./data/fox.txt"
#fileobj = open(file)
#text = fileobj.read()
#fileobj.close()
#print(text)
with open(file) as fileobj:
    text = fileobj.read()
    #print(text)
    newtext = text.rstrip(".")
    wordlist = newtext.split(" ")
    print(wordlist)