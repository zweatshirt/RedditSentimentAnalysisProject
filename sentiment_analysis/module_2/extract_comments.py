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


def extract_comments(h: str, file=False):
    if file:
        html_file = open(h, encoding='utf8')
        html = BeautifulSoup(html_file, 'html.parser')
    else:
        html = BeautifulSoup(h, 'html.parser')
    output = []
    comment_html = html.find_all(class_="entry unvoted")

    # for elem in comment_html:
    comments = html.find('body').find_all("div", class_='md')
    for comment in comments:
        output.append(comment.text)
    return output


