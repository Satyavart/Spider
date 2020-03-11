#!usr/bin/env python

import requests


def request(url):
    try:
        get_response = requests.get("http://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass


target = "google.com"
with open("files-and-dirs-wordlist.txt", "r") as file:
    content = file.read()
    content = content.split("\n")
    for line in content:
        url = target + '/' + line
        response = request(url)
        if response:
            with open("google.com_directories.txt", "a") as outfile:
                outfile.write(url + '\n')
