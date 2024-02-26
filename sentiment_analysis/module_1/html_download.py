"""
Authors: Alex Wernex and Zachery Linscott
Purpose:
    This file simply takes the url and filepath of the raw HTML file                  #
    and outputs said file. All it does is call a pre-made function.
"""


import urllib.request
import urllib.error


def save_raw_file(url, filename):
    try:
        if 'www.' in url:
            url = url.replace('www.', 'old.')
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        fp.close()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(mystr)

        return mystr
    except urllib.error.URLError:
        print(urllib.error.URLError)
        print("If you are getting an SSL Certificate verify failed error,"
              " please run -- pip install --upgrade certifi\n or"
              "go /Applications/Python 3.10/Install Certificates.command and double click the file.")


