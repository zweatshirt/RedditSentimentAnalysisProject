"""
Authors: Zachery Linscott and Alex Wernex
Purpose:
    comment_sentiment():
        The input is a comment and the return value
        is the sentiment of the comment in the form of a string.
        A sentiment is a value which is either positive, negative, or neutral.
        The comment's sentiment polarity exists on a float scale between -1 and 1.
        If the polarity is negative, the sentiment is negative.
        if the polarity is positive and greater than 0, the sentiment is positive.
        if the polarity is 0, the sentiment is neutral.
"""

import subprocess
import sys


def install_tb():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'textblob'])


try:
    from textblob import TextBlob
except:
    install_tb()
    from textblob import TextBlob


def comment_sentiment(comment) -> str:
    blob = TextBlob(comment)
    p = blob.sentiment.polarity
    if p > 0:
        return 'positive'
    elif p < 0:
        return 'negative'
    else:
        return 'neutral'
