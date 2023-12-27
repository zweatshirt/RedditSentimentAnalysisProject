'''
Authors: Alex Wernex and Zachery Linscott
Purpose:
    This file simply takes the url and filepath of the raw HTML file                  #
    and outputs said file. All it does is call a premade function.
'''


import urllib.request


def save_raw_file(url, filename):
    urllib.request.urlretrieve(url, filename)
