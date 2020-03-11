#!usr/bin/env python

import requests


def request(url):
    try:
        get_response = requests.get("http://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass


target = "google.com"
with open("subdomains-wodlist.txt", "r") as file:
    content = file.read()
    content = content.split("\n")
    for line in content:
        url = line + "." + target
        response = request(url)
        if response:
            with open("google.com.txt", "a") as outfile:
                outfile.write(url + '\n')
