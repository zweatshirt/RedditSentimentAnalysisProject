import os
from module_1.arg_parsing import arg_grabber
from module_1.html_download import save_raw_file
from module_2.extract_comments import *
from module_3.file_reading_writing import *
from module_4.comment_polarity import comment_sentiment
from module_4.sentiment_graphing import *

'''
Authors: Zachery Linscott and Alex Wernex
Purpose:
    run.py                                                                            
    This is the driver for the project.                                               
    It runs in the terminal with the file of urls                                            
    to process as an argument.                                                        
    First, it takes the names of the files you set                                    
    and creates the paths to the correct folders on your system.                      
    Then, it takes the URL from arg and passes to the three modules                   
    to save the post as a raw HTML file, extract the comments as                      
    data, and finally, saves those comments to a file.      
'''


def main():
    # points to file in need of reading
    file_arg = arg_grabber()
    with open(file_arg) as file:
        urls = [url.rstrip() for url in file]

    print("Running...")
    absolute_path = os.path.dirname(__file__)

    counter = 1
    for url in urls:

        # file naming for each url
        raw_file_name = 'HTMLOutput' + str(counter) + '.txt'
        relative_raw_path = "Data/raw/" + raw_file_name
        raw_file_name = os.path.join(absolute_path, relative_raw_path)
        processed_file_name = 'comments' + str(counter) + '.txt'
        relative_processed_path = "Data/processed/" + processed_file_name
        processed_file_name = os.path.join(absolute_path, relative_processed_path)
        sentiment_file_name = 'sentiments' + str(counter) + '.txt'
        relative_sentiment_path = "Data/sentiments/" + sentiment_file_name
        sentiment_file_name = os.path.join(absolute_path, relative_sentiment_path)
        graph_file_name = "graph" + str(counter) + '.png'
        relative_graph_path = "Data/Plots/" + graph_file_name
        graph_file_name = os.path.join(absolute_path, relative_graph_path)

        # extracting post title for each url
        post_title = url.split("/")[-2].replace("_", " ")

        # save the raw data to a file
        raw = save_raw_file(url, raw_file_name)
        print("HTML raw data saved to file {}!".format(raw_file_name))

        # extract cleaned comments from raw data
        comments = extract_comments(raw)
        print("Comments extracted!")

        # save the comments to a file
        # output_comments(comments, processed_file_name)
        print("Comments saved to file {}!".format(processed_file_name))

        # not necessary
        # grab processed/cleaned comments from comments.txt
        # comment_lst: [] = extract_file_lines(processed_file_name)
        comments_lst: [] = [c.strip() for c in comments]

        # analyze comment sentiments individually and store them in a list
        print("Analyzing the sentiment of each comment...")
        sentiments = [comment_sentiment(comment) for comment in comments_lst]

        # fist argument is the file name
        print("Comments and the sentiment of each comment saved in CSV format in {}!".format(sentiment_file_name))
        sentiments_file_write(sentiment_file_name, comments, sentiments)

        # read sentiment file and convert to df
        # would be faster to just read from the sentiments list but whatever.
        sentiments_df = csv_to_df(sentiment_file_name)
        plot_sentiments(sentiments_df, post_title, fig_num=counter, saveLoc=graph_file_name)
        counter += 1

    plt.show()
    print("Done!")


if __name__ == '__main__':
    main()
