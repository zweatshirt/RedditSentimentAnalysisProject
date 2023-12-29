import subprocess
import sys


def install_bs4():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])


try:
    from bs4 import BeautifulSoup

except:
    install_bs4()
    from bs4 import BeautifulSoup

'''
Authors: Alex Wernex and Zachery Linscott
Purpose:
    extract_comments.py
    This file simply takes the filepath of the raw HTML file
    and outputs a list of the comments form the post. This function opens the file,
    parses through the file with BeautifulSoup looking for a class id associated with
    comments. Then it extracts just the text from the post and returns it as a list.
'''


def extract_comments(filename):
    html_file = open(filename, encoding='utf8')
    output = []
    html = BeautifulSoup(html_file, 'html.parser')

    comment_html = html.find_all(class_="entry unvoted")

    for elem in comment_html:
        comments = elem.find_all(class_='md')
        for comment in comments:
            output.append(comment.text)
    return output
