#!usr/bin/env python
import requests
from urllib.parse import urljoin
import re


class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.target_link = []

    def extract_link_from(self, url):
        try:
            response = requests.get(url).content.decode()
            return re.findall('(?:href=")(.*?)"', response)
        except UnicodeDecodeError:
            pass

    def crawl(self, url):
        href_links = self.extract_link_from(url)
        if href_links:
            for link in href_links:
                link = urljoin(url, link)
                if "#" in link:
                   link = link.split("#")[0]
                if self.target_url in link and link not in self.target_link:
                    self.target_link.append(link)
                    print(link)
                    self.crawl(link)

target_url = "https://login.classy.org/"
scanner = Scanner(target_url)
scanner.crawl(target_url)