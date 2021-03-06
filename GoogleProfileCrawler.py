#!/usr/bin/env python

import urllib,sys
from bs4 import BeautifulSoup as bs

def main():
    xml = bs(urllib.urlopen('http://www.gstatic.com/s2/sitemaps/profiles-sitemap.xml').read())
    for i in xml.findAll('loc'):
        szURL = i.text
        szLocalFile = i.text[35:]
        try:
            urllib.urlretrieve(szURL, szLocalFile)
            print("Downloaded %s" % szLocalFile)
        except Exception, err:
            print("%s could not be retrieved" % szURL)
    print("All done")

# Banner
def Banner():
    print("=================================================")
    print("GoogleProfile Crawler v0.1                       ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: ./%s\n") % (cmd)

if __name__ == "__main__":
    Banner()
    help_menu(sys.argv[0])
    main()
