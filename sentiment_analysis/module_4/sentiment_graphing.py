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


def csv_to_df(file_name: str, n_lines) -> DataFrame:
    df = read_csv(file_name, nrows=n_lines, sep='\t', header=None, names=['sentiments'])
    df['sentiment_count'] = df.groupby('sentiments')['sentiments'].transform('count')
    df.drop_duplicates(inplace=True)
    return df


def plot_sentiments(df: DataFrame, postTitle, fig_num, saveLoc) -> None:
    colors = ['green', 'gray', 'red']
    color = []

    print("Plotting figure {} for {}\n".format(fig_num, postTitle))
    plt.figure(postTitle)
    plt.bar(df['sentiments'], df['sentiment_count'], color=colors, label=df['sentiments'])
    plt.xlabel(list(df)[0])
    plt.ylabel('Quantity of Sentiment')
    plt.title("{} sentiments".format(postTitle))
    plt.legend(title="Sentiments")
    plt.savefig(saveLoc)
