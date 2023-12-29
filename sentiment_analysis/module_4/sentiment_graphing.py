import random
import subprocess
import sys
from random import choice

def install_pd():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])


def install_pltl():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])

try:
    from pandas import DataFrame, read_csv

except:
    install_pd()
    from pandas import DataFrame, read_csv

try:
    import matplotlib.pyplot as plt

except:
    install_pltl()
    import matplotlib.pyplot as plt


'''
Authors: Zachery Linscott and Alex Wernex
Purpose:
    csv_to_df():
        Converts a the csv of Reddit comments with their sentiments into a dataframe.
    plot_sentiments():
        Plots a bar chart of the positive, neutral and negative sentiments counts.
'''


def csv_to_df(file_name: str) -> DataFrame:
    df = read_csv(file_name, sep='\t', header=None, names=['sentiments'], index_col=False)
    df['sentiment_count'] = df.groupby('sentiments')['sentiments'].transform('count')
    df.drop_duplicates(inplace=True)
    df = df.reset_index(drop=True)
    df = df.sort_values(by='sentiments', ascending=False)
    return df


def plot_sentiments(df: DataFrame, post_title, fig_num, save_loc) -> None:
    colors = ['green', 'gray', 'red']
    print("Plotting figure {} for {}\n".format(fig_num, post_title))

    plt.figure(post_title)
    plt.bar(df['sentiments'], df['sentiment_count'], color=colors, label=df['sentiments'])

    plt.xlabel(list(df)[0])
    plt.ylabel('Quantity of Sentiment')

    plt.title("{} sentiments".format(post_title))
    plt.legend(title="Sentiments")

    plt.savefig(save_loc)
