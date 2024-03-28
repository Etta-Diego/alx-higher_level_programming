#!/usr/bin/python3
import urllib.request
""" This python script fetches https://alx-intranet.hbtn.io/status using the package urllib"""
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as feedback:
    hypertext = feedback.read()
print("Body response:")
print("\t- type: ", type(hypertext))
print("\t- content:", hypertext)
print("\t- utf8 content: ", hypertext.decode("utf-8"))
