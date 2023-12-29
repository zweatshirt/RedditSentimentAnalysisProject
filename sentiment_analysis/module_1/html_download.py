'''
Authors: Alex Wernex and Zachery Linscott
Purpose:
    This file simply takes the url and filepath of the raw HTML file                  #
    and outputs said file. All it does is call a premade function.
'''


import urllib.request
import urllib.error


def save_raw_file(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
    except urllib.error.URLError:
        print(urllib.error.URLError)
        print("If you are getting an SSL Certificate verify failed error,"
              " please run -- pip install --upgrade certifi\n or"
              "go /Applications/Python 3.10/Install Certificates.command and double click the file.")


